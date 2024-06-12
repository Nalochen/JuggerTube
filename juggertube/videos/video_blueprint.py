from flask import Blueprint, request, url_for, redirect, render_template, jsonify, flash
from flask_login import login_required, current_user

from juggertube.game_system_enum import GameSystem
from juggertube.models import Video, db, Tournament, Team, Channel

from juggertube.video_type_enum import VideoType
from juggertube.webforms import VideoForm

video_blueprint = Blueprint('videos', __name__, template_folder='templates')


def serialize_video(video):
    return {
        'video_id': video.video_id,
        'channel_id': video.channel_id,
        'category': video.category,
        'name': video.name,
        'user_id': video.user_id,
        'link': video.link,
        'tournament_id': video.tournament_id,
        'team_one_id': video.team_one_id,
        'team_two_id': video.team_two_id,
        'upload_date': video.upload_date.strftime('%Y-%m-%d'),
        'date_of_recording': video.date_of_recording.strftime('%Y-%m-%d'),
        'game_system': video.game_system,
        'weapon_type': video.weapon_type,
        'topic': video.topic,
        'guests': video.guests,
        'comments': video.comments,
    }


@video_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add_video():
    form = VideoForm()
    if request.method == 'POST':
        name = form.name.data
        channel_id = form.channel.data
        link = form.link.data
        category = form.category.data
        upload_date = form.upload_date.data
        tournament_id = form.tournament.data
        team_one_id = form.team_one.data
        team_two_id = form.team_two.data
        date_of_recording = form.date_of_recording.data
        game_system = form.game_system.data
        weapon_type = form.weapon_type.data
        topic = form.topic.data
        guests = form.guests.data
        comments = form.comments.data

        new_video = Video(name=name, channel_id=channel_id, link=link, category=category,
                          tournament_id=tournament_id, team_one_id=team_one_id,
                          team_two_id=team_two_id, upload_date=upload_date, date_of_recording=date_of_recording,
                          game_system=game_system, weapon_type=weapon_type, topic=topic, guests=guests,
                          comments=comments)

        try:
            db.session.add(new_video)
            db.session.commit()
            return redirect(url_for('general.index'))
        except Exception as e:
            flash('something went wrong, please try again', str(e))

    form.tournament.choices = [(tournament.id, tournament.name) for tournament in Tournament.query.all()]
    form.team_one.choices = [(team.id, team.name) for team in Team.query.all()]
    form.team_two.choices = [(team.id, team.name) for team in Team.query.all()]
    form.channel.choices = [(channel.id, channel.name) for channel in Channel.query.all()]
    form.game_system.choices = GameSystem
    form.category.choices = VideoType
    return render_template('video.html', form=form)


@video_blueprint.route('/edit/<int:video_id>', methods=['GET', 'POST'])
@login_required
def edit_video(video_id):
    video = Video.query.get_or_404(video_id)
    form = VideoForm()

    if form.validate_on_submit():
        video.name = form.name.data
        video.channel_id = form.channel.data
        video.link = form.link.data
        video.category = form.category.data
        video.upload_date = form.upload_date.data
        video.tournament_id = form.tournament.data
        video.team_one_id = form.team_one.data
        video.team_two_id = form.team_two.data
        video.date_of_recording = form.date_of_recording.data
        video.game_system = form.game_system.data
        video.weapon_type = form.weapon_type.data
        video.topic = form.topic.data
        video.guests = form.guests.data
        video.comments = form.comments.data
        try:
            db.session.commit()
        except Exception as e:
            flash('something went wrong, please try again', str(e))

        form.tournament.choices = [(tournament.id, tournament.name) for tournament in Tournament.query.all()]
        form.team_one.choices = [(team.id, team.name) for team in Team.query.all()]
        form.team_two.choices = [(team.id, team.name) for team in Team.query.all()]
        form.channel.choices = [(channel.id, channel.name) for channel in Channel.query.all()]
        form.game_system.choices = GameSystem
        form.category.choices = VideoType

        return redirect(url_for('general.index'))

    if current_user.id == video.user_id:
        form.name.data = video.name
        form.channel.data = video.channel_id
        form.link.data = video.link
        form.category.data = video.category
        form.upload_date.data = video.upload_date
        form.tournament.data = video.tournament_id
        form.team_one.data = video.team_one_id
        form.team_two.data = video.team_two_id
        form.date_of_recording.data = video.date_of_recording
        form.game_system.data = video.game_system
        form.weapon_type.data = video.weapon_type
        form.topic.data = video.topic
        form.guests.data = video.guests
        form.comments.data = video.comments

        form.tournament.choices = [(tournament.id, tournament.name) for tournament in Tournament.query.all()]
        form.team_one.choices = [(team.id, team.name) for team in Team.query.all()]
        form.team_two.choices = [(team.id, team.name) for team in Team.query.all()]
        form.channel.choices = [(channel.id, channel.name) for channel in Channel.query.all()]
        form.game_system.choices = GameSystem
        form.category.choices = GameSystem

        return render_template('video.html', form=form)

    else:
        return render_template('video.html', form=form)


@video_blueprint.route('/delete/<int:video_id>', methods=['GET'])
@login_required
def delete_video(video_id):
    video = Video.query.get(video_id).first()

    name = video.name

    try:
        db.session.delete(video)
        db.session.commit()
        flash(f'Video {name} deleted')
    except Exception as e:
        flash('something went wrong, please try again', str(e))


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


@video_blueprint.route('/period/<string:beginning>/<string:ending>', methods=['GET'])
def get_videos_by_period(beginning, ending):
    videos = Video.query.filter(
        Video.date_of_recording > beginning, Video.date_of_recording < ending
    ). all()
    video_list = [serialize_video(video) for video in videos]
    return jsonify(video_list)
