from juggertube.data import channels, users
from juggertube.data.teams import teams
from juggertube.data.tournaments import tournaments
from juggertube.data.videos import videos
from juggertube.models import db


def init_db(app):
    with app.app_context():
        db.drop_all()
        db.create_all()

        teams.init_teams()
        tournaments.init_tournaments()
        users.init_users()
        channels.init_channels()
        videos.init_videos()

        db.session.commit()
