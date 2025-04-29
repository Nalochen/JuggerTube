from flask import g

from DataDomain.Database.Repository import ChannelRepository
from DataDomain.Database.Model import Channels
from DataDomain.Model import Response
from typing import List, Dict

class CreateMultipleChannelsHandler:
    """Handler for creating multiple channels"""

    @staticmethod
    def handle() -> Response:
        """Create multiple channels from an array of channel data"""
        data = g.validated_data
        channels_data = data.get('channels', [])

        if not channels_data:
            return Response(
                response='No channels provided',
                status=400
            )

        created_channels: List[Dict] = []
        failed_channels: List[Dict] = []

        for channel_data in channels_data:
            try:
                channel = Channels(
                    name=channel_data.get('name'),
                    channel_link=channel_data.get('channelLink'),
                )

                # Check if channel already exists
                if ChannelRepository.getChannelIdByName(channel.name):
                    failed_channels.append({
                        'name': channel.name,
                        'reason': 'Channel with this name already exists'
                    })
                    continue

                channel_id = ChannelRepository.create(channel)
                created_channels.append({
                    'name': channel.name,
                    'id': channel_id
                })
            except Exception as e:
                failed_channels.append({
                    'name': channel_data.get('name', 'Unknown'),
                    'reason': str(e)
                })

        response_data = {
            'created_channels': created_channels,
            'failed_channels': failed_channels
        }

        # If no channels were created successfully, return 400
        if not created_channels:
            return Response(
                response=response_data,
                status=400
            )

        # If some channels failed but others succeeded, return 207 (Multi-Status)
        if failed_channels:
            return Response(
                response=response_data,
                status=207
            )

        # If all channels were created successfully, return 200
        return Response(
            response=response_data,
            status=200
        )