from flask import Blueprint, request, jsonify
from flask_login import login_required

from juggertube.api.serializing import serialize_tournament
from juggertube.models import Team, db, Tournament
from juggertube.security import api_required

tournament_api_blueprint = Blueprint('api/tournaments', __name__)


@tournament_api_blueprint.route('/add', methods=['POST'])
@api_required
def add_tournament():
    post_data = request.args
    tournament_data = {
        'name': post_data.get("name"),
        'city': post_data.get("city")
    }

    if not tournament_data['name'] or not tournament_data['city']:
        return jsonify({'error': 'Name and city are required'}), 400

    jtr_link = post_data.get("jtrLink")
    tugeny_link = post_data.get("tugenyLink")

    if jtr_link:
        tournament_data['jtr_link'] = jtr_link

    if tugeny_link:
        tournament_data['tugeny_link'] = tugeny_link

    new_tournament = Tournament(**tournament_data)
    existing_tournament = Tournament.query.filter_by(name=new_tournament.name).first()
    if existing_tournament:
        return jsonify(serialize_tournament(existing_tournament), 'tournament already exists'), 400
    else:
        try:
            db.session.add(new_tournament)
            db.session.commit()

            tournament = serialize_tournament(Tournament.query.filter_by(name=new_tournament.name).first())
            return jsonify(tournament), 200

        except Exception as e:
            return jsonify(str(e)), 400


@tournament_api_blueprint.route('/edit/<int:tournament_id>', methods=['GET', 'POST'])
@api_required
def edit_tournament(tournament_id):
    tournament = Tournament.query.filter_by(id=tournament_id).first()

    if request.method == 'GET':
        if not tournament:
            return jsonify('Tournament not found'), 404
        return jsonify(serialize_tournament(tournament))

    if request.method == 'POST':
        post_data = request.args

        if not tournament:
            return jsonify('Tournament not found'), 404

        name = post_data.get("name")
        city = post_data.get("city")

        if not name or not city:
            return jsonify({'error': 'Name and city are required'}), 400

        tournament.name = name
        tournament.city = city

        jtr_link = post_data.get("jtrLink")
        tugeny_link = post_data.get("tugenyLink")

        if jtr_link:
            tournament.jtr_link = jtr_link
        else:
            tournament.jtr_link = None

        if tugeny_link:
            tournament.tugeny_link = tugeny_link
        else:
            tournament.tugeny_link = None

        try:
            db.session.commit()

            edited_tournament = serialize_tournament(Tournament.query.filter_by(id=tournament.id).first())
            return jsonify(edited_tournament), 200
        except Exception as e:
            return jsonify(str(e)), 400


@tournament_api_blueprint.route('/delete/<int:tournament_id>', methods=['GET'])
@api_required
def delete_tournament(tournament_id):
    tournament = Tournament.query.filter_by(id=tournament_id).first()

    if not tournament:
        return jsonify('Tournament not found'), 404

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
