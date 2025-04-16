from datetime import datetime
from typing import List

from sqlalchemy.orm import aliased

from DataDomain.Database import db
from DataDomain.Database.Model import Channels, Teams, Tournaments, Videos
from Infrastructure.Logger import logger


def parse_date(date_str) -> str:
    """Parse date string and return formatted date"""
    if not date_str:
        return None
    try:
        # Try different date formats
        for fmt in ['%Y-%m-%d', '%Y-%m-%d %H:%M:%S', '%Y-%m-%dT%H:%M:%S']:
            try:
                return datetime.strptime(str(date_str)[:19], fmt).strftime('%d-%m-%Y')
            except ValueError:
                continue
        return str(date_str)
    except Exception:
        return str(date_str)


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
        ).outerjoin(
            Tournaments,
            Videos.tournament_id == Tournaments.id
        ).outerjoin(
            TeamOne,
            Videos.team_one_id == TeamOne.id
        ).outerjoin(
            TeamTwo,
            Videos.team_two_id == TeamTwo.id
        ).filter(
            Videos.is_deleted != True
        ).order_by(
            Videos.upload_date
        ).all())

        result = []
        for video in videos:
            video_dict = {
                'id': video.id,
                'name': video.name,
                'category': video.category.value if video.category else None,
                'videoLink': video.video_link,
                'comment': video.comment,
                'gameSystem': video.game_system.value if video.game_system else None,
                'weaponType': video.weapon_type.value if video.weapon_type else None,
                'topic': video.topic,
                'guests': video.guests,
                'uploadDate': parse_date(video.upload_date),
                'dateOfRecording': parse_date(video.date_of_recording),
                'channelName': video.channel_name,
                'tournamentName': video.tournament_name,
                'teamOneName': video.team_one_name,
                'teamTwoName': video.team_two_name,
            }
            result.append(video_dict)

        return result

    @staticmethod
    def getVideoByName(videoName: str) -> dict | None:
        """get Video by Name"""

        TeamOne = aliased(Teams)
        TeamTwo = aliased(Teams)

        video = (db.session.query(
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
        ).outerjoin(
            Tournaments,
            Videos.tournament_id == Tournaments.id
        ).outerjoin(
            TeamOne,
            Videos.team_one_id == TeamOne.id
        ).outerjoin(
            TeamTwo,
            Videos.team_two_id == TeamTwo.id
        ).filter(
            Videos.is_deleted != True,
            Videos.name == videoName
        ).order_by(
            Videos.upload_date
        ).first())

        return video

    @staticmethod
    def create(video: Videos) -> int:
        try:
            db.session.add(video)
            db.session.commit()

            logger.info(
                f'VideoRepository | Create | created video {
                    video.id}')

            return video.id

        except Exception as e:
            db.session.rollback()
            logger.error(f'VideoRepository | Create | {e}')
            raise e
