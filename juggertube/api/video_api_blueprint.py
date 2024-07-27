from datetime import datetime

from flask import Blueprint, request, jsonify
from flask_login import login_required

from juggertube.api.serializing import serialize_video, serialize_choices
from juggertube.enums.game_system_enum import GameSystem
from juggertube.models import Video, db, Team, Channel, Tournament
from juggertube.security import api_required
from juggertube.video_type_enum import VideoType

video_api_blueprint = Blueprint('api/videos', __name__)


@video_api_blueprint.route('/add', methods=['GET', 'POST'])
@api_required
def add_video():
    if request.method == 'POST':
        post_data = request.args
        try:
            name = post_data.get('name')
            channel_id = post_data.get('channel_id')
            link = post_data.get('link')
            category = post_data.get('category')
            upload_date = post_data.get('upload_date')
            comments = post_data.get('comments')

            tournament_id = post_data.get('tournament_id')
            team_one_id = post_data.get('team_one_id')
            team_two_id = post_data.get('team_two_id')
            date_of_recording = post_data.get('date_of_recording')
            game_system = post_data.get('game_system')
            weapon_type = post_data.get('weapon_type')
            topic = post_data.get('topic')
            guests = post_data.get('guests')

            if not name or not channel_id or not category or not link or not upload_date:
                return jsonify({'error': 'Missing required parameters'}), 400

            try:
                category = VideoType[category]
            except KeyError:
                return jsonify({'error': 'Invalid category'}), 400

            if category == VideoType.MATCH and not (tournament_id and team_one_id and team_two_id and date_of_recording
                                                    and game_system):
                return jsonify({'error': 'Missing required parameters tournament_id, team_one_id, team_two_id, '
                                         'date_of_recording and game_system for category = MATCH'}), 400

            if game_system:
                try:
                    game_system = GameSystem[game_system]
                except KeyError:
                    return jsonify({'error': 'Invalid game_system'}), 400
            else:
                game_system = None

            upload_date = datetime.strptime(upload_date, '%Y-%m-%dT%H-%M-%S')
            date_of_recording = datetime.strptime(date_of_recording, '%Y-%m-%dT%H-%M-%S') \
                if date_of_recording else None

            new_video = Video(
                name=name,
                channel_id=channel_id,
                category=category,
                link=link,
                upload_date=upload_date,
                comments=comments if comments else None,
                tournament_id=tournament_id if tournament_id else None,
                team_one_id=team_one_id if team_one_id else None,
                team_two_id=team_two_id if team_two_id else None,
                date_of_recording=date_of_recording,
                game_system=game_system,
                weapon_type=weapon_type if weapon_type else None,
                topic=topic if topic else None,
                guests=guests if guests else None
            )

            db.session.add(new_video)
            db.session.commit()

            video = Video.query.filter_by(name=name).first()
            return jsonify(serialize_video(video)), 200
        except Exception as e:
            db.session.rollback()
            return jsonify(str(e)), 500


