import os

from config.app import app
from DataDomain.Database import initDatabase

if __name__ == '__main__':
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        initDatabase(app)

    app.run(debug=True, ssl_context="adhoc", host="0.0.0.0", port=8080)
