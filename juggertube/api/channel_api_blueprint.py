from flask import Blueprint, request, jsonify
from flask_login import login_required

from juggertube.api.serializing import serialize_channel
from juggertube.models import Channel, db

channel_api_blueprint = Blueprint('api/channels', __name__)


@channel_api_blueprint.route('/add', methods=['POST'])
def add_channel():
    post_data = request.args
    new_channel = Channel(name=post_data["name"], link=post_data["link"])

    existing_channel = Channel.query.filter_by(name=new_channel.name).first()
    if existing_channel:
        return jsonify(serialize_channel(existing_channel), 'channel already exists'), 400
    else:
        try:
            db.session.add(new_channel)
            db.session.commit()

            channel = serialize_channel(Channel.query.filter_by(name=new_channel.name).first())
            return jsonify(channel), 200

        except Exception as e:
            return jsonify(str(e)), 400


@channel_api_blueprint.route('/edit/<int:channel_id>', methods=['GET', 'POST'])
@login_required
def edit_channel(channel_id):
    channel = Channel.query.filter_by(id=channel_id).first()

    if request.method == 'GET':
        return jsonify(serialize_channel(channel))

    if request.method == 'POST':
        post_data = request.args
        channel.name = post_data["name"]
        channel.link = post_data["link"]

        try:
            db.session.commit()

            edited_channel = serialize_channel(Channel.query.filter_by(id=channel.id).first())
            return jsonify(edited_channel), 200
        except Exception as e:
            return jsonify(str(e)), 400


@channel_api_blueprint.route('/delete/<int:channel_id>', methods=['GET'])
@login_required
def delete_channel(channel_id):
    channel = Channel.query.filter_by(id=channel_id).first()

    name = channel.name

    try:
        db.session.delete(channel)
        db.session.commit()

        return jsonify(f'Channel {name} deleted'), 200

    except Exception as e:
        return jsonify(str(e)), 400


@channel_api_blueprint.route('/', methods=['GET'])
def get_channels():
    channels = Channel.query.all()
    channel_list = [serialize_channel(channel) for channel in channels]
    return jsonify(channel_list)
