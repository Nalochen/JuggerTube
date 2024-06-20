import os

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_wtf import CSRFProtect

from juggertube.init_db import init_db
from juggertube.models import db, User

from juggertube.endpoints.channels.channel_blueprint import channel_blueprint
from juggertube.endpoints.general.general_blueprint import general_blueprint
from juggertube.endpoints.videos.video_blueprint import video_blueprint
from juggertube.endpoints.teams.team_blueprint import team_blueprint
from juggertube.templates.tournaments.tournament_blueprint import tournament_blueprint
from juggertube.endpoints.auth.auth_blueprint import auth_blueprint

user = 'macromedia'
password = 'macromedia'
host = 'localhost'
database = 'JuggerTube'


def create_app(db_uri=f'mysql+mysqlconnector://{user}:{password}@{host}/{database}'):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'kt4vq7bbofhbnp00jum6at717efdn9vajc6r35rvn5ime8tgwj'

    csrf = CSRFProtect(app)

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

    if __name__ == '__main__':
        base_dir = os.path.dirname(os.path.abspath(__file__))
        cert_path = os.path.join(base_dir, 'selfsigned.crt')
        key_path = os.path.join(base_dir, 'selfsigned.key')
        context = (cert_path, key_path)
        app.run(ssl_context=context, debug=True, host='0.0.0.0', port=5000)

    return app
