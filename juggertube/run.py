from datetime import timedelta

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate

from models import db, User
from sqlalchemy import create_engine

from general.general_blueprint import general_blueprint
from videos.video_blueprint import video_blueprint
from teams.team_blueprint import team_blueprint
from tournaments.tournament_blueprint import tournament_blueprint
from auth.auth_blueprint import auth_blueprint

app = Flask(__name__)

user = 'macromedia'
password = 'macromedia'
host = 'localhost'
database = 'JuggerTube'

db_uri = f'mysql+mysqlconnector://{user}:{password}@{host}/{database}'

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_COOKIE_NAME'] = 'jtrsession'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=24)
app.config['SECRET_KEY'] = 'kt4vq7bbofhbnp00jum6at717efdn9vajc6r35rvn5ime8tgwj'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

db.init_app(app)
migrate = Migrate(app, db)
engine = create_engine(db_uri)


def init_db():
    with app.app_context():
        db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


app.register_blueprint(video_blueprint, url_prefix="/videos")
app.register_blueprint(general_blueprint)
app.register_blueprint(team_blueprint, url_prefix="/teams")
app.register_blueprint(tournament_blueprint, url_prefix="/tournaments")
app.register_blueprint(auth_blueprint, url_prefix="/auth")


if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
