from typing import Dict

from sqlalchemy.exc import SQLAlchemyError

from DataDomain.Database import db
from DataDomain.Database.Model import Teams
from DataDomain.Model import Response
from ExternalApi.TeamFrontend.Validator.CreateTeamValidator import CreateTeamValidator


class CreateTeamHandler:
    """Handler for creating new teams"""

    def handle(self, data: Dict) -> Response:
        """
        Handle team creation request
        
        Args:
            data (Dict): Validated team data from request
            
        Returns:
            Response: API response
        """
        try:
            # Create new team using validated data
            team = Teams(
                name=data['name'],
                country=data['country'],
                city=data['city'],
            )

            try:
                # Save to database
                db.session.add(team)
                db.session.commit()

                return Response(
                    response={
                        "id": team.id,
                        "message": "Team successfully created"
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
                        "message": "Failed to create team",
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