from flask import Blueprint, request, url_for, redirect, render_template, jsonify, flash
from flask_login import login_required, current_user

from juggertube.api.serializing import serialize_team
from juggertube.models import Team, db

from juggertube.webforms import TeamForm

team_api_blueprint = Blueprint('api/teams', __name__)


@team_api_blueprint.route('/add', methods=['POST'])
def add_team():
    post_data = request.args
    new_team = Team(name=post_data["name"], country=post_data["country"], city=post_data["city"])

    existing_team = Team.query.filter_by(name=new_team.name).first()
    if existing_team:
        return jsonify(serialize_team(existing_team), 'team already exists'), 400
    else:
        try:
            db.session.add(new_team)
            db.session.commit()

            team = serialize_team(Team.query.filter_by(name=new_team.name).first())
            return jsonify(team), 200

        except Exception as e:
            return jsonify(str(e)), 400


@team_api_blueprint.route('/edit/<int:team_id>', methods=['GET', 'POST'])
@login_required
def edit_team(team_id):
    team = Team.query.filter_by(id=team_id).first()

    if request.method == 'GET':
        return jsonify(serialize_team(team))

    if request.method == 'POST':
        post_data = request.args
        team.name = post_data["name"]
        team.city = post_data["city"]
        team.country = post_data["country"]

        try:
            db.session.commit()

            edited_team = serialize_team(Team.query.filter_by(id=team.id).first())
            return jsonify(edited_team), 200
        except Exception as e:
            return jsonify(str(e)), 400


@team_api_blueprint.route('/delete/<int:team_id>', methods=['GET'])
@login_required
def delete_team(team_id):
    team = Team.query.filter_by(id=team_id).first()

    name = team.name

    try:
        db.session.delete(team)
        db.session.commit()

        return jsonify(f'Team {name} deleted'), 200

    except Exception as e:
        return jsonify(str(e)), 400


@team_api_blueprint.route('/', methods=['GET'])
def get_teams():
    teams = Team.query.all()
    team_list = [serialize_team(team) for team in teams]
    return jsonify(team_list)
