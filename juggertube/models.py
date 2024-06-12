from flask_login import UserMixin
from sqlalchemy import Text, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash

from juggertube.game_system_enum import GameSystem
from juggertube.video_type_enum import VideoType


db = SQLAlchemy()
Base = declarative_base()


user_is_part_of_team = Table('user_is_part_of_team', db.Model.metadata,
                             db.Column('user_id', db.Integer, ForeignKey('users.user_id'), primary_key=True),
                             db.Column('team_id', db.Integer, ForeignKey('teams.team_id'), primary_key=True))

user_owns_channel = Table('user_owns_channel', db.Model.metadata,
                             db.Column('user_id', db.Integer, ForeignKey('users.user_id'), primary_key=True),
                             db.Column('channel_id', db.Integer, ForeignKey('channel.channel_id'), primary_key=True))


class Tournament(db.Model):
    __tablename__ = 'tournaments'

    tournament_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    jtr_link = db.Column(db.String(100))
    tugeny_link = db.Column(db.String(100))


class Team(db.Model):
    __tablename__ = 'teams'

    team_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(50))
    city = db.Column(db.String(50))
    members = db.relationship('Members', secondary=user_is_part_of_team, backref='users')


class Channel(db.Model):
    __tablename__ = 'channels'

    channel_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(50), nullable=False)
    owners = db.relationship('Owners', secondary=user_owns_channel, backref='users')


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(200), nullable=False)
    teams = db.relationship('Teams', secondary=user_is_part_of_team, backref='teams')
    channels = db.relationship('Channels', secondary=user_owns_channel, backref='channels')
    authenticated = db.Column(db.Boolean, default=False)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        return True

    def get_id(self):
        return str(self.user_id)

    def is_anonymous(self):
        return False


class Video(db.Model):
    __tablename__ = 'videos'

    video_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    channel_id = db.Column(db.Integer, ForeignKey('channel.channel_id'), nullable=False)
    category = db.Column(db.Enum(VideoType), nullable=False)
    link = db.Column(db.String(50), nullable=False)
    upload_date = db.Column(db.Date, nullable=False)
    date_of_recording = db.Column(db.Date)
    tournament_id = db.Column(db.Integer, ForeignKey('tournaments.tournament_id'))
    team_one_id = db.Column(db.Integer, ForeignKey('teams.team_id', name='fk_videos_team_one'))
    team_two_id = db.Column(db.Integer, ForeignKey('teams.team_id', name='fk_videos_team_two'))
    game_system = db.Column(db.Enum(GameSystem))
    weapon_type = db.Column(db.String(100))
    topic = db.Column(db.String(100))
    guests = db.Column(db.String(100))
    comments = db.Column(Text)
