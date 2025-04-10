from flask import Blueprint

from DataDomain.Model import Response
from ExternalApi.TournamentFrontend.Handler import CreateTournamentHandler
from ExternalApi.TournamentFrontend.InputFilter import CreateTournamentInputFilter

tournament_frontend = Blueprint('tournament-frontend', __name__)


@tournament_frontend.route('/create-tournament', methods=['POST'])
@CreateTournamentInputFilter.validate()
def create_tournament() -> Response:
    return CreateTournamentHandler.handle()
