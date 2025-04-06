from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped

from DataDomain.Database import db
from DataDomain.Database.Enum.GameSystemTypesEnum import GameSystemTypesEnum
from DataDomain.Database.Enum.VideoCategoriesEnum import VideoCategoriesEnum
from DataDomain.Database.Enum.WeaponTypesEnum import WeaponTypesEnum
from DataDomain.Database.Model import BaseModel, Channels, Teams


class Videos(BaseModel, db.Model):
    __tablename__ = 'videos'

    id: int = db.Column(
        db.Integer,
        primary_key=True
    )

    name: str = db.Column(
        db.String(100),
        nullable=False
    )

    category: VideoCategoriesEnum = db.Column(
        db.Enum(VideoCategoriesEnum),
        nullable=False,
        default=VideoCategoriesEnum.OTHER
    )

    video_link: str = db.Column(
        db.String(255),
        nullable=False
    )

    upload_date: datetime = db.Column(
        db.DateTime,
        nullable=False,
    )

    comments: str = db.Column(
        db.Text,
        nullable=False,
        default=''
    )

    date_of_recording: datetime = db.Column(
        db.DateTime,
        nullable=True,
    )

    game_system: GameSystemTypesEnum = db.Column(
        db.Enum(GameSystemTypesEnum),
        nullable=True,
    )

    weapon_type: WeaponTypesEnum = db.Column(
        db.Enum(WeaponTypesEnum),
        nullable=True,
    )

    topic: str = db.Column(
        db.String(100),
        nullable=False
    )

    guests: str = db.Column(
        db.String(100),
        nullable=False
    )

    channel: Mapped['Channels'] = db.relationship(
        'Channels',
        back_populates='videos'
    )

    tournament: Mapped['Tournaments'] = db.relationship(
        'Tournaments',
        back_populates='videos'
    )

    team_one_id: int = db.Column(
        db.Integer,
        db.ForeignKey('teams.id'),
        nullable=True)

    team_two_id: int = db.Column(
        db.Integer,
        db.ForeignKey('teams.id'),
        nullable=True
    )

    team_one: Mapped[Teams] = db.relationship(
        'Teams',
        foreign_keys=[team_one_id]
    )

    team_two: Mapped[Teams] = db.relationship(
        'Teams',
        foreign_keys=[team_two_id]
    )

    is_deleted: bool = db.Column(
        db.Boolean,
        nullable=False,
        server_default='0'
    )

    created_at: datetime = db.Column(
        db.DateTime,
        server_default=func.now()
    )

    updated_at: datetime = db.Column(
        db.DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )
