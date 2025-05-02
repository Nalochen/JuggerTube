import pandas as pd
import numpy as np
from enum import Enum
import requests
import json
from urllib3.exceptions import InsecureRequestWarning
import time
import math

# Disable SSL verification warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Define VideoCategoriesEnum to match the backend enum
class VideoCategoriesEnum(Enum):
    AWARDS = 'awards'
    HIGHLIGHTS = 'highlights'
    MATCH = 'match'
    OTHER = 'other'
    PODCAST = 'podcast'
    REPORTS = 'reports'
    SONG = 'song'
    SPARBUILDING = 'sparbuilding'
    TRAINING = 'training'

# Path to the Excel file
excel_file = 'Liste aller Juggervideos _ JuggerTube.xlsx'

# Create a mapping from Excel categories to Enum categories
category_mapping = {
    'Reports // Berichte': 'reports',
    'Match // Spielvideo': 'match',
    'Berichte': 'reports',
    'Channel': 'other',
    'Highlights': 'highlights',
    'How to make spars // Pompfenbau': 'sparbuilding',
    'Musik': 'song',
    'Musikvideo': 'song',
    'Other // Diverse': 'other',
    'Podcast': 'podcast',
    'Siegerehrung': 'awards',
    'Single Competition': 'match',
    'Song': 'song',
    'Training & Tutorial': 'training'
}

# Specify the sheets we want to analyze
target_sheets = ['DATA-Videos', 'DATA-Teams', 'DATA-Channels', 'Output-Tournaments']

# Read all sheets from the Excel file
excel = pd.ExcelFile(excel_file)

# Dictionaries to store channels and teams
channels_dict = {}
teams_dict = {}
videos_dict = {}

# Get valid category values
valid_categories = {category.value for category in VideoCategoriesEnum}

