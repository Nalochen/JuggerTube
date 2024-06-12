from flask import Blueprint, request, url_for, redirect, render_template, jsonify, flash
from flask_login import login_required, current_user

from juggertube.models import Team, db, Channel, User
from juggertube.video_type_enum import VideoType

from juggertube.webforms import TeamForm, ChannelForm

channel_blueprint = Blueprint('channels', __name__, template_folder='templates')


def serialize_channel(channel):
    return {
        'channel_id': channel.channel_id,
        'name': channel.name,
        'link': channel.link,
        'owner': channel.owner,
    }


@channel_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add_channel():
    form = ChannelForm()
    if request.method == 'POST':
        name = form.name.data
        link = form.link.data
        owner = form.owner.data
        new_channel = Channel(name=name, link=link)
        try:
            db.session.add(new_channel)

            if owner:
                db.session.flush()
                owner = db.session.query(User).get(owner.id)

                owner.channels.append(new_channel)
                new_channel.owners.append(owner)

            db.session.commit()

            return redirect(url_for('general.index'))
        except Exception as e:
            flash('Error! looks like there was a problem... please try again!', str(e))
            return render_template('channel.html', form=form)
    form.owner.choices = [(owner.id, owner.name) for owner in User.query.all()]
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

            try:
                if channel.owner:
                    db.session.flush()
                    owner = db.session.query(User).get(channel.owner.id)

                    owner.channels.append(channel)
                    channel.owners.append(owner)

                db.session.commit()
                return redirect(url_for('general.index'))
            except Exception as e:
                flash('Error! Looks like your inputs are not valid, please check if '
                      'you wrote something in every input field', str(e))

        if current_user:
            form.name.data = channel.name
            form.link.data = channel.link
            form.owner.data = channel.owner
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
