from flask import Blueprint
import logging

from config import cache
from DataDomain.Model import Response
from ExternalApi.VideoFrontend.Handler import (
    GetVideoOverviewHandler,
)

video_frontend = Blueprint('video-frontend', __name__)


@video_frontend.route('/get-video-overview',
                      methods=['GET'], endpoint='get-video-overview')
@cache.cached(key_prefix='video-overview')
def getVideoOverview() -> Response:
    return GetVideoOverviewHandler.handle()
