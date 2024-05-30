from flask import Blueprint, request, url_for, redirect, render_template, jsonify
from flask_login import login_required

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
@login_required
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


@team_blueprint.route('/edit/<int:team_id>', methods=['GET', 'POST'])
@login_required
def edit_team(team_id):
    if request.method == 'POST':
        team = Team.query.filter_by(team_id=team_id).all()

        name = request.form['name']
        country = request.form['country']
        city = request.form['city']

        if name:
            team.name = name
        if country:
            team.country = country
        if city:
            team.city = city

        db.session.commit()
        return redirect(url_for('general.index'))
    return render_template('edit_team.html')


@team_blueprint.route('/delete/<int:team_id>', methods=['GET'])
@login_required
def delete_team(team_id):
    team = Team.query.filter_by(team_id=team_id).first()

    name = team.name

    db.session.delete(team)
    db.session.commit()
    return f'<h1>Team {name} deleted<h1>'


@team_blueprint.route('/', methods=['GET'])
def get_teams():
    teams = Team.query.all()
    team_list = [serialize_team(team) for team in teams]
    return jsonify(team_list)
