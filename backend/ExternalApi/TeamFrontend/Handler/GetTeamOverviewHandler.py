from DataDomain.Database.Repository import TeamRepository
from DataDomain.Model import Response


class GetTeamOverviewHandler:
    """Handler for getting video overview"""

    @staticmethod
    def handle() -> Response:

        teams = TeamRepository.getTeamOverview()

        return Response(
            response=teams,
            status=200,
        )
