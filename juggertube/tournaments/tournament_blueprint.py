from flask import Blueprint, request, url_for, redirect, render_template

from models import Video, User, Team, Tournament, Channel, db

tournament_blueprint = Blueprint('tournaments', __name__, template_folder='templates')


@tournament_blueprint.route('/add', methods=['GET', 'POST'])
def add_tournament():
    if request.method == 'POST':
        name = request.form['name']
        date_beginning = request.form['date_beginning']
        date_ending = request.form['date_ending']
        city = request.form['city']
        jtr_link = request.form['jtr_link']
        new_tournament = Tournament(name=name, date_beginning=date_beginning,
                                    date_ending=date_ending, city=city,
                                    jtr_link=jtr_link)
        db.session.add(new_tournament)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_tournament.html')
