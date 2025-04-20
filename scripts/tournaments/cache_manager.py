import json
from pathlib import Path

# Cache file paths
CACHE_DIR = Path("cache")
TOURNAMENTS_CACHE_FILE = CACHE_DIR / "tournaments_cache.json"
TEAMS_CACHE_FILE = CACHE_DIR / "teams_cache.json"

def ensure_cache_dir():
    """Ensure the cache directory exists"""
    CACHE_DIR.mkdir(exist_ok=True)

def load_cache():
    """Load cached tournament and team data"""
    ensure_cache_dir()
    tournaments_cache = {}
    teams_cache = {}
    
    try:
        if TOURNAMENTS_CACHE_FILE.exists():
            with open(TOURNAMENTS_CACHE_FILE, 'r') as f:
                tournaments_cache = json.load(f)
    except Exception as e:
        print(f"Error loading tournaments cache: {e}")
    
    try:
        if TEAMS_CACHE_FILE.exists():
            with open(TEAMS_CACHE_FILE, 'r') as f:
                teams_cache = json.load(f)
    except Exception as e:
        print(f"Error loading teams cache: {e}")
    
    return tournaments_cache, teams_cache

def save_cache(tournaments_data, teams_data):
    """Save tournament and team data to cache files"""
    ensure_cache_dir()
    
    try:
        with open(TOURNAMENTS_CACHE_FILE, 'w') as f:
            json.dump(tournaments_data, f, indent=2)
    except Exception as e:
        print(f"Error saving tournaments cache: {e}")
    
    try:
        with open(TEAMS_CACHE_FILE, 'w') as f:
            json.dump(teams_data, f, indent=2)
    except Exception as e:
        print(f"Error saving teams cache: {e}") 