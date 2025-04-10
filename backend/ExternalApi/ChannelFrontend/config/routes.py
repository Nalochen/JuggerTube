from flask import Blueprint

from DataDomain.Model import Response
from ExternalApi.ChannelFrontend.Handler import CreateChannelHandler
from ExternalApi.ChannelFrontend.InputFilter import CreateChannelInputFilter

channel_frontend = Blueprint('channel-frontend', __name__)


@channel_frontend.route('/create-channel', methods=['POST'])
@CreateChannelInputFilter.validate()
def create_channel() -> Response:
    return CreateChannelHandler.handle()
