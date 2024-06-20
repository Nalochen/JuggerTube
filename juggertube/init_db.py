from flask import flash

from juggertube.data import (users, channels, teams, tournaments, init_videos)
from juggertube.models import db


def init_db(app):
    with app.app_context():
        db.create_all()

        #teams.init_teams(app)
        #tournaments.init_tournaments(app)
        #users.init_users(app)
        #channels.init_channels(app)
        #init_videos.init_videos(app)

        db.session.commit()
