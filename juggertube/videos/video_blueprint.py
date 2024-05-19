from flask import Blueprint, request, url_for, redirect, render_template, jsonify

from models import Video, User, Team, Tournament, Channel, db

video_blueprint = Blueprint('videos', __name__, template_folder='templates')


def serialize_video(video):
    return {
        'video_id': video.video_id,
        'name': video.name,
        'channel_id': video.channel_id,
        'link': video.link,
        'tournament_id': video.tournament_id,
        'team_one_id': video.team_one_id,
        'team_two_id': video.team_two_id,
        'upload_date': video.upload_date.isoformat(),
        'comments': video.comments,
        'type': video.type
    }


@video_blueprint.route('/add', methods=['GET', 'POST'])
def add_video():
    if request.method == 'POST':
        name = request.form['name']
        channel_id = request.form['channel_id']
        link = request.form['link']
        tournament_id = request.form['tournament_id']
        team_one_id = request.form['team_one_id']
        team_two_id = request.form['team_two_id']
        upload_date = request.form['upload_date']
        comments = request.form['comments']
        video_type = request.form['type']
        new_video = Video(name=name, channel_id=channel_id, link=link,
                          tournament_id=tournament_id, team_one_id=team_one_id,
                          team_two_id=team_two_id, upload_date=upload_date,
                          comments=comments, type=video_type)
        db.session.add(new_video)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_video.html')


@video_blueprint.route('/', methods=['GET'])
def get_videos():
    videos = Video.query.all()
    video_list = [serialize_video(video) for video in videos]
    return jsonify(video_list)


@video_blueprint.route('/team/<int:team_id>', methods=['GET'])
def get_videos_by_team(team_id):
    videos = Video.query.filter((Video.team_one_id == team_id) | (Video.team_two_id == team_id)).all()
    video_list = [serialize_video(video) for video in videos]
    return jsonify(video_list)


@video_blueprint.route('/tournament/<int:tournament_id>', methods=['GET'])
def get_videos_by_tournament(tournament_id):
    videos = Video.query.filter_by(tournament_id=tournament_id).all()
    video_list = [serialize_video(video) for video in videos]
    return jsonify(video_list)


@video_blueprint.route('/tournament/<int:tournament_id>/team/<int:team_id>', methods=['GET'])
def get_videos_by_tournament_and_team(tournament_id, team_id):
    videos = Video.query.filter_by(tournament_id=tournament_id).filter(
        (Video.team_one_id == team_id) | (Video.team_two_id == team_id)
    ).all()
    video_list = [serialize_video(video) for video in videos]
    return jsonify(video_list)
