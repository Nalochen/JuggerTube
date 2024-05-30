from flask import Blueprint, request, url_for, redirect, render_template, jsonify, session

from models import db, User

auth_blueprint = Blueprint('auth', __name__, template_folder='templates')


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

        for user in users:
            if user.password == password:
                session['username'] = username
                return '<h1>succeeded</h1>'
            else:
                return '<h1>login failed</h1>'

        return '<h1>No User with this name found</h1>'
    return render_template('login.html')


@auth_blueprint.route('/logout', methods=['GET'])
def logout_user():
    session.pop('username', default=None)
    return '<h1>User logged out!</h1>'


def is_user_logged_in():
    username = session.get('username')
    if username is not None:
        return True
    return False
