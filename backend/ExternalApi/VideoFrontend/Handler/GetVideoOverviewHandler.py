from DataDomain.Database.Repository.VideoRepository import VideoRepository
from DataDomain.Model.Response import Response


class GetVideoOverviewHandler:
    """Handler for getting video overview"""

    @staticmethod
    def handle() -> Response:

        videos = VideoRepository.getVideoOverview()

        return Response(
            response=videos,
            status=200,
        )
