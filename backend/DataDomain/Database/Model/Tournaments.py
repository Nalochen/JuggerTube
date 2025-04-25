from datetime import datetime
from typing import List

from sqlalchemy import func
from sqlalchemy.orm import Mapped

from DataDomain.Database import db
from DataDomain.Database.Model import BaseModel


class Tournaments(BaseModel):
    __tablename__ = 'tournaments'

    id: int = db.Column(
        db.Integer,
        primary_key=True,
        unique = True,
    )

    name: str = db.Column(
        db.String(100),
        nullable=False,
        unique = True,
    )

    city: str = db.Column(
        db.String(50),
        nullable=False
    )

    start_date: datetime = db.Column(
        db.DateTime,
        nullable=False,
    )

    end_date: datetime = db.Column(
        db.DateTime,
        nullable=False,
    )

    jtr_link: str = db.Column(
        db.String(255),
        nullable=False,
        unique = True,
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

    videos: Mapped[List['Videos']] = db.relationship(
        'Videos',
        back_populates='tournament'
    )
