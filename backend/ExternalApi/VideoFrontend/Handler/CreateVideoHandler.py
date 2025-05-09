from datetime import datetime

from flask import g

from DataDomain.Database.Enum import VideoCategoriesEnum
from DataDomain.Database.Model import Teams, Tournaments, Videos
from DataDomain.Database.Repository import (
    ChannelRepository,
    TeamRepository,
    TournamentRepository,
    VideoRepository,
)
from DataDomain.Model import Response


class CreateVideoHandler:
    """Handler for creating a video"""

    @staticmethod
    def handle() -> Response:
        """Create Video"""
        data = g.validated_data

        video = CreateVideoHandler._create_base_video(data)

        if VideoRepository.getVideoByName(video.name):
            return Response(
                response='Video with this name already exists',
                status=400
            )

        CreateVideoHandler._handle_category_specific_data(video, data)

        if ((video.category == VideoCategoriesEnum.REPORTS
             and not video.topic)
                or (video.category == VideoCategoriesEnum.SPARBUILDING
                    and not video.weapon_type)
                or (video.category == VideoCategoriesEnum.MATCH
                    and not video.game_system
                    and not video.tournament_id
                    and not video.team_one_id
                    and not video.team_two_id
                    )
            ):
            return Response(response='missing required data', status=400)

        try:
            videoId = VideoRepository.create(video)

        except Exception:
            return Response(status=500)

        return Response(
            response=videoId,
            status=200
        )

    @staticmethod
    def _process_video_link(video_link: str) -> tuple[str, str]:
        """Process video link and return tuple of (processed_link, link_type)"""
        if video_link.startswith("https://youtu.be/"):
            return video_link.replace("https://youtu.be/", ""), "youtube"
        return video_link, "other"

    @staticmethod
    def _create_base_video(data: dict) -> Videos:
        """Create a video with base properties"""
        video = Videos()
        channelLink = data.get('channelLink')
        channelId = ChannelRepository.getChannelIdByLink(channelLink=channelLink)

        # Set required fields
        video.name = data.get('name')
        video.category = data.get('category')
        
        # Process video link
        video_link, link_type = CreateVideoHandler._process_video_link(data.get('videoLink'))
        video.video_link = video_link
        video.link_type = link_type
        
        video.channel_id = channelId

        # Set optional fields
        video.comment = data.get('comment')
        video.upload_date = datetime.fromisoformat(data.get('uploadDate'))

        return video

    @staticmethod
    def _handle_category_specific_data(video: Videos, data: dict):
        """Handle category specific data for the video"""
        category = data.get('category')

        if category == VideoCategoriesEnum.SPARBUILDING:
            video.weapon_type = data.get('weaponType')
            video.topic = data.get('topic') | ''
            video.guests = data.get('guests') | ''

        elif category == VideoCategoriesEnum.HIGHLIGHTS:
            video.tournament_id = CreateVideoHandler._handle_tournament_data(
                data.get('tournament'))
            video.topic = data.get('topic')
            video.guests = data.get('guests')

        elif category in [VideoCategoriesEnum.OTHER, VideoCategoriesEnum.PODCAST]:
            video.topic = data.get('topic')
            video.guests = data.get('guests')

        elif category == VideoCategoriesEnum.TRAINING:
            video.weapon_type = data.get('weaponType')
            video.topic = data.get('topic')

        elif category == VideoCategoriesEnum.REPORTS:
            video.topic = data.get('topic')

        elif category == VideoCategoriesEnum.AWARDS:
            video.tournament_id = CreateVideoHandler._handle_tournament_data(
                data.get('tournament'))

        elif category == VideoCategoriesEnum.MATCH:
            video.game_system = data.get('gameSystem')
            video.tournament_id = CreateVideoHandler._handle_tournament_data(
                data.get('tournament'))
            video.team_one_id = CreateVideoHandler._handle_team_data(data.get('teamOne'))
            video.team_two_id = CreateVideoHandler._handle_team_data(data.get('teamTwo'))

    @staticmethod
    def _handle_tournament_data(tournament_data: dict) -> int | None:
        """Handle tournament data and return tournament ID"""
        if not tournament_data:
            return None

        if 'id' in tournament_data:
            return tournament_data.get('id')

        tournament = Tournaments()

        if TournamentRepository.getTournamentByName(tournament_data.get('name')):
            return None

        tournament.name = tournament_data.get('name')
        tournament.city = tournament_data.get('city')
        tournament.start_date = tournament_data.get('startDate')
        tournament.end_date = tournament_data.get('endDate')
        return TournamentRepository.create(tournament)

    @staticmethod
    def _handle_team_data(team_data: dict) -> int | None:
        """Handle team data and return team ID"""

        if 'id' in team_data:
            return team_data.get('id')

        team = Teams()
        if not TeamRepository.getTeamIdByName(team_data.get('name')):
            return None

        team.name = team_data.get('name')
        team.city = team_data.get('city')
        return TeamRepository.create(team)
