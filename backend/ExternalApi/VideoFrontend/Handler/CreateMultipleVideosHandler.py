from datetime import datetime
from typing import Dict, List

from flask import g

from DataDomain.Database.Enum import GameSystemTypesEnum, VideoCategoriesEnum
from DataDomain.Database.Model import Channels, Videos
from DataDomain.Database.Repository import (
    ChannelRepository,
    TeamRepository,
    TournamentRepository,
    VideoRepository,
)
from DataDomain.Model import Response


class CreateMultipleVideosHandler:
    """Handler for creating multiple videos"""

    @staticmethod
    def handle() -> Response:
        """Create Video"""
        data = g.validated_data
        videos_data = data.get('videos', [])

        if not videos_data:
            return Response(
                response='No videos provided',
                status=400
            )

        created_videos: List[Dict] = []
        failed_videos: List[Dict] = []

        for video_data in videos_data:
            video_name = video_data.get('name')

            if VideoRepository.getVideoByName(video_name):
                failed_videos.append({
                    'name': video_name,
                    'reason': 'Video with this name already exists'
                })
                continue

            video = Videos()
            channel_name = video_data.get('channelName')

            if not channel_name:
                failed_videos.append({
                    'name': video_name,
                    'reason': 'Channel name is required'
                })
                continue

            channel_id = ChannelRepository.getChannelIdByName(channelName=channel_name)

            # If channel doesn't exist, create it
            if not channel_id:
                try:
                    # Generate YouTube channel link - handle spaces and special characters
                    safe_channel_name = channel_name.replace(' ', '').replace('@', '')
                    channel = Channels(
                        name=channel_name,
                        channel_link=f'https://www.youtube.com/@{safe_channel_name}'
                    )
                    channel_id = ChannelRepository.create(channel)
                except Exception as e:
                    failed_videos.append({
                        'name': video_name,
                        'reason': f'Failed to create channel: {str(e)}'
                    })
                    continue

            # Set required fields
            video.name = video_data.get('name')
            video.category = VideoCategoriesEnum.MATCH
            video.video_link = video_data.get('videoLink')
            video.channel_id = channel_id
            video.topic = ''
            video.guests = ''

            video.game_system = GameSystemTypesEnum.SETS

            tournament_name = video_data.get('tournamentName')
            tournament_id = TournamentRepository.getTournamentByName(tournament_name)
            if not tournament_id:
                failed_videos.append({
                    'name': video.name,
                    'reason': f'Tournament not found: {tournament_name}'
                })
                continue

            video.tournament_id = tournament_id

            team_one_name = video_data.get('teamOneName')
            team_two_name = video_data.get('teamTwoName')

            team_one_id = TeamRepository.getTeamIdByName(team_one_name)
            team_two_id = TeamRepository.getTeamIdByName(team_two_name)

            if not team_one_id or not team_two_id:
                failed_videos.append({
                    'name': video.name,
                    'reason': f'Teams not found: {team_one_name} or {team_two_name}'
                })
                continue

            video.team_one_id = team_one_id
            video.team_two_id = team_two_id

            # Set optional fields
            video.comment = video_data.get('comment', '')
            video.upload_date = datetime.fromisoformat(video_data.get('uploadDate'))

            if (video.game_system
                        and not video.tournament_id
                        and not video.team_one_id
                        and not video.team_two_id
                    ):
                failed_videos.append({
                    'name': video.name,
                    'reason': 'Missing required data'
                })
                continue

            try:
                video_id = VideoRepository.create(video)
                created_videos.append({
                    'name': video.name,
                    'id': video_id
                })
            except Exception as e:
                failed_videos.append({
                    'name': video.name,
                    'reason': str(e)
                })

        response_data = {
            'created_videos': created_videos,
            'failed_videos': failed_videos
        }

        # If no videos were created successfully, return 400
        if not created_videos:
            return Response(
                response=response_data,
                status=400
            )

        # If some videos failed but others succeeded, return 207 (Multi-Status)
        if failed_videos:
            return Response(
                response=response_data,
                status=207
            )

        # If all videos were created successfully, return 200
        return Response(
            response=response_data,
            status=200
        )
