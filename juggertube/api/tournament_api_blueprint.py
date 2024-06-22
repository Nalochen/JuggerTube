from flask import Blueprint, request, jsonify
from flask_login import login_required

from juggertube.api.serializing import serialize_tournament
from juggertube.models import Team, db, Tournament

tournament_api_blueprint = Blueprint('api/teams', __name__)


@tournament_api_blueprint.route('/add', methods=['POST'])
def add_tournament():
    post_data = request.args
    new_tournament = Tournament(name=post_data["name"], city=post_data["city"], jtr_link=post_data["jtr_link"],
                                tugeny_link=post_data["tugrny_link"])

    existing_tournament = Tournament.query.filter_by(name=new_tournament.name).first()
    if existing_tournament:
        return jsonify(serialize_tournament(existing_tournament), 'tournament already exists'), 400
    else:
        try:
            db.session.add(new_tournament)
            db.session.commit()

            tournament = serialize_tournament(Team.query.filter_by(name=new_tournament.name).first())
            return jsonify(tournament), 200

        except Exception as e:
            return jsonify(str(e)), 400


@tournament_api_blueprint.route('/edit/<int:tournament_id>', methods=['GET', 'POST'])
@login_required
def edit_tournament(tournament_id):
    tournament = Tournament.query.filter_by(id=tournament_id).first()

    if request.method == 'GET':
        return jsonify(serialize_tournament(tournament))

    if request.method == 'POST':
        post_data = request.args
        tournament.name = post_data["name"]
        tournament.city = post_data["city"]
        tournament.jtr_link = post_data["jtr_link"]
        tournament.tugeny_link = post_data["tugeny_link"]

        try:
            db.session.commit()

            edited_tournament = serialize_tournament(Tournament.query.filter_by(id=tournament.id).first())
            return jsonify(edited_tournament), 200
        except Exception as e:
            return jsonify(str(e)), 400


@tournament_api_blueprint.route('/delete/<int:tournament_id>', methods=['GET'])
@login_required
def delete_tournament(tournament_id):
    tournament = Tournament.query.filter_by(id=tournament_id).first()

    name = tournament.name

    try:
        db.session.delete(tournament)
        db.session.commit()

        return jsonify(f'Tournament {name} deleted'), 200

    except Exception as e:
        return jsonify(str(e)), 400


@tournament_api_blueprint.route('/', methods=['GET'])
def get_tournaments():
    tournaments = Tournament.query.all()
    tournament_list = [serialize_tournament(tournament) for tournament in tournaments]
    return jsonify(tournament_list)
