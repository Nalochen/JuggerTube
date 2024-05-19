from flask import Blueprint, request, url_for, redirect, render_template, jsonify

from models import Team, db

team_blueprint = Blueprint('teams', __name__, template_folder='templates')


def serialize_team(team):
    return {
        'team_id': team.team_id,
        'name': team.name,
        'country': team.country,
        'city': team.city,
    }


@team_blueprint.route('/add', methods=['GET', 'POST'])
def add_team():
    if request.method == 'POST':
        name = request.form['name']
        country = request.form['country']
        city = request.form['city']
        new_team = Team(name=name, country=country, city=city)
        db.session.add(new_team)
        db.session.commit()
        return redirect(url_for('general.index'))
    return render_template('add_team.html')


@team_blueprint.route('/', methods=['GET'])
def get_teams():
    teams = Team.query.all()
    team_list = [serialize_team(team) for team in teams]
    return jsonify(team_list)
