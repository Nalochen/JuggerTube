from flask import Blueprint
from config import cache
from DataDomain.Model import Response

from ExternalApi.TournamentFrontend.Handler.GetTournamentOverviewHandler import GetTournamentOverviewHandler

tournament_frontend = Blueprint('tournament-frontend', __name__)


@tournament_frontend.route('/get-tournament-overview',
                      methods=['GET'], endpoint='get-tournament-overview')
@cache.cached(key_prefix='tournament-overview')
def getTournamentOverview() -> Response:
    return GetTournamentOverviewHandler.handle()