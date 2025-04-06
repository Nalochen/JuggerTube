from typing import List

from DataDomain.Database import db
from DataDomain.Database.Model.Videos import Videos

class VideoRepository:
    """Repository for video related queries"""

    @staticmethod
    def getVideoOverview() -> List[dict]:
        """Get Video Overview"""

        videos = db.session.query(
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
            Videos.guests
        ).filter(
            Videos.is_deleted is False
        ).group_by(
            Videos.id
        ).order_by(
            Videos.upload_date
        ).all()

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
            'guests': video.guests
        } for video in videos]
