from flask import Blueprint, request

from DataDomain.Model import Response
from ExternalApi.ChannelFrontend.Handler.CreateChannelHandler import CreateChannelHandler
from ExternalApi.ChannelFrontend.InputFilter.CreateChannelInputFilter import CreateChannelInputFilter

channel_frontend = Blueprint('channel-frontend', __name__)

@channel_frontend.route('/create-channel', methods=['POST'])
@CreateChannelInputFilter.validate()
def create_channel() -> Response:
    """Create a new channel"""
    return CreateChannelHandler().handle(request.validated_data) 