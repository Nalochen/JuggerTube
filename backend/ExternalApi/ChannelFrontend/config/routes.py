from flask import Blueprint

from config import cache
from DataDomain.Model import Response
from ExternalApi.ChannelFrontend.Handler import GetChannelOverviewHandler
from ExternalApi.ChannelFrontend.Handler.CreateMultipleChannelsHandler import CreateMultipleChannelsHandler
from ExternalApi.ChannelFrontend.InputFilter.CreateMultipleChannelsInputFilter import CreateMultipleChannelsInputFilter

channel_frontend = Blueprint('channel-frontend', __name__)


@channel_frontend.route('/get-channel-overview',
                        methods=['GET'], endpoint='get-channel-overview')
@cache.cached(key_prefix='channel-overview')
def getChannelOverview() -> Response:
    return GetChannelOverviewHandler.handle()

@channel_frontend.route('/create-multiple-channels',
                           methods=['POST'], endpoint='create-multiple-channels')
@CreateMultipleChannelsInputFilter.validate()
def createMultipleChannels() -> Response:
    return CreateMultipleChannelsHandler.handle()