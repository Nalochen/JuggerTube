from flask import Blueprint, request, url_for, redirect, render_template, jsonify, flash
from flask_login import login_required, current_user

from juggertube.game_system_enum import GameSystem
from juggertube.models import Video, db, Tournament, Team, Channel

from juggertube.video_type_enum import VideoType
from juggertube.webforms import VideoForm

video_blueprint = Blueprint('videos', __name__, template_folder='templates')


def serialize_video(video):
    return {
        'video_id': video.id,
        'channel': video.channel.name,
        'category': video.category.value,
        'name': video.name,
        'link': video.link,
        'tournament': video.tournament.name if video.tournament else None,
        'team_one': video.team_one.name if video.team_one else None,
        'team_two': video.team_two.name if video.team_two else None,
        'upload_date': video.upload_date.strftime('%Y-%m-%d'),
        'date_of_recording': video.date_of_recording.strftime('%Y-%m-%d') if video.date_of_recording else None,
        'game_system': video.game_system.value if video.game_system else None,
        'weapon_type': video.weapon_type if video.weapon_type else None,
        'topic': video.topic if video.topic else None,
        'guests': video.guests if video.guests else None,
        'comments': video.comments if video.comments else None,
    }


@video_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add_video():
    form = VideoForm(request.form)
    form.tournament.choices = [(tournament.id, tournament.name) for tournament in Tournament.query.all()]
    form.team_one.choices = [(team.id, team.name) for team in Team.query.all()]
    form.team_two.choices = [(team.id, team.name) for team in Team.query.all()]
    form.channel.choices = [(channel.id, channel.name) for channel in Channel.query.all()]

    if request.method == 'POST':
        name = form.name.data
        channel = Channel.query.filter_by(id=form.channel.data).first()
        link = form.link.data
        category = VideoType[form.category.data]
        upload_date = form.upload_date.data
        tournament = Tournament.query.filter_by(id=form.tournament.data).first()
        team_one = Team.query.filter_by(id=form.team_one.data).first()
        team_two = Team.query.filter_by(id=form.team_two.data).first()
        date_of_recording = form.date_of_recording.data
        game_system = form.game_system.data
        weapon_type = form.weapon_type.data
        topic = form.topic.data
        guests = form.guests.data
        comments = form.comments.data

        if game_system == '':
            game_system = None
        else:
            game_system = GameSystem[game_system]

        new_video = Video(name=name, channel_id=channel.id, channel=channel, link=link, category=category,
                          tournament_id=tournament.id, tournament=tournament, team_one_id=team_one.id, team_one=team_one,
                          team_two_id=team_two.id, team_two=team_two, upload_date=upload_date,
                          date_of_recording=date_of_recording, game_system=game_system, weapon_type=weapon_type,
                          topic=topic, guests=guests, comments=comments)

        try:
            db.session.add(new_video)
            db.session.commit()
            return redirect(url_for('general.index'))
        except Exception as e:
            flash('something went wrong, please try again', str(e))

    return render_template('video.html', form=form)


@video_blueprint.route('/edit/<int:video_id>', methods=['GET', 'POST'])
@login_required
def edit_video(video_id):
    video = Video.query.filter_by(id=video_id).first()
    form = VideoForm(video=request.form)
    form.tournament.choices = [(tournament.id, tournament.name) for tournament in Tournament.query.all()]
    form.team_one.choices = [(team.id, team.name) for team in Team.query.all()]
    form.team_two.choices = [(team.id, team.name) for team in Team.query.all()]
    form.channel.choices = [(channel.id, channel.name) for channel in Channel.query.all()]

    if request.method == 'GET':
        form.name.data = video.name
        form.channel.data = video.channel
        form.link.data = video.link
        form.category.data = video.category.value
        form.upload_date.data = video.upload_date
        form.tournament.data = video.tournament
        form.team_one.data = video.team_one
        form.team_two.data = video.team_two
        form.date_of_recording.data = video.date_of_recording if video.date_of_recording else ''
        form.game_system.data = video.game_system.value if video.game_system else ''
        form.weapon_type.data = video.weapon_type
        form.topic.data = video.topic
        form.guests.data = video.guests
        form.comments.data = video.comments

    if form.validate_on_submit():
        video.name = form.name.data
        video.channel_id = form.channel.data
        video.link = form.link.data
        video.category = form.category.data
        video.upload_date = form.upload_date.data
        video.tournament_id = form.tournament.data
        video.team_one_id = form.team_one.data
        video.team_one = Team.query.filter_by(id=form.team_one.data).first()
        video.team_two_id = form.team_two.data
        video.team_two = Team.query.filter_by(id=form.team_two.data).first()
        video.date_of_recording = form.date_of_recording.data
        if form.game_system.data == '':
            video.game_system = None
        else:
            video.game_system = GameSystem[form.game_system.data]
        video.weapon_type = form.weapon_type.data
        video.topic = form.topic.data
        video.guests = form.guests.data
        video.comments = form.comments.data

        try:
            db.session.commit()
            flash('Object updated successfully', 'success')
        except Exception as e:
            db.session.rollback()
            flash('something went wrong, please try again', str(e))

        return redirect(url_for('general.index'))

    return render_template('video.html', form=form, video=video)


@video_blueprint.route('/delete/<int:video_id>', methods=['GET'])
@login_required
def delete_video(video_id):
    video = Video.query.filter_by(id=video_id).first()
    name = video.name
    try:
        db.session.delete(video)
        db.session.commit()
        flash(f'Video {name} deleted')
    except Exception as e:
        flash('something went wrong, please try again', str(e))

    return redirect(url_for('general.index'))


@video_blueprint.route('/', methods=['GET'])
def get_videos():
    videos = Video.query.all()
    video_list = [serialize_video(video) for video in videos]
    return jsonify(video_list)


@video_blueprint.route('/team/<int:team_id>', methods=['GET'])
def get_videos_by_team(team_id):
    videos = Video.query.filter((Video.team_one == team_id) | (Video.team_two == team_id)).all()
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
        (Video.team_one == team_id) | (Video.team_two == team_id)
    ).all()
    video_list = [serialize_video(video) for video in videos]
    return jsonify(video_list)


@video_blueprint.route('/period/<string:beginning>/<string:ending>', methods=['GET'])
def get_videos_by_period(beginning, ending):
    videos = Video.query.filter(
        Video.date_of_recording > beginning, Video.date_of_recording < ending
    ). all()
    video_list = [serialize_video(video) for video in videos]
    return jsonify(video_list)
