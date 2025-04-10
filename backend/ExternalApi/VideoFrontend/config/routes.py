from flask import Blueprint, request

from config import cache
from DataDomain.Model import Response
from ExternalApi.VideoFrontend.Handler import (
    GetVideoOverviewHandler,
)
from ExternalApi.VideoFrontend.Handler.CreateVideoHandler import CreateVideoHandler
from ExternalApi.VideoFrontend.InputFilter.CreateVideoInputFilter import CreateVideoInputFilter

video_frontend = Blueprint('video-frontend', __name__)


@video_frontend.route('/get-video-overview',
                      methods=['GET'], endpoint='get-video-overview')
@cache.cached(key_prefix='video-overview')
def getVideoOverview() -> Response:
    return GetVideoOverviewHandler.handle()

@video_frontend.route('/create-video', methods=['POST'])
@CreateVideoInputFilter.validate()
def create_video() -> Response:
    """Create a new video"""
    return CreateVideoHandler().handle(request.validated_data)
