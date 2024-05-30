from flask import Blueprint, request, url_for, redirect, render_template, jsonify, flash
from flask_login import login_required

from models import Video, User, Team, Tournament, Channel, db

from tournaments.tournament_blueprint import get_tournament_by_period

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
        'upload_date': video.upload_date.strftime('%Y-%m-%d'),
        'comments': video.comments,
    }


@video_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
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
        new_video = Video(name=name, channel_id=channel_id, link=link,
                          tournament_id=tournament_id, team_one_id=team_one_id,
                          team_two_id=team_two_id, upload_date=upload_date,
                          comments=comments)
        db.session.add(new_video)
        db.session.commit()
        return redirect(url_for('general.index'))
    return render_template('add_video.html')


@video_blueprint.route('/edit/<int:video_id>', methods=['GET', 'POST'])
@login_required
def edit_video(video_id):
    if request.method == 'POST':
        video = Video.query.get(video_id)

        name = request.form['name']
        channel_id = request.form['channel_id']
        link = request.form['link']
        tournament_id = request.form['tournament_id']
        team_one_id = request.form['team_one_id']
        team_two_id = request.form['team_two_id']
        upload_date = request.form['upload_date']
        comments = request.form['comments']

        if name:
            video.name = name
        if channel_id:
            video.channel_id = channel_id
        if link:
            video.link = link
        if tournament_id:
            video.tournament_id = tournament_id
        if team_one_id:
            video.team_one_id = team_one_id
        if team_two_id:
            video.team_two_id = team_two_id
        if upload_date:
            video.upload_date = upload_date
        if comments:
            video.comments = comments

        db.session.commit()
        return redirect(url_for('general.index'))
    return render_template('edit_video.html')


@video_blueprint.route('/delete/<int:video_id>', methods=['GET'])
@login_required
def delete_video(video_id):
    video = Video.query.get(video_id).first()

    name = video.name

    db.session.delete(video)
    db.session.commit()
    return f'<h1>Video {name} deleted<h1>'


@video_blueprint.route('/', methods=['GET'])
def get_videos():
    videos = Video.query.all()
    video_list = [serialize_video(video) for video in videos]
    print('stuff')
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


@video_blueprint.route('/period/<string:beginning>/<string:ending>', methods=['GET'])
def get_videos_by_period(beginning, ending):
    try:
        tournaments = get_tournament_by_period(beginning, ending)

        videos = []
        for tournament in tournaments:
            tournament_videos = Video.query.filter_by(tournament_id=tournament.tournament_id).all()
            videos.extend(tournament_videos)

        video_list = [serialize_video(video) for video in videos]
        return jsonify(video_list)

    except Exception as e:
        return jsonify({'error': str(e)}), 400
