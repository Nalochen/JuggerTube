from datetime import datetime

from flask import g
from sqlalchemy.exc import SQLAlchemyError

from DataDomain.Database import db
from DataDomain.Database.Enum.GameSystemTypesEnum import GameSystemTypesEnum
from DataDomain.Database.Enum.VideoCategoriesEnum import VideoCategoriesEnum
from DataDomain.Database.Enum.WeaponTypesEnum import WeaponTypesEnum
from DataDomain.Database.Model.Videos import Videos
from DataDomain.Model import Response


class CreateVideoHandler:
    """Handler for creating new videos"""

    @staticmethod
    def handle() -> Response:

        data = g.validated_data

        try:
            # Create new video using validated data
            video = Videos(
                name=data['name'],
                channel_id=data['channel_id'],
                category=VideoCategoriesEnum(data['category']),
                video_link=data['video_link'],
                upload_date=datetime.fromisoformat(data['upload_date'].replace('Z', '+00:00')),
                topic=data['topic'],
                guests=data['guests'],
                comment=data.get('comment', ''),
                tournament_id=data.get('tournament_id'),
                team_one_id=data.get('team_one_id'),
                team_two_id=data.get('team_two_id'),
                date_of_recording=(
                    datetime.fromisoformat(data['date_of_recording'].replace('Z', '+00:00'))
                    if data.get('date_of_recording')
                    else None
                ),
                game_system=(
                    GameSystemTypesEnum(data['game_system'])
                    if data.get('game_system')
                    else None
                ),
                weapon_type=(
                    WeaponTypesEnum(data['weapon_type'])
                    if data.get('weapon_type')
                    else None
                )
            )

            try:
                # Save to database
                db.session.add(video)
                db.session.commit()

                return Response(
                    response={
                        "id": video.id,
                        "message": "Video created successfully"
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
                        "message": "Failed to create video",
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
