from flask import Blueprint, request, url_for, redirect, render_template, jsonify, flash

from juggertube.models import db, User
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_required, logout_user, login_user

from juggertube.webforms import RegisterForm, LoginForm

auth_blueprint = Blueprint('auth', __name__, template_folder='templates')


def serialize_user(user):
    return {
        'user_id': user.user_id,
        'username': user.username,
        'email': user.email,
        'password_hash': user.password_hash,
    }


@auth_blueprint.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [serialize_user(user) for user in users]
    return jsonify(user_list)


@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            return redirect(url_for('auth.login'))

        try:
            hashed_pw = generate_password_hash(form.password.data, method='scrypt')
            new_user = User(email=form.email.data, username=form.username.data, password_hash=hashed_pw)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            flash('Account successfully created', 'info')
        except Exception as e:
            flash(str(e), 'danger')

    return render_template('register.html', form=form)


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash('login successful', 'info')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('general.index'))
        else:
            flash('login failed please check username and password', 'info')

    return render_template('login.html', form=form)


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
    return f'<h1>User {name} deleted<h1>'
