from flask import Blueprint

from config import cache
from DataDomain.Model import Response
from ExternalApi.VideoFrontend.Handler import CreateVideoHandler, GetVideoOverviewHandler, CreateMultipleVideosHandler
from ExternalApi.VideoFrontend.InputFilter.CreateVideoInputFilter import CreateVideoInputFilter
from ExternalApi.VideoFrontend.InputFilter.CreateMultipleVideosInputFilter import CreateMultipleVideosInputFilter

video_frontend = Blueprint('video-frontend', __name__)


@video_frontend.route('/get-video-overview',
                      methods=['GET'], endpoint='get-video-overview')
@cache.cached(key_prefix='video-overview')
def getVideoOverview() -> Response:
    return GetVideoOverviewHandler.handle()


@video_frontend.route('/create-video',
                      methods=['POST'], endpoint='create-video')
@CreateVideoInputFilter.validate()
@cache.cached(key_prefix='create-video')
def createVideo() -> Response:
    return CreateVideoHandler.handle()


@video_frontend.route('/create-multiple-videos',
                      methods=['POST'], endpoint='create-multiple-videos')
@CreateMultipleVideosInputFilter.validate()
@cache.cached(key_prefix='create-multiple-videos')
def createMultipleVideos() -> Response:
    return CreateMultipleVideosHandler.handle()