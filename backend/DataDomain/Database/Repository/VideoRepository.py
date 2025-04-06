from typing import List

from DataDomain.Database import db
from DataDomain.Database.Model.Videos import Videos

from DataDomain.Database.Model.Channels import Channels
from DataDomain.Database.Model.Tournaments import Tournaments

from DataDomain.Database.Model.Teams import Teams


class VideoRepository:
    """Repository for video related queries"""

    @staticmethod
    def getVideoOverview() -> List[dict]:
        """Get Video Overview"""

        videos = (db.session.query(
            Videos.id,
            Videos.name,
            Videos.category,
            Videos.video_link,
            Videos.upload_date,
            Videos.comment,
            Videos.date_of_recording,
            Videos.game_system,
            Videos.weapon_type,
            Videos.topic,
            Videos.guests,
            Channels.name.label('channel_name'),
            Tournaments.name.label('tournament_name'),
            Teams.name.label('team_name')
        ).join(
            Channels,
            Videos.channel_id == Channels.id
        ).join(
            Tournaments,
            Videos.tournament_id == Tournaments.id
        ).join(
            Teams,
            Videos.team_one_id == Teams.id
        ).join (
            Teams,
            Videos.team_two_id == Teams.id
        ).filter(
            Videos.is_deleted is False
        ).group_by(
            Videos.id
        ).order_by(
            Videos.upload_date
        ).all())

        return [{
            'id': video.id,
            'name': video.name,
            'category': video.category,
            'videoLink': video.video_link,
            'uploadDate': video.upload_date.isoformat(),
            'comment': video.comment,
            'dateOfRecording': video.date_of_recording.isoformat(),
            'gameSystem': video.game_system,
            'weaponType': video.weapon_type,
            'topic': video.topic,
            'guests': video.guests,
            'channelName': video.channel_name,
            'tournamentName': video.tournament_name,
            'teamName': video.team_name,
        } for video in videos]
