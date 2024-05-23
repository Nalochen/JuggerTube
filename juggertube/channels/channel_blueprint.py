from flask import Blueprint, request, url_for, redirect, render_template, jsonify

from models import Channel, db

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
        name = request.form['name']
        link = request.form['link']
        new_channel = Channel(name=name, link=link)
        db.session.add(new_channel)
        db.session.commit()
        return redirect(url_for('general.index'))
    return render_template('add_channel.html')


@channel_blueprint.route('/', methods=['GET'])
def get_channels():
    channels = Channel.query.all()
    channel_list = [serialize_channel(channel) for channel in channels]
    return jsonify(channel_list)

