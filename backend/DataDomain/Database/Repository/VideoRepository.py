from typing import List

from sqlalchemy.orm import aliased

from DataDomain.Database import db
from DataDomain.Database.Model import Channels, Teams, Tournaments, Videos


class VideoRepository:
    """Repository for video related queries"""

    @staticmethod
    def getVideoOverview() -> List[dict]:
        """Get Video Overview"""

        TeamOne = aliased(Teams)
        TeamTwo = aliased(Teams)

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
            TeamOne.name.label('team_one_name'),
            TeamTwo.name.label('team_two_name')
        ).join(
            Channels,
            Videos.channel_id == Channels.id
        ).join(
            Tournaments,
            Videos.tournament_id == Tournaments.id
        ).join(
            TeamOne,
            Videos.team_one_id == TeamOne.id
        ).join(
            TeamTwo,
            Videos.team_two_id == TeamTwo.id
        ).filter(
            Videos.is_deleted == False
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
            'teamOneName': video.team_one_name,
            'teamTwoName': video.team_two_name,
        } for video in videos]
