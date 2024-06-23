from flask import Blueprint, request, jsonify
from flask_login import login_required

from juggertube.api.serializing import serialize_channel, serialize_user, serialize_choices
from juggertube.models import Channel, db, User

channel_api_blueprint = Blueprint('api/channels', __name__)


@channel_api_blueprint.route('/add', methods=['POST'])
def add_channel():
    post_data = request.args
    name = post_data.get('name')
    link = post_data.get('link')
    owners = post_data.get('owners')

    if not name or not link:
        return jsonify({'error': 'Name and link are required'}), 400

    existing_channel = Channel.query.filter_by(name=name).first()
    if existing_channel:
        return jsonify(serialize_channel(existing_channel), 'channel already exists'), 400

    owner_ids = []
    if owners:
        try:
            owner_ids = [int(owner_id) for owner_id in owners.split(',')]
        except ValueError:
            jsonify({'error': 'Owners must be comma-separated list of integers'})
    else:
        owner_ids = []

    valid_owners = []
    for owner_id in owner_ids:
        owner = User.query.filter_by(id=owner_id).first()
        if owner:
            valid_owners.append(owner)
        else:
            return jsonify({'error': f'Owner with ID {owner_id} not found'}), 400

    new_channel = Channel(name=post_data["name"], link=post_data["link"], owners=valid_owners)

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
    if not channel:
        return jsonify({'error': 'channel not found'}), 404

    if request.method == 'GET':
        return jsonify(serialize_channel(channel))

    if request.method == 'POST':
        post_data = request.args
        name = post_data.get('name')
        link = post_data.get('link')
        owners = post_data.get('owners')

        if not name or not link:
            return jsonify({'error': 'Name and link are required'}), 400

        owner_ids = []
        if owners:
            try:
                owner_ids = [int(owner_id) for owner_id in owners.split(',')]
            except ValueError:
                jsonify({'error': 'Owners must be comma-separated list of integers'})
        else:
            owner_ids = []

        valid_owners = []
        for owner_id in owner_ids:
            owner = User.query.filter_by(id=owner_id).first()
            if owner:
                valid_owners.append(owner)
            else:
                return jsonify({'error': f'Owner with ID {owner_id} not found'}), 400

        channel.name = name
        channel.link = link
        channel.owners = valid_owners

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


@channel_api_blueprint.route('/owner-choices', methods=['GET'])
def get_owner_choices():
    owners = [(user.id, user.username) for user in User.query.all()]
    owner_choices = [serialize_choices(user) for user in owners]
    return jsonify(owner_choices)
