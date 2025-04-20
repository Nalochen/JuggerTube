import json
from pathlib import Path
from datetime import datetime

# Error logging configuration
CACHE_DIR = Path("cache")
ERROR_LOG_FILE = CACHE_DIR / "youtube_errors.json"

def ensure_cache_dir():
    """Ensure the cache directory exists"""
    CACHE_DIR.mkdir(exist_ok=True)

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