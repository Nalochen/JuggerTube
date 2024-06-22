import ast

from flask import Blueprint, request, jsonify
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash

from juggertube.api.serializing import serialize_user, serialize_choices
from juggertube.models import Team, db, User

auth_api_blueprint = Blueprint('api/auth', __name__)


@auth_api_blueprint.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [serialize_user(user) for user in users]
    return jsonify(user_list)


@auth_api_blueprint.route('/register', methods=['POST'])
def register():
    post_data = request.args

    user_data = {
        'username': post_data["username"],
        'email': post_data["email"],
        'password_hash': post_data["password_hash"]
    }

    teams = ast.literal_eval(post_data["team"])

    new_user = User(**user_data)

    if post_data["team"] is not None:
        new_user.teams = [Team.query.filter_by(id=teams["choice_id"]).first()]

    existing_user = User.query.filter_by(email=new_user.email).first()
    if existing_user:
        return jsonify('User already exists')
    else:
        try:
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)

            return jsonify(f'{new_user.username}'), 200

        except Exception as e:
            return jsonify(str(e)), 400


@auth_api_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        post_data = request.args

        user = User.query.filter_by(username=post_data["username"]).first()
        if user and check_password_hash(user.password_hash, post_data["password"]):
            login_user(user)
            return jsonify("successfull"), 200
        else:
            return jsonify("an error occurred, please check username and password"), 404


@auth_api_blueprint.route('/edit/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    user = User.query.filter_by(id=user_id).first()

    if request.method == 'GET':
        return jsonify(serialize_user(user))

    if request.method == 'POST':
        post_data = request.args
        user.username = post_data["name"]
        user.email = post_data["link"]
        user.team = Team.query.filter_by(id=post_data["team"])
        user.password_hash = post_data["password_hash"]

        try:
            db.session.commit()

            return jsonify(f'changed user {user.username}'), 200
        except Exception as e:
            return jsonify(str(e)), 400


@auth_api_blueprint.route('/logout>', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify("User has been logged out"), 200


@auth_api_blueprint.route('/delete/<int:user_id>', methods=['GET'])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()

    if user is not None:
        name = user.username

        try:
            db.session.delete(user)
            db.session.commit()

            return jsonify(f'User {name} deleted'), 200

        except Exception as e:
            return jsonify(str(e)), 400
    else:
        return jsonify('User does not exist'), 404


@auth_api_blueprint.route('/team-choices', methods=['GET'])
def get_team_choices():
    teams = [(team.id, team.name) for team in Team.query.all()]
    team_choices = [serialize_choices(choice) for choice in teams]

    return jsonify(team_choices)
