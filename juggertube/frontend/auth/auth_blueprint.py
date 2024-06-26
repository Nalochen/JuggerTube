from flask import Blueprint, jsonify, request, render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from juggertube.api.serializing import serialize_user
from juggertube.models import User, Team, db
from juggertube.webforms import RegisterForm, LoginForm

auth_blueprint = Blueprint('auth', __name__, template_folder='templates')


@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)

    if request.method == 'GET':
        form.team.choices = [(team.id, team.name) for team in Team.query.all()]
        return render_template('register.html', form=form)

    if request.method == 'POST':
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            return redirect(url_for('auth.login'))

        email = form.email.data
        username = form.username.data
        password_hash = generate_password_hash(form.password.data, method='scrypt')

        try:
            new_user = User(email=email, username=username, password_hash=password_hash)
            db.session.add(new_user)
            new_user.teams.append(Team.query.filter_by(id=form.team.data).first())

            db.session.commit()
            login_user(new_user)
            flash('Account successfully created', 'info')
        except Exception as e:
            flash(str(e), 'danger')


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if request.method == 'GET':
        return render_template('login.html', form=form)

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
            flash('login seems to not have worked, please try again', 'info')
            return render_template('login.html', form=form)


@auth_blueprint.route('edit/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    form = RegisterForm()
    form.team.choices = [(team.id, team.name) for team in Team.query.all()]
    user = User.query.filter_by(id=user_id).first()

    if request.method == 'GET':
        form.username.data = user.username
        form.email.data = user.email
        form.team.data = user.teams
        form.password.data = 'changeme'
        return render_template('register.html', form=form)

    if request.method == 'POST':
        if form.validate_on_submit():
            user.username = form.username.data
            user.email = form.email.data
            user.password_hash = generate_password_hash(form.password.data, method='scrypt')

            team_id = form.team.data
            if team_id:
                team_to_add_to = Team.query.get(team_id)
                if team_to_add_to not in user.teams:
                    user.teams.append(team_to_add_to)
            else:
                user.teams = []

            try:
                db.session.commit()
                return redirect(url_for('general.index'))
            except Exception as e:
                flash('Error! Looks like your inputs are not valid, please check if you wrote something in every '
                      'input field', str(e))
                return render_template('register.html', form=form)
        else:
            flash('Form validation failed. Please check your inputs.', 'error')
            return render_template('register.html', form=form)


@auth_blueprint.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    flash('User logged out!')
    return redirect(url_for('general.index'))


@auth_blueprint.route('/delete/<int:user_id>', methods=['GET'])
@login_required
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()

    name = user.username
    try:
        db.session.delete(user)
        db.session.commit()
        flash(f'User {name} deleted')
        return redirect(url_for('general.index'))
    except Exception as e:
        flash('something went wrong, please try again', str(e))
        return redirect(url_for('auth.delete_user/{user_id}'))
