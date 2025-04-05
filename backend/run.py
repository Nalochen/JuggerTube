from DataDomain.Database import db, initDatabase
from config.app import app

if __name__ == '__main__':

    with app.app_context():
        db.create_all()
    print("database created")

    initDatabase(app)

    app.run(debug=True, ssl_context="adhoc", host="0.0.0.0", port=8080)
