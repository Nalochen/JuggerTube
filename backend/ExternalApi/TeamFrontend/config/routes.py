from flask import Blueprint, request

from DataDomain.Model import Response
from ExternalApi.TeamFrontend.Handler.CreateTeamHandler import CreateTeamHandler
from ExternalApi.TeamFrontend.InputFilter.CreateTeamInputFilter import CreateTeamInputFilter

team_frontend = Blueprint('team-frontend', __name__)

@team_frontend.route('/create-team', methods=['POST'])
@CreateTeamInputFilter.validate()
def create_team() -> Response:
    """Create a new team"""
    return CreateTeamHandler().handle(request.validated_data) 