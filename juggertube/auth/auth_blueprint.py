from flask import Blueprint, request, url_for, redirect, render_template, jsonify, flash
from sqlalchemy.sql.functions import current_user

from juggertube.models import db, User, Team
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_required, logout_user, login_user

from juggertube.webforms import RegisterForm, LoginForm

auth_blueprint = Blueprint('auth', __name__, template_folder='templates')


def serialize_user(user):
    teams = [team.name for team in user.teams]
    return {
        'user_id': user.id,
        'username': user.username,
        'email': user.email,
        'password_hash': user.password_hash,
        'teams': teams
    }


@auth_blueprint.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [serialize_user(user) for user in users]
    return jsonify(user_list)


@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            return redirect(url_for('auth.login'))

        email = form.email.data
        username = form.username.data
        password_hash = generate_password_hash(form.password.data, method='scrypt')
        team = form.team.data

        try:
            new_user = User(email=email, username=username, password_hash=password_hash)
            db.session.add(new_user)
            new_user.teams.append(Team.query.filter_by(id=form.team.data).first())

            db.session.commit()
            login_user(new_user)
            flash('Account successfully created', 'info')
        except Exception as e:
            flash(str(e), 'danger')
    form.team.choices = [(team.id, team.name) for team in Team.query.all()]
    return render_template('register.html', form=form)


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
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


@auth_blueprint.route('/edit/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    form = RegisterForm()
    if request.method == 'POST':
        user = User.query.filter_by(id=user_id).first()

        if form.validate_on_submit():
            user.username = form.username.data
            user.email = form.email.data
            user.team = form.team.data
            user.password_hash = generate_password_hash(form.password.data, method='scrypt')

            try:
                if user.team:
                    db.session.flush()

                    team_to_add_to = db.session.query(Team).get(user.team.id)

                    team_to_add_to.members.append(user)
                    user.teams.append(team_to_add_to)

                db.session.commit()
                return redirect(url_for('general.index'))
            except Exception as e:
                flash('Error! Looks like your inputs are not valid, please check if '
                      'you wrote something in every input field', str(e))

        if current_user:
            form.username.data = user.username
            form.email.data = user.email
            form.team.data = user.team
            form.password.data = 'changeme'
            return render_template('post-channel.html', form=form)

        else:
            return redirect(url_for('general.index'))
    form.team.choices = [(team.id, team.name) for team in Team.query.all()]


@auth_blueprint.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    flash('User logged out!')


@auth_blueprint.route('/delete/<int:user_id>', methods=['GET'])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()

    name = user.username
    try:
        db.session.delete(user)
        db.session.commit()
        flash(f'User {name} deleted')
    except Exception as e:
        flash('something went wrong, please try again', str(e))
