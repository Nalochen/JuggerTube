from juggertube.models import db


def init_db(app):
    with app.app_context():
        db.drop_all()
        db.create_all()

        db.session.commit()