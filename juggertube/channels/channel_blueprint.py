from flask import Blueprint, request, url_for, redirect, render_template, jsonify, flash
from flask_login import login_required, current_user

from juggertube.models import Team, db, Channel
from juggertube.video_type_enum import VideoType

from juggertube.webforms import TeamForm, ChannelForm

channel_blueprint = Blueprint('channels', __name__, template_folder='templates')


def serialize_channel(channel):
    return {
        'channel_id': channel.channel_id,
        'name': channel.name,
        'link': channel.link,
        'owner': channel.owner,
        'team': channel.team,
        'content_type': channel.content_type,
    }


@channel_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add_channel():
    form = ChannelForm()
    if request.method == 'POST':
        name = form.name.data
        link = form.link.data
        owner = form.owner.data
        team = form.team.data
        content_type = form.content_type.data
        new_channel = Channel(name=name, link=link, owner=owner, team=team, content_type=content_type)
        try:
            db.session.add(new_channel)
            db.session.commit()
            return redirect(url_for('general.index'))
        except Exception as e:
            flash('Error! looks like there was a problem... please try agin!', str(e))
            return render_template('channel.html', form=form)
    form.content_type.choices = VideoType
    return render_template('channel.html', form=form)


@channel_blueprint.route('/edit/<int:channel_id>', methods=['GET', 'POST'])
@login_required
def edit_channel(channel_id):
    form = ChannelForm()
    if request.method == 'POST':
        channel = Channel.query.get_or_404(channel_id=channel_id)

        if form.validate_on_submit():
            channel.name = form.name.data
            channel.link = form.link.data
            channel.owner = form.owner.data
            channel.team_id = form.team.data
            channel.content_type = form.content_type.data

            try:
                db.session.commit()
                return redirect(url_for('general.index'))
            except Exception as e:
                flash('Error! Looks like your inputs are not valid, please check if '
                      'you wrote something in every input field', str(e))

        if current_user:
            form.name.data = channel.name
            form.link.data = channel.link
            form.owner.data = channel.owner
            form.team.data = channel.team_id
            form.content_type.data = channel.content_type
            return render_template('channel.html', form=form)

        else:
            return redirect(url_for('general.index'))

    form.content_type.choices = VideoType


@channel_blueprint.route('/delete/<int:channel_id>', methods=['GET'])
@login_required
def delete_channel(channel_id):
    channel = Channel.query.filter_by(channel_id=channel_id).first()

    name = channel.name

    try:
        db.session.delete(channel)
        db.session.commit()
        flash(f'channel {name} deleted')
    except Exception as e:
        flash('something went wrong please try again', str(e))


@channel_blueprint.route('/', methods=['GET'])
def get_channels():
    channels = Channel.query.all()
    channel_list = [serialize_channel(channel) for channel in channels]
    return jsonify(channel_list)
