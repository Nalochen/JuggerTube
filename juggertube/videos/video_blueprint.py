import flask_login
from flask import Blueprint, request, url_for, redirect, render_template, jsonify, flash
from flask_login import login_required, current_user

from juggertube.models import Video, db, Tournament, Team

from juggertube.tournaments.tournament_blueprint import get_tournament_by_period
from juggertube.webforms import VideoForm

video_blueprint = Blueprint('videos', __name__, template_folder='templates')


def serialize_video(video):
    return {
        'video_id': video.video_id,
        'name': video.name,
        'user_id': video.user_id,
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
    form = VideoForm()
    if request.method == 'POST':
        name = form.name.data
        user_id = flask_login.current_user.user_id
        link = form.link.data
        tournament_id = form.tournament.data
        team_one_id = form.team_one.data
        team_two_id = form.team_two.data
        upload_date = form.date.data
        comments = form.comments.data

        new_video = Video(name=name, user_id=user_id, link=link,
                          tournament_id=tournament_id, team_one_id=team_one_id,
                          team_two_id=team_two_id, upload_date=upload_date,
                          comments=comments)
        db.session.add(new_video)
        db.session.commit()
        return redirect(url_for('general.index'))

    form.tournament.choices = [(tournament.tournament_id, tournament.name) for tournament in Tournament.query.all()]
    form.team_one.choices = [(team.team_id, team.name) for team in Team.query.all()]
    form.team_two.choices = [(team.team_id, team.name) for team in Team.query.all()]
    return render_template('video.html', form=form)


@video_blueprint.route('/edit/<int:video_id>', methods=['GET', 'POST'])
@login_required
def edit_video(video_id):
    video = Video.query.get_or_404(video_id)
    form = VideoForm()

    if form.validate_on_submit():
        video.name = form.name.data
        video.user_id = flask_login.current_user.user_id
        video.link = form.link.data
        video.tournament_id = form.tournament.data
        video.team_one_id = form.team_one.data
        video.team_two_id = form.team_two.data
        video.upload_date = form.date.data
        video.comments = form.comments.data
        db.session.commit()

        form.tournament.choices = [(tournament.id, tournament.name) for tournament in Tournament.query.all()]
        form.team_one.choices = [(team.id, team.name) for team in Team.query.all()]
        form.team_two.choices = [(team.id, team.name) for team in Team.query.all()]

        return redirect(url_for('general.index'))

    if current_user.id == video.user_id:
        form.name.data = video.name
        form.link.data = video.link
        form.tournament.data = video.tournament_id
        form.team_one.data = video.team_one_id
        form.team_two.data = video.team_two_id
        form.date.data = video.upload_date
        form.comments.data = video.comments

        form.tournament.choices = [(tournament.id, tournament.name) for tournament in Tournament.query.all()]
        form.team_one.choices = [(team.id, team.name) for team in Team.query.all()]
        form.team_two.choices = [(team.id, team.name) for team in Team.query.all()]

        return render_template('video.html', form=form)

    else:
        return render_template('video.html', form=form)


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
