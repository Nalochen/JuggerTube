from flask import Blueprint, request

from DataDomain.Model import Response
from ExternalApi.TournamentFrontend.Handler.CreateTournamentHandler import CreateTournamentHandler
from ExternalApi.TournamentFrontend.InputFilter.CreateTournamentInputFilter import CreateTournamentInputFilter

tournament_frontend = Blueprint('tournament-frontend', __name__)

@tournament_frontend.route('/create-tournament', methods=['POST'])
@CreateTournamentInputFilter.validate()
def create_tournament() -> Response:
    """Create a new tournament"""
    return CreateTournamentHandler().handle(request.validated_data) 