from flask import g
from typing import List, Dict, Optional

from DataDomain.Database.Repository import ChannelRepository
from DataDomain.Database.Model import Channels
from DataDomain.Database.Enum import ChannelLinkTypesEnum
from DataDomain.Model import Response

class CreateMultipleChannelsHandler:
    """Handler for creating multiple channels"""

    @staticmethod
    def _generate_channel_link(identifier: str, link_type: ChannelLinkTypesEnum) -> str:
        """Generate the appropriate channel link based on the link type"""
        if link_type == ChannelLinkTypesEnum.YOUTUBE_CUSTOM:
            # Ensure the handle starts with @
            handle = identifier if identifier.startswith('@') else f'@{identifier}'
            return f'https://youtu.be/c/{handle}'
        # For other types, use the identifier as is since it should be a full URL
        return identifier

    @staticmethod
    def _generate_channel_name(identifier: str, provided_name: Optional[str], link_type: ChannelLinkTypesEnum) -> str:
        """Generate a channel name if not provided"""
        if provided_name:
            return provided_name
        
        # For YouTube custom URLs, use the handle as name if no name provided
        if link_type == ChannelLinkTypesEnum.YOUTUBE_CUSTOM:
            # Remove @ if present and capitalize first letter
            name = identifier.lstrip('@')
            return name[0].upper() + name[1:] if name else identifier
        
        return identifier

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
                identifier = channel_data.get('channelIdentifier')
                link_type = ChannelLinkTypesEnum[channel_data.get('linkType')]
                provided_name = channel_data.get('name')

                if not identifier:
                    raise ValueError('Channel identifier is required')

                channel_link = CreateMultipleChannelsHandler._generate_channel_link(identifier, link_type)
                channel_name = CreateMultipleChannelsHandler._generate_channel_name(identifier, provided_name, link_type)

                channel = Channels(
                    name=channel_name,
                    channel_link=channel_link,
                    link_type=link_type
                )

                # Check if channel already exists
                if ChannelRepository.getChannelIdByName(channel.name):
                    failed_channels.append({
                        'identifier': identifier,
                        'reason': f'Channel with name {channel.name} already exists'
                    })
                    continue

                channel_id = ChannelRepository.create(channel)
                created_channels.append({
                    'name': channel.name,
                    'id': channel_id,
                    'channelLink': channel.channel_link
                })
            except Exception as e:
                failed_channels.append({
                    'identifier': channel_data.get('channelIdentifier', 'Unknown'),
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