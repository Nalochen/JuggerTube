from typing import List

from DataDomain.Database import db
from DataDomain.Database.Model import Channels


class ChannelRepository:
    """Repository for channel related queries"""

    @staticmethod
    def getChannelOverview() -> List[dict]:
        """Get Channel Overview"""

        channels = (db.session.query(
            Channels.id,
            Channels.name,
            Channels.channel_link
        ).filter(
            Channels.is_deleted != True
        ).order_by(
            Channels.name.asc()
        ).all())

        result = []
        for channel in channels:
            channel_dict = {
                'id': channel.id,
                'name': channel.name,
                'channelLink': channel.channel_link,
            }
            result.append(channel_dict)

        return result

    @staticmethod
    def getChannelById(channelId: int) -> dict | None:
        """Get Channel by id"""

        channel = db.session.query(
            Channels.id,
            Channels.name,
            Channels.channel_link
        ).filter(
            Channels.id == channelId
        ).group_by(
            Channels.id
        ).first()

        if not channel:
            return None

        return {
            'id': channel.id,
            'name': channel.name,
            'channelLink': channel.channel_link
        }

    @staticmethod
    def getChannelIdByLink(channelLink: str) -> int | None:
        """Get Channel by id"""

        channel = db.session.query(
            Channels.id,
            Channels.channel_link
        ).filter(
            Channels.id == channelLink
        ).group_by(
            Channels.id
        ).first()

        if not channel:
            return None

        return channel.id
