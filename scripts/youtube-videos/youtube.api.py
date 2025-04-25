from googleapiclient.discovery import build
from cache_manager import load_cache, save_cache
from video_processor import process_video_data
from api_client import send_videos_to_api
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
from pathlib import Path
from datetime import datetime

# Disable SSL verification warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Cache configuration
CACHE_DIR = Path("cache")
YOUTUBE_CACHE_FILE = CACHE_DIR / "youtube_videos_cache.json"
ERROR_LOG_FILE = CACHE_DIR / "youtube_errors.json"

def ensure_cache_dir():
    """Ensure the cache directory exists"""
    CACHE_DIR.mkdir(exist_ok=True)

def load_cache():
    """Load cached YouTube video data"""
    ensure_cache_dir()
    videos_cache = {}
    
    try:
        if YOUTUBE_CACHE_FILE.exists():
            with open(YOUTUBE_CACHE_FILE, 'r') as f:
                videos_cache = json.load(f)
    except Exception as e:
        print(f"Error loading YouTube videos cache: {e}")
    
    return videos_cache

def save_cache(videos_data):
    """Save YouTube video data to cache file"""
    ensure_cache_dir()
    
    try:
        with open(YOUTUBE_CACHE_FILE, 'w') as f:
            json.dump(videos_data, f, indent=2)
    except Exception as e:
        print(f"Error saving YouTube videos cache: {e}")

def load_error_log():
    """Load existing error log"""
    ensure_cache_dir()
    error_log = []
    
    try:
        if ERROR_LOG_FILE.exists():
            with open(ERROR_LOG_FILE, 'r') as f:
                error_log = json.load(f)
    except Exception as e:
        print(f"Error loading error log: {e}")
    
    return error_log

def save_error_log(error_log):
    """Save error log to file"""
    ensure_cache_dir()
    
    try:
        with open(ERROR_LOG_FILE, 'w') as f:
            json.dump(error_log, f, indent=2)
    except Exception as e:
        print(f"Error saving error log: {e}")

def log_video_error(video_name, tournament_name, team_one_name, team_two_name, error_message):
    """Log video processing error with relevant details"""
    if "Video with this name already exists" in error_message:
        return
        
    error_log = load_error_log()
    error_entry = {
        "timestamp": datetime.now().isoformat(),
        "videoName": video_name,
        "tournamentName": tournament_name,
        "teamOneName": team_one_name,
        "teamTwoName": team_two_name,
        "errorMessage": error_message
    }
    error_log.append(error_entry)
    save_error_log(error_log)

# Change URL depending on the environment
create_videos_url = 'https://localhost:8080/api/video-frontend/create-multiple-videos'

def fetch_youtube_videos(youtube, channel_id, videos_cache):
    """Fetch videos from YouTube channel and process them"""
    # Get channel data including customUrl
    response = youtube.channels().list(
        part='contentDetails,snippet',
        id=channel_id
    ).execute()

    playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    channel_custom_url = response['items'][0]['snippet'].get('customUrl', '')
    
    # Fetch all videos from the playlist
    youtube_videos = []
    next_page_token = None
    
    while True:
        playlist_items_response = youtube.playlistItems().list(
            part='snippet',
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        for item in playlist_items_response['items']:
            video_id = item['snippet']['resourceId']['videoId']
            
            # Add channel custom URL to each video item
            item['snippet']['customUrl'] = channel_custom_url

            # Check cache
            if video_id in videos_cache:
                print(f"Using cached data for video {video_id}")
                youtube_videos.append(item)
                continue
            
            youtube_videos.append(item)
            videos_cache[video_id] = item
        
        next_page_token = playlist_items_response.get('nextPageToken')
        if not next_page_token:
            break
    
    return youtube_videos

def process_youtube_videos(youtube_videos):
    """Process YouTube videos and separate them into valid and other videos"""
    videos_data = []
    videos_other_naming = []
    
    for youtube_video in youtube_videos:
        video_data, is_valid = process_video_data(youtube_video)
        
        if is_valid:
            videos_data.append(video_data)
        else:
            videos_other_naming.append({
                video_data['name'],
                video_data['videoLink']
            })
    
    return videos_data, videos_other_naming

def save_other_naming(channel_id, videos_other_naming):
    """Save unmatched videos to a file"""
    with open(f"{channel_id}OtherNaming.txt", "w", encoding="utf-8") as out_file:
        for video in videos_other_naming:
            line = f"{video}\n"
            out_file.write(line)

def main(channel_id):
    # Load cached data
    videos_cache = load_cache()
    
    # Initialize YouTube API
    api_key = 'AIzaSyCd4irgsASp6cb393tAgYBTXacjGq2YG3E'
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    # Fetch videos from YouTube
    youtube_videos = fetch_youtube_videos(youtube, channel_id, videos_cache)
    
    # Save updated cache
    save_cache(videos_cache)
    
    # Process videos
    videos_data, videos_other_naming = process_youtube_videos(youtube_videos)
    
    # Send valid videos to API
    send_videos_to_api(videos_data)
    
    # Save unmatched videos
    save_other_naming(channel_id, videos_other_naming)

if __name__ == "__main__":
    channel_ids = [
        'UCIp0Z0R5BNYoRTFG-1s5Y9g',
        'UC1EXd2J8aqwiKC64yvIMKGQ',
        'UCvdd5RoFdmzJhBTeesXZ6og'
    ]
    
    for channel in channel_ids:
        main(channel)
