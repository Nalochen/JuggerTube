from flask import Blueprint

from config import cache
from DataDomain.Model import Response
from ExternalApi.TeamFrontend.Handler import GetTeamOverviewHandler
from ExternalApi.TeamFrontend.Handler.CreateMultipleTeamsHandler import (
    CreateMultipleTeamsHandler,
)
from ExternalApi.TeamFrontend.InputFilter.CreateMultipleTeamsInputFilter import (
    CreateMultipleTeamsInputFilter
)

team_frontend = Blueprint('team-frontend', __name__)


@team_frontend.route('/get-team-overview',
                     methods=['GET'], endpoint='get-team-overview')
@cache.cached(key_prefix='team-overview')
def getTeamOverview() -> Response:
    return GetTeamOverviewHandler.handle()

@team_frontend.route('/create-multiple-teams',
                           methods=['POST'], endpoint='create-multiple-teams')
@CreateMultipleTeamsInputFilter.validate()
def createMultipleTeams() -> Response:
    return CreateMultipleTeamsHandler.handle()