# Iterate through target sheets
for sheet_name in target_sheets:
    if sheet_name not in excel.sheet_names:
        print(f"\nWarning: Sheet '{sheet_name}' not found in the Excel file.")
        continue

    # Read the sheet into a DataFrame
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    
    if sheet_name == 'DATA-Channels':
        # Process channels
        print(f"\n{'='*50}")
        print("Channels Dictionary:")
        print('='*50)
        
        for _, row in df.iterrows():
            # Skip if both CustomUrl and Link are missing
            if pd.isna(row['CustomUrl']) and pd.isna(row['Link']):
                continue
                
            # Use CustomUrl if available, otherwise use Link
            channel_link = row['CustomUrl'] if pd.notna(row['CustomUrl']) else row['Link']
            
            channels_dict[row['name']] = {
                'channelLink': channel_link,
                'name': row['name']
            }
        
        # Print channels dictionary
        for channel_name, data in channels_dict.items():
            print(f"Name: {data['name']}")
            print(f"Link: {data['channelLink']}")
            
    elif sheet_name == 'DATA-Teams':
        # Process teams
        print(f"\n{'='*50}")
        print("Teams Dictionary:")
        print('='*50)
        
        for _, row in df.iterrows():
            # Replace NaN city with "Mixteam"
            city = row['City/Ort']
            if pd.isna(city):
                city = "Mixteam"
                
            teams_dict[row['Teamname']] = {
                'city': city
            }
        
        # Print teams dictionary
        for team_name, data in teams_dict.items():
            print(f"\nTeam: {team_name}")
            print(f"City: {data['city']}")
            
    elif sheet_name == 'DATA-Videos':
        # Process videos
        print(f"\n{'='*50}")
        print("Videos Dictionary:")
        print('='*50)
        
        for idx, row in df.iterrows():
            excel_category = row['Category'] if pd.notna(row['Category']) else 'Other // Diverse'
            # Map the Excel category to enum category
            category = category_mapping.get(excel_category, 'other')
            
            # Create base video object
            video_obj = {
                'name': row['Videoname'],
                'category': category,
                'videoLink': row['Link'],
                'uploadDate': row['Date of Upload'],
                'channel': row['Channel'],
                'comment': row['Comment'] if pd.notna(row['Comment']) else None,
                'dateOfRecording': row['Date of Recording'] if pd.notna(row['Date of Recording']) else None
            }

            # Add category-specific fields
            # Topic field - required for REPORTS, optional for others
            if category == 'reports' or (category in ['sparbuilding', 'training', 'other', 'podcast', 'highlights'] and pd.notna(row.get('Topic'))):
                if category == 'reports' and pd.isna(row.get('Topic')):
                    print(f"Warning: Missing required 'Topic' for REPORTS video: {row['Videoname']}")
                video_obj['topic'] = row['Topic'] if pd.notna(row.get('Topic')) else None

            # Guests field - optional for specific categories
            if category in ['sparbuilding', 'other', 'podcast', 'highlights'] and pd.notna(row.get('Guests')):
                video_obj['guests'] = row['Guests']

            # Weapon Type field - required for SPARBUILDING, optional for TRAINING
            if category == 'sparbuilding':
                if pd.isna(row.get('Type of weapon')):
                    print(f"Warning: Missing required 'Type of weapon' for SPARBUILDING video: {row['Videoname']}")
                video_obj['weaponType'] = row['Type of weapon'] if pd.notna(row.get('Type of weapon')) else None
            elif category == 'training' and pd.notna(row.get('Type of weapon')):
                video_obj['weaponType'] = row['Type of weapon']

            # Game System field - required for MATCH
            if category == 'match':
                if pd.isna(row.get('System')):
                    print(f"Warning: Missing required 'System' for MATCH video: {row['Videoname']}")
                video_obj['gameSystem'] = row['System'] if pd.notna(row.get('System')) else None

            # Tournament Name field - required for MATCH, optional for HIGHLIGHTS and AWARDS
            if category == 'match':
                if pd.isna(row.get('Tournament')):
                    print(f"Warning: Missing required 'Tournament' for MATCH video: {row['Videoname']}")
                video_obj['tournamentName'] = row['Tournament'] if pd.notna(row.get('Tournament')) else None
            elif category in ['highlights', 'awards'] and pd.notna(row.get('Tournament')):
                video_obj['tournamentName'] = row['Tournament']

            # Team names - required for MATCH
            if category == 'match':
                if pd.isna(row.get('Team 1')):
                    print(f"Warning: Missing required 'Team 1' for MATCH video: {row['Videoname']}")
                if pd.isna(row.get('Team 2')):
                    print(f"Warning: Missing required 'Team 2' for MATCH video: {row['Videoname']}")
                video_obj['teamOneName'] = row['Team 1'] if pd.notna(row.get('Team 1')) else None
                video_obj['teamTwoName'] = row['Team 2'] if pd.notna(row.get('Team 2')) else None

            videos_dict[idx] = video_obj
        
        # Print first 3 videos from dictionary
        print("\nFirst 3 videos:")
        for idx in list(videos_dict.keys())[:3]:
            video = videos_dict[idx]
            print(f"\nVideo {idx + 1}:")
            print(f"Name: {video['name']}")
            print(f"Category: {video['category']}")
            print(f"Video Link: {video['videoLink']}")
            print(f"Upload Date: {video['uploadDate']}")
            print(f"Channel Name: {video['channel']}")
            print(f"Comment: {video['comment']}")
            print(f"Date of Recording: {video['dateOfRecording']}")
            
            # Print category-specific fields if they exist
            if 'topic' in video:
                print(f"Topic: {video['topic']}")
            if 'guests' in video:
                print(f"Guests: {video['guests']}")
            if 'weaponType' in video:
                print(f"Weapon Type: {video['weaponType']}")
            if 'gameSystem' in video:
                print(f"Game System: {video['gameSystem']}")
            if 'tournamentName' in video:
                print(f"Tournament: {video['tournamentName']}")
            if 'teamOneName' in video:
                print(f"Team 1: {video['teamOneName']}")
            if 'teamTwoName' in video:
                print(f"Team 2: {video['teamTwoName']}")
            
    elif sheet_name == 'Output-Tournaments':
        # For tournaments sheet, print first 3 rows as before
        print(f"\n{'='*50}")
        print(f"Sheet: {sheet_name}")
        print('='*50)
        
        # Print column headers
        print("\nColumns:")
        for col in df.columns:
            print(f"- {col}")
        
        # Print first 3 rows
        print("\nFirst 3 rows:")
        print(df.head(3).to_string())
    
# Function to check if a value is JSON serializable
def clean_value(value):
    if pd.isna(value) or (isinstance(value, float) and (math.isnan(value) or math.isinf(value))):
        return None
    return str(value) if value is not None else None

