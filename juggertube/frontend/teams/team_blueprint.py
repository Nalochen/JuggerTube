from flask import Blueprint, request, render_template, current_app
from flask_login import login_required

from juggertube.api import team_api_blueprint

from juggertube.webforms import TeamForm

team_blueprint = Blueprint('teams', __name__, template_folder='templates')


@team_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add_team():
    with current_app.test_client() as client:
        form = TeamForm(request.form)

        if request.method == 'GET':
            return render_template('post-team.html', form=form)

        if request.method == 'POST':
            post_data = {
                "name": form.name.data,
                "country": form.country.data,
                "city": form.city.data
            }
            response = client.post('/api/teams/add', query_string=post_data)
            data = response.get_json()
            return data


@team_blueprint.route('/edit/<int:team_id>', methods=['GET', 'POST'])
@login_required
def edit_team(team_id):
    with current_app.test_client() as client:
        form = TeamForm(team=request.form)

        if request.method == 'GET':
            response = team_api_blueprint.edit_team(team_id)
            data = response.get_json()

            form.name.data = data['name']
            form.country.data = data['country']
            form.city.data = data['city']

            return render_template('post-team.html', form=form)

        if request.method == 'POST':
            if form.validate_on_submit():
                post_data = {
                    "name": form.name.data,
                    "country": form.country.data,
                    "city": form.city.data
                }

                response = client.post(f'/api/teams/edit/{team_id}', query_string=post_data)
                data = response.get_json()
                return data
            else:
                return render_template('post-team.html', form=form)


@team_blueprint.route('/delete/<int:team_id>', methods=['GET'])
@login_required
def delete_team(team_id):
    response = team_api_blueprint.delete_team(team_id)
    deleted_team = response.get_json
    return deleted_team


@team_blueprint.route('/', methods=['GET'])
def get_teams():
    response = team_api_blueprint.get_teams()
    teams_list = response.get_json()
    return render_template('show-teams.html', team_list=teams_list)
