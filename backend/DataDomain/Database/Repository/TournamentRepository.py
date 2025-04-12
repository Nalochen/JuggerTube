from DataDomain.Database.db import db
from DataDomain.Database.Model.Tournaments import Tournaments
from Infrastructure.Logger.Logger import logger


class TournamentRepository:
    """Repository for tournament related queries"""

    @staticmethod
    def create(tournament: Tournaments) -> int:
        try:
            db.session.add(tournament)
            db.session.commit()

            logger.info(
                f'TournamentRepository | Create | created tournament {tournament.id}')

            return tournament.id

        except Exception as e:
            db.session.rollback()
            logger.error(f'TournamentRepository | Create | {e}')
            raise e