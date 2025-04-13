from DataDomain.Database.Repository.TournamentRepository import TournamentRepository
from DataDomain.Model import Response


class GetTournamentOverviewHandler:
    """Handler for getting tournament overview"""

    @staticmethod
    def handle() -> Response:

        tournaments = TournamentRepository.getTournamentOverview()

        return Response(
            response=tournaments,
            status=200,
        )