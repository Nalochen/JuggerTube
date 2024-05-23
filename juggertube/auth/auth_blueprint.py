from flask import Blueprint, request, url_for, redirect, render_template, jsonify

from models import db, User

auth_blueprint = Blueprint('auth', __name__, template_folder='templates')


def serialize_user(user):
    return {
        'user': user.user_id,
        'email': user.email,
        'username': user.username,
        'password': user.password,
    }


@auth_blueprint.route('/', methods=['GET'])
def get_user():
    users = User.query.all()
    user_list = [serialize_user(user) for user in users]
    return jsonify(user_list)


@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        new_user = User(email=email, username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('general.index'))
    return render_template('register.html')


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = User.query.filter_by(username=username).all()

        # wenn users leer -> kein User mit Namen gefunden

        for user in users:
            if user.password == password:
                print('user is logged in')
            else:
                print('login failed')

        return redirect(url_for('general.index'))
    return render_template('login.html')
