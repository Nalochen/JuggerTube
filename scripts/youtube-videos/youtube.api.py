from googleapiclient.discovery import build

from ExternalApi.VideoFrontend.Handler import CreateVideoHandler
from video import Video


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

    # Extract video URLs
    videos = []
    videos_other_naming = []

    for youtube_video in youtube_videos:
        video_id = youtube_video['snippet']['resourceId']['videoId']

        video_title = youtube_video['snippet']['title']
        video_name = video_title
        video_category = 'MATCH'
        video_channel = youtube_video['snippet']['channelTitle']
        video_system = 'SETS'
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
            video = Video(
                name=video_title,
                category=video_category,
                channel=video_channel,
                game_system=video_system,
                link=video_link,
                upload_date=video_upload_date,
                team_one=video_team_one,
                team_two=video_team_two,
                tournament=video_tournament
            )
            videos.append(video)
        else:
            videos_other_naming.append({video_name, video_link})

    for video in videos:
        CreateVideoHandler.handle(video)

    # open file
    out_file = open(f"{channel_id}OtherNaming.txt", "w", encoding="utf-8")
    # Print the extracted video URLs
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
