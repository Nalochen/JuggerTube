from flask import g

from DataDomain.Database.Model import Teams, Tournaments, Videos
from DataDomain.Database.Repository import (
    ChannelRepository,
    TeamRepository,
    TournamentRepository,
    VideoRepository,
)
from DataDomain.Model import Response


class CreateTournamentHandler:
    """Handler for creating a tournament"""

    @staticmethod
    def handle(tournamentData: Tournaments) -> Response:
        """Create Video"""
        data = g.validated_data | tournamentData

        tournament = Tournaments(
            name=data.get('name'),
            city=data.get('city'),
            start_date=data.get('startDate'),
            end_date=data.get('end_date'),
            jtr_link=data.get('jtrLink')
        )

        if TournamentRepository.getTournamentByName(tournament.name):
            return Response(
                response='Tournament with this name already exists',
                status=400
            )

        try:
            tournamentId = TournamentRepository.create(tournament)

        except Exception:
            return Response(status=500)

        return Response(
            response=tournamentId,
            status=200
        )