# Function to send data to backend
def send_data_to_backend(endpoint, data, entity_name):
    try:
        response = requests.post(
            f'https://localhost:8080{endpoint}',
            json=data,
            verify=False  # Since it's localhost, we can skip SSL verification
        )
        response.raise_for_status()
        print(f"\nSuccessfully sent {entity_name} data to backend")
        return True
    except requests.exceptions.RequestException as e:
        print(f"\nError sending {entity_name} data to backend: {str(e)}")
        if hasattr(e, 'response') and hasattr(e.response, 'text'):
            print(f"Response content: {e.response.text}")
        return False

# After processing all sheets, send data to backend
if __name__ == "__main__":
    # First, send teams data
    teams_list = []
    for name, data in teams_dict.items():
        team_data = {
            "name": clean_value(name),
            "city": clean_value(data["city"])
        }
        if team_data["name"] and team_data["city"]:  # Only add if both values are valid
            teams_list.append(team_data)
    
    teams_payload = {"teams": teams_list}
    send_data_to_backend(
        '/api/team-frontend/create-multiple-teams',
        teams_payload,
        'teams'
    )
    print("\nProceeding with channels...")

    # Then, send channels data
    channels_list = []
    for data in channels_dict.values():
        channel_data = {
            "name": clean_value(data["name"]),
            "channelLink": clean_value(data["channelLink"])
        }
        if channel_data["name"] and channel_data["channelLink"]:  # Only add if both values are valid
            channels_list.append(channel_data)
    
    channels_payload = {"channels": channels_list}
    send_data_to_backend(
        '/api/channel-frontend/create-multiple-channels',
        channels_payload,
        'channels'
    )
    print("\nProceeding with videos...")

    # Wait a short time to ensure teams and channels are processed
    time.sleep(2)
    
    # Convert videos dictionary to list
    videos_list = []
    for video in videos_dict.values():
        video_data = {
            "name": clean_value(video["name"]),
            "category": clean_value(video["category"]).lower(),  # Ensure category is lowercase
            "videoLink": clean_value(video["videoLink"]),
            "channelName": clean_value(video["channel"]),  # This maps from Excel's "channel" to API's "channelName"
            "uploadDate": clean_value(video["uploadDate"]),
            "dateOfRecording": clean_value(video["dateOfRecording"]) if video.get("dateOfRecording") else None,
            "comment": clean_value(video["comment"]) if video.get("comment") else None
        }
        
        # Add category-specific fields based on the category
        if video_data["category"] == "reports":
            video_data["topic"] = clean_value(video.get("topic", ""))
        elif video_data["category"] == "match":
            video_data["gameSystem"] = "sets"  # Default to sets as per handler
            if "teamOneName" in video:
                video_data["teamOneName"] = clean_value(video["teamOneName"])
            if "teamTwoName" in video:
                video_data["teamTwoName"] = clean_value(video["teamTwoName"])
            if "tournamentName" in video:
                video_data["tournamentName"] = clean_value(video["tournamentName"])
        elif video_data["category"] == "sparbuilding":
            video_data["weaponType"] = clean_value(video.get("weaponType", ""))
            video_data["topic"] = clean_value(video.get("topic", ""))
        
        # Print debug information for each video
        print(f"\nProcessing video: {video_data['name']}")
        print(f"Channel Name: {video_data['channelName']}")
        
        # Only add if all required fields are present and non-empty
        required_fields = ["name", "category", "videoLink", "uploadDate", "channelName"]
        missing_fields = [field for field in required_fields if not video_data.get(field)]
        
        if not missing_fields:
            videos_list.append(video_data)
        else:
            print(f"\nSkipping video '{video_data.get('name', 'Unknown')}' due to missing required fields: {', '.join(missing_fields)}")
    
    videos_payload = {"videos": videos_list}
    
    # Print the first video data for debugging
    if videos_list:
        print("\nFirst video data example:")
        print(json.dumps(videos_list[0], indent=2))
    else:
        print("\nNo valid videos to send!")
    
    videos_success = send_data_to_backend(
        '/api/video-frontend/create-multiple-videos',
        videos_payload,
        'videos'
    )

    if videos_success:
        print("\nAll data successfully sent to backend!")
    else:
        print("\nFailed to send videos data to backend")

print("\nAnalysis complete!") 