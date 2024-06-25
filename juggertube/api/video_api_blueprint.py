from datetime import datetime

from flask import Blueprint, request, jsonify
from flask_login import login_required

from juggertube.api.serializing import serialize_video, serialize_team, serialize_tournament, serialize_channel, \
    serialize_choices
from juggertube.game_system_enum import GameSystem
from juggertube.models import Video, db, Team, Channel, Tournament
from juggertube.video_type_enum import VideoType

video_api_blueprint = Blueprint('api/videos', __name__)


@video_api_blueprint.route('/add', methods=['GET', 'POST'])
def add_video():
    if request.method == 'POST':
        post_data = request.args
        video_data = {
            'name': post_data.get('name'),
            'channel_id': post_data.get('channel_id'),
            'category': VideoType[post_data.get('category')],
            'link': post_data.get('link'),
            'upload_date': datetime.strptime(post_data.get('upload_date'), '%Y-%m-%dT%H-%M-%S'),
        }

        print(video_data)

        if (not video_data['name'] or not video_data['channel_id'] or not video_data['category']
                or not video_data['link'] or not video_data['upload_date']):
            return jsonify({'error': 'name, channel_id, category, link and uploadDate are required'}), 400

        comments = post_data.get("comments")
        tournament_id = post_data.get("tournament_id")
        team_one_id = post_data.get("team_one_id")
        team_two_id = post_data.get("team_two_id")
        date_of_recording = post_data.get('date_of_recording'),
        weapon_type = post_data.get("weapon_type")
        topic = post_data.get("topic")
        guests = post_data.get("guests")
        if post_data.get('game_system'):
            video_data['game_system'] = GameSystem[post_data.get('game_system')]

        if video_data['category'] == VideoType.MATCH and not (tournament_id and team_one_id and team_two_id
                                                              and date_of_recording and video_data['game_system']):
            return jsonify({'error': 'When the Video is a Match, tournament_id, team_one_id, team_two_id, '
                                     'date_of_recording and game_system are required'}), 400

        if tournament_id:
            video_data['tournament_id'] = tournament_id
        if team_one_id:
            video_data['team_one_id'] = team_one_id
            video_data['team_one'] = Team.query.filter_by(id=team_one_id).first()
        if team_two_id:
            video_data['team_two_id'] = team_two_id
            video_data['team_two'] = Team.query.filter_by(id=team_two_id).first()
        if date_of_recording:
            video_data['date_of_recording'] = date_of_recording

        if comments:
            video_data['comments'] = comments
        if weapon_type:
            video_data['weapon_type'] = weapon_type
        if topic:
            video_data['topic'] = topic
        if guests:
            video_data['guests'] = guests

        new_video = Video(**video_data)

        existing_video = Video.query.filter_by(name=new_video.name).first()
        if existing_video:
            return jsonify(serialize_video(existing_video), 'video already exists'), 400
        else:
            try:
                db.session.add(new_video)
                db.session.commit()

                video = Video.query.filter_by(name=new_video.name).first()
                serialized_video = serialize_video(video)
                return jsonify(serialized_video), 200
            except Exception as e:
                db.session.rollback()
                return jsonify(str(e)), 400


@video_api_blueprint.route('/edit/<int:video_id>', methods=['GET', 'POST'])
@login_required
def edit_video(video_id):
    video = Video.query.filter_by(id=video_id).first()

    if request.method == 'GET':
        return jsonify(serialize_video(video))

    if request.method == 'POST':
        post_data = request.args
        video.name = post_data["name"]
        video.channel_id = post_data["channel_id"]
        video.link = post_data["link"]
        video.category = VideoType[post_data["category"]]
        video.upload_date = post_data["upload_date"]
        video.tournament_id = post_data["tournament_id"]
        video.team_one_id = post_data["team_one_id"]
        video.team_one = Team.query.filter_by(id=post_data["team_one_id"]).first()
        video.team_two_id = post_data["team_two_id"]
        video.team_two = Team.query.filter_by(id=post_data["team_two_id"]).first()
        video.date_of_recording = post_data["date_of_recording"]
        if post_data["game_system"] != '':
            video.game_system = GameSystem[post_data["game_system"]]
        else:
            video.game_system = None
        video.weapon_type = post_data["weapon_type"]
        video.topic = post_data["topic"]
        video.guests = post_data["guests"]
        video.comments = post_data["comments"]

        try:
            db.session.commit()

            edited_video = serialize_video(Video.query.filter_by(id=video.id).first())
            return jsonify(edited_video), 200
        except Exception as e:
            return jsonify(str(e)), 400


@video_api_blueprint.route('/delete/<int:video_id>', methods=['GET'])
@login_required
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
