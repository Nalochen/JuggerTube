from flask import flash

from juggertube.data import (users, channels, teams, tournaments, videos_part_one, videos_part_two, videos_part_three,
                             videos_part_four)
from juggertube.models import db


def init_db(app):
    with app.app_context():
        db.create_all()

        #teams.init_teams(app)
        #tournaments.init_tournaments(app)
        #users.init_users(app)
        #channels.init_channels(app)
        #videos_part_one.init_videos(app)
        #videos_part_two.init_videos(app)
        #videos_part_three.init_videos(app)
        #videos_part_four.init_videos(app)

        db.session.commit()
