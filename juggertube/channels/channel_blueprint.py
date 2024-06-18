from flask import Blueprint, request, url_for, redirect, render_template, jsonify, flash
from flask_login import login_required, current_user

from juggertube.models import db, Channel, User

from juggertube.webforms import ChannelForm

channel_blueprint = Blueprint('channels', __name__, template_folder='templates')


def serialize_channel(channel):
    return {
        'channel_id': channel.id,
        'name': channel.name,
        'link': channel.link,
    }


@channel_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add_channel():
    form = ChannelForm(request.form)
    form.owner.choices = [(owner.id, owner.username) for owner in User.query.all()]
    if request.method == 'POST':
        name = form.name.data
        link = form.link.data
        owner = User.query.filter_by(id=form.owner.data).first()
        new_channel = Channel(name=name, link=link)
        try:
            owner.channels.append(new_channel)
            db.session.add(new_channel)
            db.session.commit()

            return redirect(url_for('general.index'))
        except Exception as e:
            flash('Error! looks like there was a problem... please try again!', str(e))
            return render_template('post-channel.html', form=form)
    form.owner.choices = [(owner.id, owner.username) for owner in User.query.all()]
    return render_template('post-channel.html', form=form)


@channel_blueprint.route('/edit/<int:channel_id>', methods=['GET', 'POST'])
@login_required
def edit_channel(channel_id):
    channel = Channel.query.filter_by(id=channel_id).first()
    form = ChannelForm(channel=request.form)
    form.owner.choices = [(owner.id, owner.username) for owner in User.query.all()]
    if request.method == 'GET':
        form.name.data = channel.name
        form.link.data = channel.link
        form.owner.data = channel.owners

    if form.validate_on_submit():
        channel.name = form.name.data
        channel.link = form.link.data
        try:
            db.session.commit()
            return redirect(url_for('general.index'))
        except Exception as e:
            db.session.rollback()
            flash('something went wrong, please try again', str(e))

    return render_template('post-channel.html', form=form)


@channel_blueprint.route('/delete/<int:channel_id>', methods=['GET'])
@login_required
def delete_channel(channel_id):
    channel = Channel.query.filter_by(id=channel_id).first()

    name = channel.name

    try:
        db.session.delete(channel)
        db.session.commit()
        flash(f'channel {name} deleted')
    except Exception as e:
        flash('something went wrong please try again', str(e))

    return redirect(url_for('general.index'))


@channel_blueprint.route('/', methods=['GET'])
def get_channels():
    channels = Channel.query.all()
    channel_list = [serialize_channel(channel) for channel in channels]
    return render_template('show-channels.html', channel_list=jsonify(channel_list))
