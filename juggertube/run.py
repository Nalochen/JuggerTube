from flask import Flask
from models import db
from sqlalchemy import create_engine

from general.general_blueprint import general_blueprint
from videos.video_blueprint import video_blueprint
from channels.channel_blueprint import channel_blueprint
from teams.team_blueprint import team_blueprint
from tournaments.tournament_blueprint import tournament_blueprint

app = Flask(__name__)

db_uri = 'mysql+mysqlconnector://macromedia:macromedia@localhost/JuggerTube'

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
engine = create_engine(db_uri)


def init_db():
    with app.app_context():
        db.create_all()


app.register_blueprint(video_blueprint, url_prefix="/videos")
app.register_blueprint(channel_blueprint, url_prefix="/channels")
app.register_blueprint(general_blueprint)
app.register_blueprint(team_blueprint, url_prefix="/teams")
app.register_blueprint(tournament_blueprint, url_prefix="/tournaments")


if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
