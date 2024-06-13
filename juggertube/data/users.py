from werkzeug.security import generate_password_hash

from juggertube.models import User, db, Team


def init_users(app):
    with app.app_context():
        new_users = [
            {"user": User(username='Patrick', email='testtest.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": 'Pink Pain'},
            {"user": User(username='{Peter}', email='testtest.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": 'Die Leere Menge'},
            {"user": User(username='Max CH', email='testtest.de',
                          password_hash=generate_password_hash('test', method='scrypt')),
             "team": 'Jugger Basilisken Basel'},
            {"user": User(username='Jonas', email='testtest.de',
                          password_hash=generate_password_hash('test', method='scrypt')),
             "team": 'Flying Juggmen Bonn'},
            {"user": User(username='David GAG', email='testtest.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": 'GAG'},
            {"user": User(username='David', email='testtest.de',
                          password_hash=generate_password_hash('test', method='scrypt'))},
            {"user": User(username='Lester', email='testtest.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": 'Rigor Mortis'},
            {"user": User(username='Kurt', email='testtest.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": 'Jugg - the Ripper'},
            {"user": User(username='Jules', email='testtest.de',
                          password_hash=generate_password_hash('test', method='scrypt')),
             "team": 'Schergen von Monasteria'},
            {"user": User(username='Linus', email='testtest.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": 'Falco Jugger'},
            {"user": User(username='Manuel', email='testtest.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": 'NLG'},
            {"user": User(username='Max V.', email='testtest.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": 'Peters Pawns'},
            {"user": User(username='Marc', email='testtest.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": 'Pompfritz'},
            {"user": User(username='Simba', email='testtest.de',
                          password_hash=generate_password_hash('test', method='scrypt')),
             "team": 'Leipziger Nachtwache'},
            {"user": User(username='Nadine', email='testtest.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": 'Sloth Machine'},
            {"user": User(username='Jens', email='testtest.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": 'Problemkinder'},
            {"user": User(username='Uhu/Ruben', email='testtest.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": 'JCE Schädeljäger'},
            {"user": User(username='Nikolay', email='testtest.de',
                          password_hash=generate_password_hash('test', method='scrypt')),
             "team": 'die verstörten Zernichter'},
            {"user": User(username='Joni', email='testtest.de',
                          password_hash=generate_password_hash('test', method='scrypt')), },
            {"user": User(username='Pete {}', email='testtest.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": 'Die Leere Menge'},
            {"user": User(username='Ludwig', email='testtest.de',
                          password_hash=generate_password_hash('test', method='scrypt')),
             "team": 'Leipziger Nachtwache'},
            {"user": User(username='Yps', email='testtest.de',
                          password_hash=generate_password_hash('test', method='scrypt')), },
            {"user": User(username='Luca', email='testtest.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": 'MécanHydre'},
            {"user": User(username='Finn Eh', email='testtest.de',
                          password_hash=generate_password_hash('test', method='scrypt')), },
            {"user": User(username='Manuel', email='testtest.de',
                          password_hash=generate_password_hash('test', method='scrypt')), },
            {"user": User(username='Robert', email='testtest.de',
                          password_hash=generate_password_hash('test')), "team": 'Karlshorster Kollektiv'},
        ]

        for new_user in new_users:
            db.session.add(new_user.user)
            db.session.flush()
            user = db.session.query(User).get(new_user.user.id)

            team_id = Team.query.filter_by(name=new_user.team).id
            team = db.session.query(Team).get(team_id)

            user.teams.append(team)
            team.members.append(user)

        db.session.commit()
