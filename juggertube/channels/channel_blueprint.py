from flask import Blueprint, request, url_for, redirect, render_template, jsonify

from models import Channel, db
from auth.auth_blueprint import is_user_logged_in

channel_blueprint = Blueprint('channels', __name__, template_folder='templates')


def serialize_channel(channel):
    return {
        'channel_id': channel.channel_id,
        'name': channel.name,
        'link': channel.link,
    }


@channel_blueprint.route('/add', methods=['GET', 'POST'])
def add_channel():
    if request.method == 'POST':
        if is_user_logged_in():
            name = request.form['name']
            link = request.form['link']
            new_channel = Channel(name=name, link=link)
            db.session.add(new_channel)
            db.session.commit()
            return redirect(url_for('general.index'))
        return redirect(url_for('auth.login_user'))
    return render_template('add_channel.html')


@channel_blueprint.route('/edit/<int:channel_id>', methods=['GET', 'POST'])
def edit_channel(channel_id):
    if request.method == 'POST':
        if is_user_logged_in():
            channel = Channel.query.filter_by(channel_id=channel_id).all()

            name = request.form['name']
            link = request.form['link']

            if name:
                channel.name = name
            if link:
                channel.link = link

            db.session.commit()
            return redirect(url_for('general.index'))
        return redirect(url_for('auth.login_user'))
    return render_template('edit_channel.html')


@channel_blueprint.route('/delete/<int:channel_id>', methods=['POST'])
def delete_channel(channel_id):
    if is_user_logged_in():
        channel = Channel.query.filter_by(channel_id=channel_id).all()

        name = channel.name

        db.session.delete(channel)
        db.session.commit()
        return f'<h1>Channel {name} deleted<h1>'
    return redirect(url_for('auth.login_user'))


@channel_blueprint.route('/', methods=['GET'])
def get_channels():
    channels = Channel.query.all()
    channel_list = [serialize_channel(channel) for channel in channels]
    return jsonify(channel_list)

