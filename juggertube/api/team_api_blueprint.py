from flask import Blueprint, request, jsonify
from flask_login import login_required

from juggertube.api.serializing import serialize_team
from juggertube.models import Team, db
from juggertube.security import api_required

team_api_blueprint = Blueprint('api/teams', __name__)


@team_api_blueprint.route('/add', methods=['POST'])
@api_required
def add_team():
    print('here')
    post_data = request.args
    name = post_data.get("name")
    country = post_data.get("country")
    city = post_data.get("city")

    if not name or not country or not city:
        return jsonify({'error': 'Name, Country and City are required'}), 400

    new_team = Team(name=name, country=country, city=city)

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
@api_required
def edit_team(team_id):
    team = Team.query.filter_by(id=team_id).first()

    if not team:
        return jsonify({'error': 'Team not found'}), 404

    if request.method == 'GET':
        return jsonify(serialize_team(team)), 200

    if request.method == 'POST':
        post_data = request.args
        name = post_data.get("name")
        city = post_data.get("city")
        country = post_data.get("country")

        if not name or not country or not city:
            return jsonify({'error': 'Name, Country and City are required'}), 400

        team.name = name
        team.city = city
        team.country = country

        try:
            db.session.commit()

            edited_team = serialize_team(Team.query.filter_by(id=team.id).first())
            return jsonify(edited_team), 200
        except Exception as e:
            return jsonify(str(e)), 400


@team_api_blueprint.route('/delete/<int:team_id>', methods=['GET'])
@api_required
def delete_team(team_id):
    team = Team.query.filter_by(id=team_id).first()

    if not team:
        return jsonify('Team not found'), 404

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
