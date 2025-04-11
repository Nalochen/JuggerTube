from DataDomain.Database.db import db
from DataDomain.Database.Model import Teams
from Infrastructure.Logger.Logger import logger


class TeamRepository:
    """Repository for team related queries"""

    @staticmethod
    def create(team: Teams) -> int:
        try:
            db.session.add(team)
            db.session.commit()

            logger.info(
                f'TeamRepository | Create | created team {team.id}')

            return team.id

        except Exception as e:
            db.session.rollback()
            logger.error(f'TeamRepository | Create | {e}')
            raise e