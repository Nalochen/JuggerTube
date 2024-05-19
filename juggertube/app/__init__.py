from flask import Flask
from juggertube.app import video_blueprint

def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(video_blueprint)

    return app
