from flask import Blueprint

from DataDomain.Model import Response
from ExternalApi.ChannelFrontend.Handler.GetChannelOverviewHandler import GetChannelOverviewHandler


channel_frontend = Blueprint('channel-frontend', __name__)


@channel_frontend.route('/get-channel-overview',
                        methods=['GET'], endpoint='get-channel-overview')
def getChannelOverview() -> Response:
    return GetChannelOverviewHandler.handle()