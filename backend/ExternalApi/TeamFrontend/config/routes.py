from flask import Blueprint

from DataDomain.Model import Response
from ExternalApi.TeamFrontend.Handler import CreateTeamHandler
from ExternalApi.TeamFrontend.InputFilter import CreateTeamInputFilter

team_frontend = Blueprint('team-frontend', __name__)


@team_frontend.route('/create-team', methods=['POST'])
@CreateTeamInputFilter.validate()
def create_team() -> Response:
    return CreateTeamHandler.handle()
