from flask_login import UserMixin
from sqlalchemy import Text
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash

from juggertube.enums.game_system_enum import GameSystem
from juggertube.video_type_enum import VideoType

db = SQLAlchemy()
Base = declarative_base()

user_team = db.Table('user_team',
                     db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
                     db.Column('team_id', db.Integer, db.ForeignKey('teams.id'), primary_key=True)
                     )

user_channel = db.Table('user_channel',
                        db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
                        db.Column('channel_id', db.Integer, db.ForeignKey('channels.id'), primary_key=True)
                        )


class Video(db.Model):
    __tablename__ = 'videos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    channel_id = db.Column(db.Integer, db.ForeignKey('channels.id'), nullable=False)
    category = db.Column(db.Enum(VideoType), nullable=False)
    link = db.Column(db.String(150), nullable=False)
    upload_date = db.Column(db.Date, nullable=False)
    comments = db.Column(Text)

    tournament_id = db.Column(db.Integer, db.ForeignKey('tournaments.id'))
    team_one_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    team_one = db.relationship('Team',
                               foreign_keys=[team_one_id],
                               backref='video_team_one'
                               )
    team_two_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    team_two = db.relationship('Team',
                               foreign_keys=[team_two_id],
                               backref='video_team_two'
                               )
    date_of_recording = db.Column(db.Date)
    game_system = db.Column(db.Enum(GameSystem))

    weapon_type = db.Column(db.String(100))
    topic = db.Column(db.String(100))
    guests = db.Column(db.String(100))


class Tournament(db.Model):
    __tablename__ = 'tournaments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    jtr_link = db.Column(db.String(100))
    tugeny_link = db.Column(db.String(100))
    videos = db.relationship(
        'Video',
        backref='tournament'
    )


class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(50))
    city = db.Column(db.String(50))


class Channel(db.Model):
    __tablename__ = 'channels'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(100), nullable=False)
    videos = db.relationship(
        Video,
        backref='channel'
    )


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(200), nullable=False)
    teams = db.relationship(
        'Team',
        secondary=user_team,
        backref=db.backref('members', lazy='dynamic')
    )
    channels = db.relationship(
        'Channel',
        secondary=user_channel,
        backref=db.backref('owners', lazy='dynamic')
    )
    authenticated = db.Column(db.Boolean, default=False)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        return True

    def get_id(self):
        return str(self.id)

    def is_anonymous(self):
        return False
