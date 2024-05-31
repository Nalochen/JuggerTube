from datetime import datetime

from flask import Blueprint, request, url_for, redirect, render_template, jsonify
from flask_login import login_required, current_user

from models import Video, User, Team, Tournament, Channel, db

from juggertube.webforms import TournamentForm, EditTournamentForm

tournament_blueprint = Blueprint('tournaments', __name__, template_folder='templates')


def serialize_tournament(tournament):
    return {
        'tournament_id': tournament.tournament_id,
        'name': tournament.name,
        'date_beginning': tournament.date_beginning.strftime('%Y-%m-%d'),
        'date_ending': tournament.date_ending.strftime('%Y-%m-%d'),
        'city': tournament.city,
        'jtr_link': tournament.jtr_link,
    }


@tournament_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add_tournament():
    form = TournamentForm()
    if request.method == 'POST':
        name = form.name.data
        date_beginning = form.date_beginning.data
        date_ending = form.date_ending.data
        city = form.city.data
        jtr_link = form.jtr_link.data
        new_tournament = Tournament(name=name, date_beginning=date_beginning,
                                    date_ending=date_ending, city=city,
                                    jtr_link=jtr_link)
        db.session.add(new_tournament)
        db.session.commit()
        return redirect(url_for('general.index'))
    return render_template('tournament.html', form=form)


@tournament_blueprint.route('/edit/<int:tournament_id>', methods=['GET', 'POST'])
@login_required
def edit_tournament(tournament_id):
    if request.method == 'POST':
        tournament = Tournament.query.get_or_404(tournament_id=tournament_id)
        form = EditTournamentForm()

        if form.validate_on_submit():
            tournament.name = form.name.data
            tournament.date_beginning = form.date_beginning.data
            tournament.date_ending = form.date_ending.data
            tournament.city = form.city.data
            tournament.jtr_link = form.jtr_link.data
            db.session.commit()
            return redirect(url_for('general.index'))

        if current_user:
            form.name.data = tournament.name
            form.date_beginning.data = tournament.date_beginning
            form.date_ending = tournament.date_ending
            form.city.data = tournament.city
            form.jtr_link = tournament.jtr_link
            return render_template('tournament.html', form=form)
        else:
            return redirect(url_for('general.index'))


@tournament_blueprint.route('/delete/<int:tournament_id>', methods=['GET'])
@login_required
def delete_tournament(tournament_id):
    tournament = Tournament.query.filter_by(tournament_id=tournament_id).first()

    name = tournament.name

    db.session.delete(tournament)
    db.session.commit()
    return f'<h1>Tournament {name} deleted<h1>'


@tournament_blueprint.route('/', methods=['GET'])
def get_tournaments():
    tournaments = Tournament.query.all()
    tournament_list = [serialize_tournament(tournament) for tournament in tournaments]
    return jsonify(tournament_list)


@tournament_blueprint.route('/period/<string:beginning>/<string:ending>', methods=['GET'])
def get_tournament_by_period(beginning, ending):
    beginning_date = datetime.strptime(beginning, '%Y-%m-%d')
    ending_date = datetime.strptime(ending, '%Y-%m-%d')

    tournaments = Tournament.query.filter(
        Tournament.date_beginning >= beginning_date,
        Tournament.date_ending <= ending_date
    ).all()
    return tournaments
