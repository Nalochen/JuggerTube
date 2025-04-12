from DataDomain.Model import Response
from DataDomain.Database.Repository.ChannelRepository import ChannelRepository


class GetChannelOverviewHandler:
    """Handler for getting Channel Overview"""

    @staticmethod
    def handle() -> Response:

        channels = ChannelRepository.getChannelOverview()

        return Response(
            response=channels,
            status=200,
        )