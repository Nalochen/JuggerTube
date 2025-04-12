from DataDomain.Database.db import db
from DataDomain.Database.Model import Teams
from Infrastructure.Logger.Logger import logger
from typing import List


class TeamRepository:
    """Repository for team related queries"""

    @staticmethod
    def getAllTeams() -> List[dict]:
        """Get all teams from database"""
        teams = (db.session.query(
            Teams.id,
            Teams.name,
            Teams.country,
            Teams.city,
            Teams.comment
        ).filter(
            Teams.is_deleted != True
        ).order_by(
            Teams.name
        ).all())

        result = []
        for team in teams:
            team_dict = {
                'id': team.id,
                'name': team.name,
                'country': team.country,
                'city': team.city,
                'comment': team.comment
            }
            result.append(team_dict)

        return result

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