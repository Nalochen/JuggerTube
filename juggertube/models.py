from flask_login import UserMixin
from sqlalchemy import Text, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

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


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(200), nullable=False)
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
    user_id = db.Column(db.Integer, ForeignKey('users.user_id'), nullable=False)
    link = db.Column(db.String(50), nullable=False)
    tournament_id = db.Column(db.Integer, ForeignKey('tournaments.tournament_id'), nullable=False)
    team_one_id = db.Column(db.Integer, ForeignKey('teams.team_id', name='fk_videos_team_one'), nullable=False)
    team_two_id = db.Column(db.Integer, ForeignKey('teams.team_id', name='fk_videos_team_two'), nullable=False)
    upload_date = db.Column(db.Date, nullable=False)
    comments = db.Column(Text)


user_is_part_of_team = Table('user_is_part_of_team', db.Model.metadata,
                             db.Column('user_id', db.Integer, ForeignKey('users.user_id'), primary_key=True),
                             db.Column('team_id', db.Integer, ForeignKey('teams.team_id'), primary_key=True)
                             )
