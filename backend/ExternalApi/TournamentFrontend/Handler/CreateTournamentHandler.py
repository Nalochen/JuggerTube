from datetime import datetime

from flask import g
from sqlalchemy.exc import SQLAlchemyError

from DataDomain.Database import db
from DataDomain.Database.Model import Tournaments
from DataDomain.Model import Response


class CreateTournamentHandler:
    """Handler for creating new tournaments"""

    @staticmethod
    def handle() -> Response:

        data = g.validated_data
        try:
            # Create new tournament using validated data
            tournament = Tournaments(
                name=data['name'],
                city=data['city'],
                start_date=datetime.fromisoformat(
                    data['startDate'].replace(
                        'Z',
                        '+00:00')),
                end_date=datetime.fromisoformat(
                    data['endDate'].replace(
                        'Z',
                        '+00:00')),
                address=data['address'],
                jtr_link=data.get(
                    'jtrLink',
                    ''))

            try:
                # Save to database
                db.session.add(tournament)
                db.session.commit()

                return Response(
                    response={
                        "id": tournament.id,
                        "message": "Tournament created successfully"
                    },
                    status=201
                )

            except SQLAlchemyError as db_error:
                # Rollback transaction on database error
                db.session.rollback()

                # Log the error for debugging
                print(f"Database error: {str(db_error)}")

                return Response(
                    response={
                        "message": "Failed to create tournament",
                        "error": str(db_error)
                    },
                    status=500
                )

        except Exception as e:
            # Log the error for debugging
            print(f"Unexpected error: {str(e)}")

            return Response(
                response={
                    "message": "Internal server error",
                    "error": str(e)
                },
                status=500
            )