@video_api_blueprint.route('/edit/<int:video_id>', methods=['GET', 'POST'])
@api_required
def edit_video(video_id):
    video = Video.query.filter_by(id=video_id).first()
    if not video:
        return jsonify({'error': 'video not found'}), 404

    if request.method == 'GET':
        return jsonify(serialize_video(video))

    if request.method == 'POST':
        post_data = request.args
        try:
            name = post_data.get('name')
            channel_id = post_data.get('channel_id')
            link = post_data.get('link')
            category = post_data.get('category')
            upload_date = post_data.get('upload_date')
            comments = post_data.get('comments')

            tournament_id = post_data.get('tournament_id')
            team_one_id = post_data.get('team_one_id')
            team_two_id = post_data.get('team_two_id')
            date_of_recording = post_data.get('date_of_recording')
            game_system = post_data.get('game_system')
            weapon_type = post_data.get('weapon_type')
            topic = post_data.get('topic')
            guests = post_data.get('guests')

            if name:
                video.name = name
            if channel_id:
                video.channel_id = channel_id
            if category:
                try:
                    video.category = VideoType[category]
                except KeyError:
                    return jsonify({'error': 'Invalid category'}), 400
            if link:
                video.link = link
            if upload_date:
                try:
                    video.upload_date = datetime.strptime(upload_date, '%Y-%m-%dT%H-%M-%S')
                except ValueError:
                    return jsonify({'error': 'Invalid upload_date format'}), 400
            if comments:
                video.comments = comments
            if tournament_id:
                video.tournament_id = tournament_id
            if team_one_id:
                video.team_one_id = team_one_id
            if team_two_id:
                video.team_two_id = team_two_id
            if date_of_recording:
                try:
                    video.date_of_recording = datetime.strptime(date_of_recording, '%Y-%m-%dT%H-%M-%S')
                except ValueError:
                    return jsonify({'error': 'Invalid upload_date format'}), 400
            if game_system:
                try:
                    video.game_system = GameSystem[game_system]
                except KeyError:
                    return jsonify({'error': 'Invalid game_system'}), 400
            if weapon_type:
                video.weapon_type = weapon_type
            if topic:
                video.topic = topic
            if guests:
                video.guests = guests

            db.session.commit()

            updated_video = Video.query.filter_by(id=video_id).first()
            return jsonify(serialize_video(updated_video)), 200

        except Exception as e:
            db.session.rollback()
            return jsonify(str(e)), 500


@video_api_blueprint.route('/delete/<int:video_id>', methods=['GET'])
@api_required
def delete_video(video_id):
    video = Video.query.filter_by(id=video_id).first()

    name = video.name

    try:
        db.session.delete(video)
        db.session.commit()

        return jsonify(f'Video {name} deleted'), 200

    except Exception as e:
        return jsonify(str(e)), 400


@video_api_blueprint.route('/', methods=['GET'])
def get_videos():
    videos = Video.query.all()
    video_list = [serialize_video(video) for video in videos]
    return jsonify(video_list)


@video_api_blueprint.route('/team/<int:team_id>', methods=['GET'])
def get_videos_by_team(team_id):
    videos = Video.query.filter((Video.team_one_id == team_id) or (Video.team_two_id == team_id)).all()
    video_list = [serialize_video(video) for video in videos]
    return jsonify(video_list)


@video_api_blueprint.route('/tournament/<int:tournament_id>', methods=['GET'])
def get_videos_by_tournament(tournament_id):
    videos = Video.query.filter_by(tournament_id=tournament_id).all()
    video_list = [serialize_video(video) for video in videos]
    return jsonify(video_list)


@video_api_blueprint.route('/tournament/<int:tournament_id>/team/<int:team_id>', methods=['GET'])
def get_videos_by_tournament_and_team(tournament_id, team_id):
    videos = Video.query.filter_by(tournament_id=tournament_id).filter(
        (Video.team_one_id == team_id) or (Video.team_two_id == team_id)
    ).all()
    video_list = [serialize_video(video) for video in videos]
    return jsonify(video_list)


@video_api_blueprint.route('/period/<string:beginning>/<string:ending>', methods=['GET'])
def get_videos_by_period(beginning, ending):
    videos = Video.query.filter(
        Video.date_of_recording > beginning, Video.date_of_recording < ending
    ).all()
    video_list = [serialize_video(video) for video in videos]
    return jsonify(video_list)


@video_api_blueprint.route('/form-choices', methods=['GET'])
@api_required
def get_form_choices():
    tournaments = [(tournament.id, tournament.name) for tournament in Tournament.query.all()]
    teams = [(team.id, team.name) for team in Team.query.all()]
    channels = [(channel.id, channel.name) for channel in Channel.query.all()]

    tournament_choices = [serialize_choices(tournament) for tournament in tournaments]
    team_choices = [serialize_choices(team) for team in teams]
    channel_choices = [serialize_choices(channel) for channel in channels]

    response = {
        "tournament_choices": tournament_choices,
        "team_choices": team_choices,
        "channel_choices": channel_choices
    }

    return jsonify(response)
