def clean_tournament_name(tournament_name):
    """Clean tournament name by removing the year if present"""
    if not tournament_name or len(tournament_name) <= 5:
        return tournament_name
        
    tournament_name = tournament_name.strip()
    last_five = tournament_name[-5:]
    
    # Check if last 4 chars are numbers and start with "20"
    if last_five[0] == " " and last_five[1:3] == "20" and last_five[3:].isdigit():
        return tournament_name[:-5]
    
    return tournament_name

def clean_video_name(video_name):
    """Clean video name by removing common prefixes"""
    prefixes_to_remove = [
        'Kleines Finale ', 'KLEINES FINALE ',
        'Finale ', 'FINALE ',
        'Halbfinale ', 'HALBFINALE ',
        'Viertelfinale ', 'VIERTELFINALE ',
        'Gruppenphase ',
        'MULTICAM! ', 'DUAL CAM ', 'MULTICAM ',
        'GRAND FINAL WCC 2023  '
    ]
    
    for prefix in prefixes_to_remove:
        if video_name.find(prefix) > -1:
            video_name = video_name.replace(prefix, '')
    
    return video_name

def extract_video_details(video_name):
    """Extract team names and tournament from video name"""
    team_one = None
    team_two = None
    tournament = None
    
    # Extract team names
    if ' gegen ' in video_name:
        team_one = video_name.split(' gegen ')[0].strip()
        if ' | ' in video_name:
            team_two = video_name.split(' gegen ')[1].split(' | ')[0].strip()
    elif ' vs ' in video_name:
        team_one = video_name.split(' vs ')[0].strip()
        if ' | ' in video_name:
            team_two = video_name.split(' vs ')[1].split(' | ')[0].strip()
        elif ' (' in video_name:
            team_two = video_name.split(' vs ')[1].split(' (')[0].strip()
    
    # Extract tournament name
    if ' | ' in video_name and ' [Jugger]' in video_name:
        tournament = video_name.split(' | ')[1].split(' [Jugger]')[0]
    elif ' (' in video_name and ') [Jugger]' in video_name:
        tournament = video_name.split(' (')[1].split(') [Jugger]')[0]
    
    if tournament:
        tournament = clean_tournament_name(tournament)
    
    return team_one, team_two, tournament

def process_video_data(youtube_video):
    """Process a single YouTube video and extract relevant information"""
    video_id = youtube_video['snippet']['resourceId']['videoId']
    video_title = youtube_video['snippet']['title']
    video_name = clean_video_name(video_title)
    
    video_data = {
        "name": video_title,
        "category": "match",  # Default category for matches
        "videoLink": f"https://www.youtube.com/watch?v={video_id}",
        "uploadDate": youtube_video['snippet']['publishedAt'],
        "channelName": youtube_video['snippet']['customUrl'],
        "gameSystem": "sets",  # Default to sets system
    }
    
    team_one, team_two, tournament = extract_video_details(video_name)
    
    if team_one and team_two and tournament:
        video_data.update({
            "teamOneName": team_one,
            "teamTwoName": team_two,
            "tournamentName": tournament,
        })
        return video_data, True
    
    return video_data, False 