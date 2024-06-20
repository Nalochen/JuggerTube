from flask import Blueprint, request, url_for, redirect, render_template, jsonify, flash
from flask_login import login_required, current_user

from juggertube.models import Team, db

from juggertube.webforms import TeamForm

team_blueprint = Blueprint('teams', __name__, template_folder='templates')


def serialize_team(team):
    return {
        'team_id': team.id,
        'name': team.name,
        'country': team.country,
        'city': team.city,
    }


@team_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add_team():
    form = TeamForm(request.form)
    if request.method == 'POST':
        name = form.name.data
        country = form.country.data
        city = form.city.data
        new_team = Team(name=name, country=country, city=city)
        try:
            db.session.add(new_team)
            db.session.commit()
            return redirect(url_for('general.index'))
        except Exception as e:
            flash('Error! looks like there was a problem... please try agin!', str(e))
            return render_template('post-channel.html', form=form)

    if request.method == 'GET':
        return render_template('post-team.html', form=form)


@team_blueprint.route('/edit/<int:team_id>', methods=['GET', 'POST'])
@login_required
def edit_team(team_id):
    team = Team.query.filter_by(id=team_id).first()
    form = TeamForm(team=request.form)

    if request.method == 'GET':
        form.name.data = team.name
        form.country.data = team.country
        form.city.data = team.city

    if form.validate_on_submit():
        team.name = form.name.data
        team.country = form.country.data
        team.city = form.city.data

        try:
            db.session.commit()
            return redirect(url_for('general.index'))
        except Exception as e:
            flash('Error! Looks like your inputs are not valid, please check if '
                  'you wrote something in every input field', str(e))

    if request.method == 'GET':
        return render_template('post-team.html', form=form)


@team_blueprint.route('/delete/<int:team_id>', methods=['GET'])
@login_required
def delete_team(team_id):
    team = Team.query.filter_by(id=team_id).first()

    name = team.name

    try:
        db.session.delete(team)
        db.session.commit()
        flash(f'Team {name} deleted')
    except Exception as e:
        flash('something went wrong please try again', str(e))

    return redirect(url_for('general.index'))


@team_blueprint.route('/', methods=['GET'])
def get_teams():
    teams = Team.query.all()
    team_list = [serialize_team(team) for team in teams]
    return render_template('show-teams.html', channel_list=jsonify(team_list))
