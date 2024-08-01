from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate

from juggertube.init_db import init_db
from juggertube.models import db, User

from juggertube.frontend.channels.channel_blueprint import channel_blueprint
from juggertube.frontend.general.general_blueprint import general_blueprint
from juggertube.frontend.videos.video_blueprint import video_blueprint
from juggertube.frontend.teams.team_blueprint import team_blueprint
from juggertube.frontend.tournaments.tournament_blueprint import tournament_blueprint
from juggertube.frontend.auth.auth_blueprint import auth_blueprint
from juggertube.api.team_api_blueprint import team_api_blueprint
from juggertube.api.video_api_blueprint import video_api_blueprint
from juggertube.api.channel_api_blueprint import channel_api_blueprint
from juggertube.api.tournament_api_blueprint import tournament_api_blueprint

user = 'juggertube'
password = '6dr497820t~s,.-zunDTHEVRTrwjiocüt'
host = 'localhost'
database = 'JuggerTube'


def create_app(db_uri=f'mysql+mysqlconnector://{user}:{password}@{host}/{database}'):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'kt4vq7bbofhbnp00jum6at717efdn9vajc6r35rvn5ime8tgwj'
    app.config['SPEC_FORMAT'] = 'yaml'

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    migrate = Migrate(app, db)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        init_db(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(video_blueprint, url_prefix="/videos")
    app.register_blueprint(general_blueprint)
    app.register_blueprint(team_blueprint, url_prefix="/teams")
    app.register_blueprint(tournament_blueprint, url_prefix="/tournaments")
    app.register_blueprint(channel_blueprint, url_prefix="/channels")
    app.register_blueprint(auth_blueprint, url_prefix="/auth")
    app.register_blueprint(team_api_blueprint, url_prefix="/api/teams")
    app.register_blueprint(tournament_api_blueprint, url_prefix="/api/tournaments")
    app.register_blueprint(channel_api_blueprint, url_prefix="/api/channels")
    app.register_blueprint(video_api_blueprint, url_prefix="/api/videos")

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)

    return app
