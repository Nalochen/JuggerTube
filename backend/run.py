from DataDomain.Database import db
from config.app import app

if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(debug=True, ssl_context="adhoc", host="0.0.0.0", port=8080)
