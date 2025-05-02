from enum import Enum

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

CATEGORY_MAPPING = {
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

TARGET_SHEETS = ['DATA-Videos', 'DATA-Teams', 'DATA-Channels', 'Output-Tournaments'] 