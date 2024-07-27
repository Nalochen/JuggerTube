import flask_login
from flask import Blueprint, request, jsonify
from flask_login import login_required

from juggertube.api.serializing import serialize_device
from juggertube.models import Device

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/add-device', methods=['POST'])
@login_required
def add_device():
    post_data = request.args
    device_name = post_data.get('device_name')

    if Device.find_by_name(device_name):
        return {'message': f'A device with the name "{device_name}" already exists'}, 400

    owner = flask_login.current_user

    new_device = Device(device_name=device_name, user_id=owner.id)

    try:
        new_device.save_to_db()

        device = Device.query.filter_by(device_name=new_device.device_name).first().json()
        return jsonify(device), 200

    except Exception as e:
        return jsonify(str(e)), 400


@api_blueprint.route('/', methods=['GET'])
def get_devices():
    devices = Device.query.all()
    device_list = [serialize_device(device) for device in devices]
    return jsonify(device_list)
