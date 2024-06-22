from flask import Blueprint, request, url_for, redirect, render_template, flash, current_app
from flask_login import login_required

from juggertube.api import tournament_api_blueprint
from juggertube.models import Tournament, db

from juggertube.webforms import TournamentForm

tournament_blueprint = Blueprint('tournaments', __name__, template_folder='templates')


@tournament_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add_tournament():
    with current_app.test_client() as client:
        form = TournamentForm(request.form)

        if request.method == 'GET':
            return render_template('post-tournament.html', form=form)

        if request.method == 'POST':
            post_data = {
                "name": form.name.data,
                "city": form.city.data,
                "jtr_link": form.jtr_link.data,
                "tugeny_link": form.tugeny_link.data
            }
            response = client.post('/api/tournaments/add', query_string=post_data)
            data = response.get_json()
            return data


@tournament_blueprint.route('/edit/<int:tournament_id>', methods=['GET', 'POST'])
@login_required
def edit_tournament(tournament_id):
    with current_app.test_client() as client:
        form = TournamentForm(team=request.form)

        if request.method == 'GET':
            response = tournament_api_blueprint.edit_tournament(tournament_id)
            data = response.get_json()

            form.name.data = data['name']
            form.city.data = data['city']
            form.jtr_link.data = data['jtr_link']
            form.tugeny_link.data = data['tugeny_link']

            return render_template('post-tournaments.html', form=form)

        if request.method == 'POST':
            if form.validate_on_submit():
                post_data = {
                    "name": form.name.data,
                    "city": form.city.data,
                    "jtr_link": form.jtr_link.data,
                    "tugeny_link": form.tugeny_link.data
                }

                response = client.post(f'/api/tournaments/edit/{tournament_id}', query_string=post_data)
                data = response.get_json()
                return data
            else:
                return render_template('post-tournaments.html', form=form)


@tournament_blueprint.route('/delete/<int:tournament_id>', methods=['GET'])
@login_required
def delete_tournament(tournament_id):
    response = tournament_api_blueprint.delete_tournament(tournament_id)
    deleted_tournament = response.get_json
    return deleted_tournament


@tournament_blueprint.route('/', methods=['GET'])
def get_tournaments():
    response = tournament_api_blueprint.get_tournaments()
    tournaments_list = response.get_json()
    return render_template('show-tournaments.html', tournament_list=tournaments_list)
