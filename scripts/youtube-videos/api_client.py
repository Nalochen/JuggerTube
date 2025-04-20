import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from error_logger import log_video_error

# Disable SSL verification warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# API configuration
CREATE_VIDEOS_URL = 'https://localhost:8080/api/video-frontend/create-multiple-videos'

def send_videos_to_api(videos_data):
    """Send video data to the API and handle responses"""
    if not videos_data:
        return
        
    payload = {"videos": videos_data}
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Host': 'localhost:8080'
    }
    
    try:
        print("Sending payload:", payload)
        
        response = requests.post(
            CREATE_VIDEOS_URL, 
            json=payload,
            headers=headers,
            verify=False  # Disable SSL verification for local development only
        )
        print(f"API Response Status: {response.status_code}")
        
        # Handle non-200 status codes
        if response.status_code != 200:
            error_msg = f"Error: Server returned status code {response.status_code}"
            print(error_msg)
            _log_error_for_all_videos(videos_data, f"{error_msg}. Response: {response.text}")
            return
        
        if response.text:
            _handle_api_response(response, videos_data)
            
    except requests.exceptions.ConnectionError as e:
        error_msg = f"Connection Error: Could not connect to the server. Is it running? Error: {str(e)}"
        print(error_msg)
        _log_error_for_all_videos(videos_data, error_msg)
    except Exception as e:
        error_msg = f"Error sending data to API: {str(e)}"
        print(error_msg)
        _log_error_for_all_videos(videos_data, error_msg)

def _handle_api_response(response, videos_data):
    """Handle the API response and log any errors"""
    try:
        response_data = response.json()
        print(f"Response content: {response_data}")
        
        if not isinstance(response_data, dict):
            return
            
        # Handle different possible error response formats
        errors = []
        if 'errors' in response_data:
            errors = response_data['errors']
        elif 'error' in response_data:
            errors = [response_data['error']]
        elif 'message' in response_data and response.status_code != 200:
            errors = [{'message': response_data['message']}]
            
        print(f"Found {len(errors)} errors to process")
        
        for error in errors:
            error_msg = error.get('message', 'Unknown error')
            if "Video with this name already exists" in error_msg:
                continue
                
            # Try to match error to video
            video_name = error.get('videoName')
            matched_video = None
            
            if video_name:
                matched_video = next((v for v in videos_data if v['name'] == video_name), None)
            
            if not matched_video and len(videos_data) == 1:
                matched_video = videos_data[0]
            
            if matched_video:
                print(f"Logging error for video: {matched_video['name']}")
                _log_error_for_video(matched_video, error_msg)
            else:
                print("Could not match error to specific video, logging for all videos")
                _log_error_for_all_videos(videos_data, error_msg)
                
    except ValueError as e:
        print(f"Error parsing response JSON: {e}")
        print(f"Raw response: {response.text}")
        _log_error_for_all_videos(videos_data, f"Failed to parse API response: {response.text}")

def _log_error_for_video(video_data, error_msg):
    """Log error for a single video"""
    if "name" not in video_data:
        return

    log_video_error(
        video_name=video_data['name'],
        tournament_name=video_data.get('tournamentName'),
        team_one_name=video_data.get('teamOneName'),
        team_two_name=video_data.get('teamTwoName'),
        error_message=error_msg
    )

def _log_error_for_all_videos(videos_data, error_msg):
    """Log error for all videos in the payload"""
    for video_data in videos_data:
        _log_error_for_video(video_data, error_msg) 