from DataDomain.Database.Repository import ChannelRepository
from DataDomain.Model import Response


class GetChannelOverviewHandler:
    """Handler for getting Channel Overview"""

    @staticmethod
    def handle() -> Response:

        channels = ChannelRepository.getChannelOverview()

        return Response(
            response=channels,
            status=200,
        )
