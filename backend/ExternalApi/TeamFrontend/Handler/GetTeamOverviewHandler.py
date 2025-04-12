from DataDomain.Model import Response
from DataDomain.Database.Repository.TeamRepository import TeamRepository


class GetTeamOverviewHandler:
    """Handler for getting video overview"""

    @staticmethod
    def handle() -> Response:

        teams = TeamRepository.getTeamOverview()

        return Response(
            response=teams,
            status=200,
        )
