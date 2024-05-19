from flask import Flask
from app.video_blueprint import video_blueprint
from app.models import db
from sqlalchemy import create_engine, text

app = Flask(__name__)

db_uri = 'mysql+mysqlconnector://macromedia:macromedia@localhost/JuggerTube'

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
engine = create_engine(db_uri)


def init_db():
    with app.app_context():
        db.create_all()


app.register_blueprint(video_blueprint)


if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
