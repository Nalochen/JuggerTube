from DataDomain.Database.Repository import VideoRepository
from DataDomain.Model import Response


class GetVideoOverviewHandler:
    """Handler for getting video overview"""

    @staticmethod
    def handle() -> Response:

        videos = VideoRepository.getVideoOverview()

        return Response(
            response=videos,
            status=200,
        )
