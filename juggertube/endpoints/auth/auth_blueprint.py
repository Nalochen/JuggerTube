from flask import Blueprint, request, url_for, redirect, render_template, jsonify, flash, current_app

from juggertube.api import auth_api_blueprint
from juggertube.models import db, User, Team
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_required, logout_user, login_user

from juggertube.webforms import RegisterForm, LoginForm

auth_blueprint = Blueprint('auth', __name__, template_folder='templates')


@auth_blueprint.route('/', methods=['GET'])
def get_users():
    response = auth_api_blueprint.get_users()
    return response


@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    with current_app.test_client() as client:
        form = RegisterForm(request.form)
        if request.method == 'GET':
            response = auth_api_blueprint.get_team_choices()
            data = response.get_json()

            form.team.choices = data
            return render_template('register.html', form=form)

        if request.method == 'POST':
            post_data = {
                "email": form.email.data,
                "username": form.username.data,
                "password_hash": generate_password_hash(form.password.data, method='scrypt'),
                "team": form.team.data
            }

            response = client.post('/api/auth/register', query_string=post_data)
            data = response.get_json()
            return data


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    with current_app.test_client() as client:
        form = LoginForm(request.form)
        if request.method == 'GET':
            return render_template('login.html', form=form)

        if request.method == 'POST':
            next_page = request.args.get('next')
            post_data = {
                "username": form.username.data,
                "password": form.password.data #ask prof at thursday!
            }

            response = client.post('/api/auth/login', query_string=post_data)
            data = response.get_json()

            if response.status_code == 200:
                flash(data, 'info')
                return redirect(next_page) if next_page else redirect(url_for('general.index'))
            else:
                flash(data, 'info')
                return render_template('login.html', form=form)


@auth_blueprint.route('/edit/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    with current_app.test_client() as client:
        form = RegisterForm()

        if request.method == 'GET':
            response = auth_api_blueprint.get_team_choices()
            data = response.get_json()

            form.team.choices = data

            response = auth_api_blueprint.edit_user(user_id)
            data = response.get_json()

            form.username.data = data["username"]
            form.email.data = data["email"]
            form.team.data = data["team"]
            form.password.data = "changeme"

            return render_template('register.html', form=form)

        if request.method == 'POST':
            if form.validate_on_submit():
                post_data = {
                    "username": form.username.data,
                    "email": form.email.data,
                    "team": form.team.data,
                    "password_hash": generate_password_hash(form.password.data, method='scrypt')
                }

                response = client.post(f'/api/edit/{user_id}', query_string=post_data)
                data = response.get_json()
                return data
            else:
                return render_template('register.html', form=form)


@auth_blueprint.route('/logout', methods=['GET'])
@login_required
def logout():
    response = auth_api_blueprint.get_team_choices()
    data = response.get_json()
    flash(data, 'info')
    return redirect(url_for('general.index'))


@auth_blueprint.route('/delete/<int:user_id>', methods=['GET'])
def delete_user(user_id):
    response = auth_api_blueprint.delete_user(user_id)
    deleted_user = response[0].get_json()
    return deleted_user
