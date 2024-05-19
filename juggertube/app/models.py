from sqlalchemy import create_engine, Column, Integer, String, Date, Text, Enum, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Tournament(Base):
    __tablename__ = 'tournaments'

    tournament_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    date_beginning = Column(Date, nullable=False)
    date_ending = Column(Date, nullable=False)
    city = Column(String(50), nullable=False)
    jtr_link = Column(String(100), nullable=False)

class Team(Base):
    __tablename__ = 'teams'

    team_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    country = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(Text, nullable=False)

class Channel(Base):
    __tablename__ = 'channels'

    channel_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(75), nullable=False)
    link = Column(String(50), nullable=False)

class Video(Base):
    __tablename__ = 'videos'

    video_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    channel_id = Column(Integer, ForeignKey('channels.channel_id'), nullable=False)
    link = Column(String(50), nullable=False)
    tournament_id = Column(Integer, ForeignKey('tournaments.tournament_id'), nullable=False)
    team_one_id = Column(Integer, ForeignKey('teams.team_id'), nullable=False)
    team_two_id = Column(Integer, ForeignKey('teams.team_id'), nullable=False)
    upload_date = Column(Date, nullable=False)
    comments = Column(Text)
    type = Column(Enum('reports', 'highlights', 'tutorials', 'building', 'matches', 'music', 'podcast', 'other'), nullable=False)

user_has_channel = Table('user_has_channel', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.user_id'), primary_key=True),
    Column('channel_id', Integer, ForeignKey('channels.channel_id'), primary_key=True)
)

user_is_part_of_team = Table('user_is_part_of_team', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.user_id'), primary_key=True),
    Column('team_id', Integer, ForeignKey('teams.team_id'), primary_key=True)
)

# Database setup
engine = create_engine('sqlite:///example.db')  # Replace with your actual database URL
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
