from typing import List

from DataDomain.Database import db
from DataDomain.Database.Model import Tournaments
from Infrastructure.Logger import logger


class TournamentRepository:
    """Repository for tournament related queries"""

    @staticmethod
    def getTournamentOverview() -> List[dict]:
        """get all Tournaments queries"""
        tournaments = (db.session.query(
            Tournaments.id,
            Tournaments.name,
            Tournaments.city,
            Tournaments.start_date,
            Tournaments.end_date,
            Tournaments.jtr_link
        ).filter(
            Tournaments.is_deleted != True
        ).order_by(
            Tournaments.name
        ).all())

        result = []
        for tournament in tournaments:
            tournament_dict = {
                'id': tournament.id,
                'name': tournament.name,
                'city': tournament.city,
                'start_date': tournament.start_date,
                'end_date': tournament.end_date,
                'jtr_link': tournament.jtr_link
            }
            result.append(tournament_dict)

        return result

    @staticmethod
    def getTournamentByName(tournamentName: str) -> int | None:
        """get Tournament ID by Name"""
        tournament = (db.session.query(
            Tournaments.id
        ).filter(
            Tournaments.is_deleted != True,
            Tournaments.name == tournamentName
        ).scalar())

        return tournament


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
