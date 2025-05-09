import os
from datetime import timedelta

import pymysql
from flask_cors import CORS


class Config:
    """Configuration class for the Flask app"""

    @staticmethod
    def init_app(app) -> None:
        """Initializes the Flask app with the given configuration"""

        CORS(app, resources={
            r"/uploads/*": {"origins": [
                "http://localhost:4200",
                "http://localhost:80",
                "https://localhost:443"
            ]}
        })

        pymysql.install_as_MySQLdb()

        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

        app.config['CACHE_REDIS_HOST'] = os.getenv('CACHE_REDIS_HOST')
        app.config['CACHE_REDIS_PORT'] = os.getenv('CACHE_REDIS_PORT')
        app.config['CACHE_REDIS_DB'] = 0
        app.config['CACHE_DEFAULT_TIMEOUT'] = 300

        app.config['JWT_VERIFY_SUB'] = False
        app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=30)

        app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024  # 4MB

        app.config['DATABASE_PATH'] = '/app/DataDomain/Database'
        app.config['UPLOAD_FOLDER'] = '/app/DataDomain/assets'

        if os.getenv('FLASK_ENV') == 'production':
            app.config['CACHE_TYPE'] = 'redis'

        elif os.getenv('FLASK_ENV') == 'development':
            app.config['CACHE_TYPE'] = 'null'

            import warnings

            warnings.filterwarnings(
                "ignore",
                message="Flask-Caching: CACHE_TYPE is set to null, "
                        "caching is effectively disabled.")
