from flask import Blueprint
from config import cache

from DataDomain.Model import Response
from ExternalApi.ChannelFrontend.Handler.GetChannelOverviewHandler import GetChannelOverviewHandler


channel_frontend = Blueprint('channel-frontend', __name__)


@channel_frontend.route('/get-channel-overview',
                        methods=['GET'], endpoint='get-channel-overview')
@cache.cached(key_prefix='channel-overview')
def getChannelOverview() -> Response:
    return GetChannelOverviewHandler.handle()