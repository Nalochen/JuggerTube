from flask import g
from sqlalchemy.exc import SQLAlchemyError

from DataDomain.Database import db
from DataDomain.Database.Model import Channels
from DataDomain.Model import Response


class CreateChannelHandler:
    """Handler for creating new channels"""

    @staticmethod
    def handle() -> Response:
        data = g.validated_data

        try:
            # Create new channel using validated data
            channel = Channels(
                name=data['name'],
                channel_link=data['channel_link']
            )

            try:
                # Save to database
                db.session.add(channel)
                db.session.commit()

                return Response(
                    response={
                        "id": channel.id,
                        "message": "Channel successfully created"
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
                        "message": "Failed to create channel",
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
