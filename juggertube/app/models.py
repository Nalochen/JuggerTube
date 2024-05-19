from sqlalchemy import Text, Enum, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
Base = declarative_base()


class Tournament(db.Model):
    __tablename__ = 'tournaments'

    tournament_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    date_beginning = db.Column(db.Date, nullable=False)
    date_ending = db.Column(db.Date, nullable=False)
    city = db.Column(db.String(50), nullable=False)
    jtr_link = db.Column(db.String(100), nullable=False)


class Team(db.Model):
    __tablename__ = 'teams'

    team_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)


class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(Text, nullable=False)


class Channel(db.Model):
    __tablename__ = 'channels'

    channel_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(75), nullable=False)
    link = db.Column(db.String(50), nullable=False)


class Video(db.Model):
    __tablename__ = 'videos'

    video_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    channel_id = db.Column(db.Integer, ForeignKey('channels.channel_id'), nullable=False)
    link = db.Column(db.String(50), nullable=False)
    tournament_id = db.Column(db.Integer, ForeignKey('tournaments.tournament_id'), nullable=False)
    team_one_id = db.Column(db.Integer, ForeignKey('teams.team_id', name='fk_videos_team_one'), nullable=False)
    team_two_id = db.Column(db.Integer, ForeignKey('teams.team_id', name='fk_videos_team_two'), nullable=False)
    upload_date = db.Column(db.Date, nullable=False)
    comments = db.Column(Text)
    type = db.Column(Enum('reports', 'highlights', 'tutorials', 'building', 'matches', 'music', 'podcast', 'other'),
                     nullable=False)


user_has_channel = Table('user_has_channel', db.Model.metadata,
                         db.Column('user_id', db.Integer, ForeignKey('users.user_id'), primary_key=True),
                         db.Column('channel_id', db.Integer, ForeignKey('channels.channel_id'), primary_key=True)
                         )

user_is_part_of_team = Table('user_is_part_of_team', db.Model.metadata,
                             db.Column('user_id', db.Integer, ForeignKey('users.user_id'), primary_key=True),
                             db.Column('team_id', db.Integer, ForeignKey('teams.team_id'), primary_key=True)
                             )
