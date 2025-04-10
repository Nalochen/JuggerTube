import os

from flask import Flask
from flask_compress import Compress
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_talisman import Talisman
from redis import Redis

from config import Config, cache, limiter
from DataDomain.Database import db
from ExternalApi.VideoFrontend.config.routes import video_frontend
from ExternalApi.TournamentFrontend.config.routes import tournament_frontend
from ExternalApi.TeamFrontend.config.routes import team_frontend
from ExternalApi.ChannelFrontend.config.routes import channel_frontend

def createApp() -> Flask:
    """Creates the Flask app"""

    app = Flask(__name__)
    Config.init_app(app)

    app.register_blueprint(video_frontend,
                           url_prefix='/api/video-frontend')
    app.register_blueprint(tournament_frontend,
                         url_prefix='/api/tournament-frontend')
    app.register_blueprint(team_frontend,
                          url_prefix='/api/team-frontend')
    app.register_blueprint(channel_frontend,
                          url_prefix='/api/channel-frontend')
    # app.register_blueprint(system, url_prefix='/api/system')

    cache.init_app(app)

    db.init_app(app)

    Migrate(
        app,
        db,
        directory=os.path.join(
            app.config['DATABASE_PATH'],
            'Migration'))

    Talisman(app, 
             force_https=False,  # Disable HTTPS forcing in development
             content_security_policy={
        'default-src': ["'self'"],
        'script-src': ["'self'", "'unsafe-inline'"],
        'style-src': ["'self'", "'unsafe-inline'"],
        'img-src': ["'self'"],
    })

    Compress(app)

    return app


app = createApp()

jwt = JWTManager(app)

redis = Redis(
    host=app.config['CACHE_REDIS_HOST'],
    port=app.config['CACHE_REDIS_PORT'],
    db=app.config['CACHE_REDIS_DB'])

limiter.init_app(app)
