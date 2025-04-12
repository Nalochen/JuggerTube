from flask import Blueprint

from DataDomain.Model import Response
from ExternalApi.TeamFrontend.Handler.GetTeamOverviewHandler import GetTeamOverviewHandler

team_frontend = Blueprint('team-frontend', __name__)


@team_frontend.route('/get-team-overview',
                      methods=['GET'], endpoint='get-team-overview')
def getTeamOverview() -> Response:
    return GetTeamOverviewHandler.handle()