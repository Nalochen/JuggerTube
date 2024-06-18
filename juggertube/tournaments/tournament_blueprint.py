from datetime import datetime

from flask import Blueprint, request, url_for, redirect, render_template, jsonify, flash
from flask_login import login_required, current_user

from juggertube.models import Tournament, db

from juggertube.webforms import TournamentForm

tournament_blueprint = Blueprint('tournaments', __name__, template_folder='templates')


def serialize_tournament(tournament):
    return {
        'tournament_id': tournament.id,
        'name': tournament.name,
        'city': tournament.city,
        'jtr_link': tournament.jtr_link,
        'tugeny_link': tournament.tugeny_link,
    }


@tournament_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add_tournament():
    form = TournamentForm(request.form)
    if request.method == 'POST':
        name = form.name.data
        city = form.city.data
        jtr_link = form.jtr_link.data
        tugeny_link = form.tugeny_link.data
        new_tournament = Tournament(name=name, city=city,
                                    jtr_link=jtr_link, tugeny_link=tugeny_link)
        try:
            db.session.add(new_tournament)
            db.session.commit()
            return redirect(url_for('general.index'))
        except Exception as e:
            flash('something went wrong, please try again', str(e))

    return render_template('post-tournaments.html', form=form)


@tournament_blueprint.route('/edit/<int:tournament_id>', methods=['GET', 'POST'])
@login_required
def edit_tournament(tournament_id):
    tournament = Tournament.query.filter_by(id=tournament_id).first()
    form = TournamentForm(tournament=request.form)

    if request.method == 'GET':
        form.name.data = tournament.name
        form.city.data = tournament.city
        form.jtr_link.data = tournament.jtr_link
        form.tugeny_link.data = tournament.tugeny_link

    if form.validate_on_submit():
        tournament.name = form.name.data
        tournament.city = form.city.data
        tournament.jtr_link = form.jtr_link.data
        tournament.tugeny_link = form.tugeny_link.data
        try:
            db.session.commit()
            return redirect(url_for('general.index'))
        except Exception as e:
            db.session.rollback()
            flash('something went wrong, please try again', str(e))

    return render_template('post-tournaments.html', form=form, tournament=tournament)


@tournament_blueprint.route('/delete/<int:tournament_id>', methods=['GET'])
@login_required
def delete_tournament(tournament_id):
    tournament = Tournament.query.filter_by(id=tournament_id).first()

    name = tournament.name
    try:
        db.session.delete(tournament)
        db.session.commit()
        flash(f'Tournament {name} deleted')
    except Exception as e:
        flash('something went wrong, please try again', str(e))

    return redirect(url_for('general.index'))


@tournament_blueprint.route('/', methods=['GET'])
def get_tournaments():
    tournaments = Tournament.query.all()
    tournament_list = [serialize_tournament(tournament) for tournament in tournaments]
    return render_template('show-tournaments.html', channel_list=jsonify(tournament_list))