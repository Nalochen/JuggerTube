from werkzeug.security import generate_password_hash

from juggertube.models import User, db, Team


def init_users(app):
    with app.app_context():
        new_users = [
            {"user": User(username='Patrick', email='testtest1.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": 'Pink Pain'},
            {"user": User(username='{Peter}', email='testtest2.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": 'Die Leere Menge'},
            {"user": User(username='Max CH', email='testtest3.de',
                          password_hash=generate_password_hash('test', method='scrypt')),
             "team": 'Jugger Basilisken Basel'},
            {"user": User(username='Jonas', email='testtest4.de',
                          password_hash=generate_password_hash('test', method='scrypt')),
             "team": 'Flying Juggmen Bonn'},
            {"user": User(username='David GAG', email='testtest5.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": 'GAG'},
            {"user": User(username='David', email='testtest6.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": ''},
            {"user": User(username='Lester', email='testtest7.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": 'Rigor Mortis'},
            {"user": User(username='Kurt', email='testtest8.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": 'Jugg - the Ripper'},
            {"user": User(username='Jules', email='testtest9.de',
                          password_hash=generate_password_hash('test', method='scrypt')),
             "team": 'Schergen von Monasteria'},
            {"user": User(username='Linus', email='testtest10.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": 'Falco Jugger'},
            {"user": User(username='Manuel', email='testtest11.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": 'NLG'},
            {"user": User(username='Max V.', email='testtest12.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": 'Peters Pawns'},
            {"user": User(username='Marc', email='testtest13.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": 'Pompfritz'},
            {"user": User(username='Simba', email='testtest14.de',
                          password_hash=generate_password_hash('test', method='scrypt')),
             "team": 'Leipziger Nachtwache'},
            {"user": User(username='Nadine', email='testtest15.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": 'Sloth Machine'},
            {"user": User(username='Jens', email='testtest16.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": 'Problemkinder'},
            {"user": User(username='Nikolay', email='testtest18.de',
                          password_hash=generate_password_hash('test', method='scrypt')),
             "team": 'die verstörten Zernichter'},
            {"user": User(username='Joni', email='testtest19.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": ''},
            {"user": User(username='Pete {}', email='testtest20.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": 'Die Leere Menge'},
            {"user": User(username='Ludwig', email='testtest21.de',
                          password_hash=generate_password_hash('test', method='scrypt')),
             "team": 'Leipziger Nachtwache'},
            {"user": User(username='Yps', email='testtest22.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": ''},
            {"user": User(username='Luca', email='testtest23.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": 'MécanHydre'},
            {"user": User(username='Finn Eh', email='testtest24.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": ''},
            {"user": User(username='Manuel', email='testtest25.de',
                          password_hash=generate_password_hash('test', method='scrypt')), "team": ''},
            {"user": User(username='Robert', email='testtest26.de',
                          password_hash=generate_password_hash('test')), "team": 'Karlshorster Kollektiv'},
            {"user": User(username='Nalo', email='testtest27.de',
                          password_hash=generate_password_hash('test', method='scrypt')),
             "team": 'Cranium Ex Machina'},
        ]

        for new_user in new_users:
            existing_user = User.query.filter_by(username=new_user["user"].username).first()

            if not existing_user:
                db.session.add(new_user["user"])
                db.session.flush()
                user = db.session.query(User).filter_by(id=new_user["user"].id).first()

                if not new_user["team"] == '':
                    team = Team.query.filter_by(name=new_user["team"]).first()

                    user.teams.append(team)

        db.session.commit()
