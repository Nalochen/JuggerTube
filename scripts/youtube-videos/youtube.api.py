from googleapiclient.discovery import build
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Disable SSL verification warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Change URL depending on the environment
create_videos_url = 'https://localhost:8080/api/video-frontend/create-multiple-videos'

def main(channel_id):
    api_key = 'AIzaSyCd4irgsASp6cb393tAgYBTXacjGq2YG3E'
    youtube = build(
        'youtube',
        'v3',
        developerKey=api_key
    )

    # Make a request to youtube api
    request = youtube.channels().list(
        part='contentDetails',
        id=channel_id
    )

    # get a response for api
    response = request.execute()

    # Retrieve the uploads playlist ID for the given channel
    playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    # Retrieve all videos from uploads playlist
    youtube_videos = []
    next_page_token = None

    while True:
        playlist_items_response = youtube.playlistItems().list(
            # part='contentDetails',
            part='snippet',
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        youtube_videos += playlist_items_response['items']

        next_page_token = playlist_items_response.get('nextPageToken')

        if not next_page_token:
            break

    # Extract video URLs and prepare data for API
    videos_data = []
    videos_other_naming = []

    for youtube_video in youtube_videos:
        video_id = youtube_video['snippet']['resourceId']['videoId']

        video_title = youtube_video['snippet']['title']
        video_name = video_title
        video_channel = youtube_video['snippet']['channelTitle']
        video_system = 'sets'  # Default to sets system
        video_link = f"https://www.youtube.com/watch?v={video_id}"
        video_upload_date = youtube_video['snippet']['publishedAt']
        video_team_one = None
        video_team_two = None
        video_tournament = None

        if video_name.find('Kleines Finale ') > -1:
            video_name = video_name.replace('Kleines Finale ', '')
        if video_name.find('Finale ') > -1:
            video_name = video_name.replace('Finale ', '')
        if video_name.find('Halbfinale ') > -1:
            video_name = video_name.replace('Halbfinale ', '')
        if video_name.find('Viertelfinale ') > -1:
            video_name = video_name.replace('Viertelfinale ', '')
        if video_name.find('Gruppenphase ') > -1:
            video_name = video_name.replace('Gruppenphase ', '')
        if video_name.find('MULTICAM! ') > -1:
            video_name = video_name.replace('MULTICAM! ', '')
        if video_name.find('MULTICAM ') > -1:
            video_name = video_name.replace('MULTICAM ', '')
        if video_name.find('HALBFINALE ') > -1:
            video_name = video_name.replace('HALBFINALE ', '')
        if video_name.find('VIERTELFINALE ') > -1:
            video_name = video_name.replace('VIERTELFINALE  ', '')
        if video_name.find('GRAND FINAL WCC 2023  ') > -1:
            video_name = video_name.replace('GRAND FINAL WCC 2023  ', '')
        if video_name.find('FINALE ') > -1:
            video_name = video_name.replace('FINALE ', '')
        if video_name.find(' gegen ') > -1:
            video_team_one = video_name.split(' gegen ')[0]
        if video_name.find(' vs ') > -1:
            video_team_one = video_name.split(' vs ')[0]
        if video_name.find(' gegen ') > -1 and video_name.find(' | ') > -1:
            video_team_two = video_name.split(' gegen ')[1].split(' | ')[0]
        if video_name.find(' vs ') > -1 and video_name.find(' | ') > -1:
            video_team_two = video_name.split(' vs ')[1].split(' | ')[0]
        if video_name.find(' vs ') > -1 and video_name.find(' (') > -1:
            video_team_two = video_name.split(' vs ')[1].split(' (')[0]
        if video_name.find(' | ') > -1 and video_name.find(' [Jugger]') > -1:
            video_tournament = video_name.split(' | ')[1].split(' [Jugger]')[0]
        if video_name.find(' (') > -1 and video_name.find(') [Jugger]') > -1:
            video_tournament = video_name.split(' (')[1].split(') [Jugger]')[0]

        if video_team_two and video_team_one and video_tournament:
            video_data = {
                "name": video_title,
                "category": "match",  # Default category for matches
                "videoLink": video_link,
                "uploadDate": video_upload_date,
                "channelName": video_channel,
                "gameSystem": video_system,
                "teamOneName": video_team_one,
                "teamTwoName": video_team_two,
                "tournamentName": video_tournament,
            }
            videos_data.append(video_data)
        else:
            videos_other_naming.append({video_name, video_link})

    # Send request to create videos API
    if videos_data:
        payload = {"videos": videos_data}
        try:
            # Print the payload for debugging
            print("Sending payload:")
            print(payload)
            
            # Add headers and ensure SSL verification is disabled for local development
            headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Host': 'localhost:8080'
            }
            response = requests.post(
                create_videos_url, 
                json=payload,
                headers=headers,
                verify=False  # Disable SSL verification for local development only
            )
            print(f"API Response Status: {response.status_code}")
            if response.status_code != 200:
                print(f"Error: Server returned status code {response.status_code}")
            if response.text:  # Only try to print JSON if there's content
                try:
                    print(f"Response content: {response.json()}")
                except ValueError:
                    print(f"Raw response: {response.text}")
        except requests.exceptions.ConnectionError as e:
            print(f"Connection Error: Could not connect to the server. Is it running? Error: {str(e)}")
        except Exception as e:
            print(f"Error sending data to API: {str(e)}")

    # Write unmatched videos to file
    out_file = open(f"{channel_id}OtherNaming.txt", "w", encoding="utf-8")
    for video in videos_other_naming:
        line = (f'{video}' + "\n")
        out_file.write(line)


if __name__ == "__main__":
    channel_ids = [
        'UCIp0Z0R5BNYoRTFG-1s5Y9g',
        'UC1EXd2J8aqwiKC64yvIMKGQ',
        'UCvdd5RoFdmzJhBTeesXZ6og'
    ]

    for channel in channel_ids:
        main(channel)
