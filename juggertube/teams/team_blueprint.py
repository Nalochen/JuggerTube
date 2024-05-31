from flask import Blueprint, request, url_for, redirect, render_template, jsonify
from flask_login import login_required, current_user

from models import Team, db

from juggertube.webforms import TeamForm, EditTeamForm

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
    form = TeamForm()
    if request.method == 'POST':
        name = form.name.data
        country = form.country.data
        city = form.city.data
        new_team = Team(name=name, country=country, city=city)
        db.session.add(new_team)
        db.session.commit()
        return redirect(url_for('general.index'))
    return render_template('team.html', form=form)


@team_blueprint.route('/edit/<int:team_id>', methods=['GET', 'POST'])
@login_required
def edit_team(team_id):
    if request.method == 'POST':
        team = Team.query.get_or_404(team_id=team_id)
        form = EditTeamForm()

        if form.validate_on_submit():
            team.name = form.name.data
            team.country = form.country.data
            team.city = form.city.data
            db.session.commit()
            return redirect(url_for('general.index'))

        if current_user:
            form.name.data = team.name
            form.country.data = team.country
            form.city.data = team.city
            return render_template('team.html', form=form)

        else:
            return redirect(url_for('general.index'))


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
