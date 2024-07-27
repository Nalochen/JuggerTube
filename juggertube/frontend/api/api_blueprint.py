from flask import Blueprint, request, render_template, current_app
from flask_login import login_required

from juggertube.api import api_blueprint
from juggertube.webforms import APIDeviceForm

api_ui_blueprint = Blueprint('api_ui', __name__, template_folder='templates')


@api_ui_blueprint.route('/add-device', methods=['GET', 'POST'])
@login_required
def add_device():
    with current_app.test_client() as client:
        form = APIDeviceForm(request.form)

        if request.method == 'GET':
            return render_template('post-device.html', form=form)

        if request.method == 'POST':
            post_data = {
                "device_name": form.device_name.data,
            }

            response = client.post('/api/add_device', query_string=post_data)
            data = response.get_json()
            return data


@api_ui_blueprint.route('/devices', methods=['GET'])
def get_devices():
    response = api_blueprint.get_devices()
    device_list = response.get_json()
    return render_template('show-devices.html', device_list=device_list)
