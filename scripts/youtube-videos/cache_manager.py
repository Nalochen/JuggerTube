import json
from pathlib import Path

# Cache configuration
CACHE_DIR = Path("cache")
YOUTUBE_CACHE_FILE = CACHE_DIR / "youtube_videos_cache.json"

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