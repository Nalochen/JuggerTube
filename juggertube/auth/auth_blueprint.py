from flask import Blueprint, request, url_for, redirect, render_template, jsonify, flash

from models import db, User
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_required, logout_user, login_user

auth_blueprint = Blueprint('auth', __name__, template_folder='templates')


def serialize_user(user):
    return {
        'user_id': user.user_id,
        'username': user.username,
        'email': user.email,
        'password': user.password,
    }


@auth_blueprint.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [serialize_user(user) for user in users]
    return jsonify(user_list)


@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email'])
        if user:
            return redirect(url_for('auth.login'))

        hashed_pw = generate_password_hash(request.form['password'], method='scrypt')
        new_user = User(email=request.form['email'], username=request.form['username'], password=hashed_pw)
        login_user(new_user)
        db.session.add(new_user)
        db.session.commit()

    return render_template('register.html')


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user:
            if check_password_hash(user.password_hash, password):
                login_user(user)
                return '<h1>succeeded</h1>'
            else:
                return '<h1>login failed</h1>'

        return '<h1>No User with this name found</h1>'
    return render_template('login.html')


@auth_blueprint.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return '<h1>User logged out!</h1>'


@auth_blueprint.route('/delete/<int:user_id>', methods=['GET'])
def delete_user(user_id):
    user = User.query.filter_by(user_id=user_id).first()

    name = user.username

    db.session.delete(user)
    db.session.commit()
    return f'<h1>Team {name} deleted<h1>'
