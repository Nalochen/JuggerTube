from DataDomain.Model.Response import Response

from DataDomain.Database.Repository.VideoRepository import VideoRepository


class GetVideoOverviewHandler:
    """Handler for getting video overview"""

    @staticmethod
    def handle() -> Response:

        videos = VideoRepository.getVideoOverview()

        return Response(
            response=videos,
            status=200,
        )
