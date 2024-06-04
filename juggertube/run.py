import os

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate

from juggertube.models import db, User
from sqlalchemy import create_engine

from juggertube.general.general_blueprint import general_blueprint
from juggertube.videos.video_blueprint import video_blueprint
from juggertube.teams.team_blueprint import team_blueprint
from juggertube.tournaments.tournament_blueprint import tournament_blueprint
from juggertube.auth.auth_blueprint import auth_blueprint

app = Flask(__name__)

user = 'macromedia'
password = 'macromedia'
host = 'localhost'
database = 'JuggerTube'

db_uri = f'mysql+mysqlconnector://{user}:{password}@{host}/{database}'

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'kt4vq7bbofhbnp00jum6at717efdn9vajc6r35rvn5ime8tgwj'

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

db.init_app(app)
migrate = Migrate(app, db)
migrate.init_app(app, db)
engine = create_engine(db_uri)


def init_db():
    with app.app_context():
        db.create_all()


@login_manager.user_loader
def load_user(user_id):
    print(user_id)
    return User.query.get(int(user_id))


app.register_blueprint(video_blueprint, url_prefix="/videos")
app.register_blueprint(general_blueprint)
app.register_blueprint(team_blueprint, url_prefix="/teams")
app.register_blueprint(tournament_blueprint, url_prefix="/tournaments")
app.register_blueprint(auth_blueprint, url_prefix="/auth")


if __name__ == '__main__':
    init_db()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    cert_path = os.path.join(base_dir, 'selfsigned.crt')
    key_path = os.path.join(base_dir, 'selfsigned.key')
    context = (cert_path, key_path)
    app.run(ssl_context='context', debug=True, host='0.0.0.0', port=5000)
