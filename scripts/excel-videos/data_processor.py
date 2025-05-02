import pandas as pd
from typing import Dict, List
from datetime import datetime
from helpers import clean_value
from enums import CATEGORY_MAPPING
from validation_logger import log_validation_error
import re

def convert_date_to_iso(date_value) -> str:
    """Convert date to ISO format string."""
    if pd.isna(date_value):
        return None
    
    if isinstance(date_value, str):
        try:
            # Try German format (DD.MM.YYYY)
            day, month, year = date_value.split('.')
            date_obj = datetime(int(year), int(month), int(day))
            return date_obj.isoformat()
        except (ValueError, AttributeError):
            return None
    
    # If it's already a datetime object (from pandas)
    return date_value.isoformat()

class DataProcessor:
    def __init__(self, excel_file: str):
        self.excel_file = excel_file
        self.excel = pd.ExcelFile(excel_file)
        self.channels_dict = {}
        self.teams_dict = {}
        self.videos_dict = {}

    def process_channels(self, df: pd.DataFrame) -> Dict:
        """Process channels data from DataFrame."""
        for _, row in df.iterrows():
            if pd.isna(row['CustomUrl']) and pd.isna(row['Link']):
                continue
            
            channel_link = row['CustomUrl'] if pd.notna(row['CustomUrl']) else row['Link']
            self.channels_dict[row['name']] = {
                'channelLink': channel_link,
                'name': row['name']
            }
        return self.channels_dict

    def process_teams(self, df: pd.DataFrame) -> Dict:
        """Process teams data from DataFrame."""
        for _, row in df.iterrows():
            city = row['City/Ort'] if pd.notna(row['City/Ort']) else "Mixteam"
            self.teams_dict[row['Teamname']] = {'city': city}
        return self.teams_dict

    def process_videos(self, df: pd.DataFrame) -> Dict:
        """Process videos data from DataFrame."""
        for idx, row in df.iterrows():
            excel_category = row['Category'] if pd.notna(row['Category']) else 'Other // Diverse'
            category = CATEGORY_MAPPING.get(excel_category, 'other')
            
            video_obj = self._create_base_video_object(row, category)
            self._add_category_specific_fields(video_obj, row, category)
            self.videos_dict[idx] = video_obj
            
        return self.videos_dict

    def _create_base_video_object(self, row: pd.Series, category: str) -> Dict:
        """Create base video object with common fields."""
        return {
            'name': row['Videoname'],
            'category': category,
            'videoLink': row['Link'],
            'uploadDate': row['Date of Upload'],
            'channel': row['Channel'],
            'comment': row['Comment'] if pd.notna(row['Comment']) else None,
            'dateOfRecording': row['Date of Recording'] if pd.notna(row['Date of Recording']) else None
        }

    def _add_category_specific_fields(self, video_obj: Dict, row: pd.Series, category: str):
        """Add category-specific fields to video object."""
        # Topic field
        if category == 'reports' or (category in ['sparbuilding', 'training', 'other', 'podcast', 'highlights'] and pd.notna(row.get('Topic'))):
            video_obj['topic'] = row['Topic'] if pd.notna(row.get('Topic')) else None

        # Guests field
        if category in ['sparbuilding', 'other', 'podcast', 'highlights'] and pd.notna(row.get('Guests')):
            video_obj['guests'] = row['Guests']

        # Weapon Type field
        if category == 'sparbuilding' or (category == 'training' and pd.notna(row.get('Type of weapon'))):
            video_obj['weaponType'] = row['Type of weapon'] if pd.notna(row.get('Type of weapon')) else None

        # Game System and Tournament fields for matches
        if category == 'match':
            video_obj.update({
                'gameSystem': row['System'] if pd.notna(row.get('System')) else None,
                'tournamentName': row['Tournament'] if pd.notna(row.get('Tournament')) else None,
                'teamOneName': row['Team 1'] if pd.notna(row.get('Team 1')) else None,
                'teamTwoName': row['Team 2'] if pd.notna(row.get('Team 2')) else None
            })
        elif category in ['highlights', 'awards'] and pd.notna(row.get('Tournament')):
            video_obj['tournamentName'] = row['Tournament']

    def _clean_youtube_url_from_name(self, name: str) -> str:
        """Remove YouTube URLs from video names."""
        if not name:
            return name
        # Pattern matches both youtu.be and youtube.com URLs at the end of the string
        youtube_pattern = r'\s*(?:https?://)?(?:(?:www\.)?youtube\.com/\S+|youtu\.be/\S+)\s*$'
        return re.sub(youtube_pattern, '', name).strip()

    def prepare_data_for_api(self) -> tuple[List[Dict], List[Dict], List[Dict]]:
        """Prepare processed data for API submission."""
        teams_list = [
            {"name": clean_value(name), "city": clean_value(data["city"])}
            for name, data in self.teams_dict.items()
            if clean_value(name) and clean_value(data["city"])
        ]

        channels_list = [
            {"name": clean_value(data["name"]), "channelLink": clean_value(data["channelLink"])}
            for data in self.channels_dict.values()
            if clean_value(data["name"]) and clean_value(data["channelLink"])
        ]

        videos_list = []
        for video in self.videos_dict.values():
            video_data = self._prepare_video_for_api(video)
            if self._validate_video_data(video_data):
                videos_list.append(video_data)

        return teams_list, channels_list, videos_list

    def _prepare_video_for_api(self, video: Dict) -> Dict:
        """Prepare a single video for API submission."""
        video_data = {
            "name": clean_value(self._clean_youtube_url_from_name(video["name"])),
            "category": clean_value(video["category"]).lower(),
            "videoLink": clean_value(video["videoLink"]),
            "channelName": clean_value(video["channel"]),
            "uploadDate": convert_date_to_iso(video["uploadDate"]),
            "dateOfRecording": convert_date_to_iso(video.get("dateOfRecording")),
            "comment": clean_value(video.get("comment"))
        }

        # Add category-specific fields
        if video_data["category"] == "reports":
            video_data["topic"] = clean_value(video.get("topic"))
        elif video_data["category"] == "match":
            video_data.update({
                "gameSystem": "sets",
                "teamOneName": clean_value(video.get("teamOneName")),
                "teamTwoName": clean_value(video.get("teamTwoName")),
                "tournamentName": clean_value(video.get("tournamentName"))
            })
        elif video_data["category"] == "sparbuilding":
            video_data.update({
                "weaponType": clean_value(video.get("weaponType")),
                "topic": clean_value(video.get("topic"))
            })
        elif video_data["category"] in ["highlights", "awards"]:
            video_data["tournamentName"] = clean_value(video.get("tournamentName"))

        return video_data

    def _validate_video_data(self, video_data: Dict) -> bool:
        """Validate required fields for video data."""
        required_fields = ["name", "category", "videoLink", "uploadDate", "channelName"]
        missing_fields = [field for field in required_fields if not video_data.get(field)]
        
        if missing_fields:
            log_validation_error(video_data, missing_fields)
            return False
            
        return True 