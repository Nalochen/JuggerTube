from flask import Blueprint, request, render_template, current_app
from flask_login import login_required

from juggertube.api.channel_api_blueprint import channel_api_blueprint
from juggertube.webforms import ChannelForm

channel_blueprint = Blueprint('channels', __name__, template_folder='templates')


@channel_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add_channel():
    with current_app.test_client() as client:
        form = ChannelForm(request.form)

        if request.method == 'GET':
            return render_template('post-channel.html', form=form)

        if request.method == 'POST':
            post_data = {
                "name": form.name.data,
                "link": form.link.data
            }
            response = client.post('/api/channels/add', query_string=post_data)
            data = response.get_json()
            return data


@channel_blueprint.route('/edit/<int:channel_id>', methods=['GET', 'POST'])
@login_required
def edit_channel(channel_id):
    with current_app.test_client() as client:
        form = ChannelForm(team=request.form)

        if request.method == 'GET':
            response = channel_api_blueprint.edit_channel(channel_id)
            data = response.get_json()

            form.name.data = data['name']
            form.link.data = data['link']

            return render_template('post-channel.html', form=form)

        if request.method == 'POST':
            if form.validate_on_submit():
                post_data = {
                    "name": form.name.data,
                    "link": form.link.data,
                }

                response = client.post(f'/api/channels/edit/{channel_id}', query_string=post_data)
                data = response.get_json()
                return data
            else:
                return render_template('post-channel.html', form=form)


@channel_blueprint.route('/delete/<int:channel_id>', methods=['GET'])
@login_required
def delete_channel(channel_id):
    response = channel_api_blueprint.delete_channel(channel_id)
    deleted_channel = response.get_json
    return deleted_channel


@channel_blueprint.route('/', methods=['GET'])
def get_channels():
    response = channel_api_blueprint.get_channels()
    channels_list = response.get_json()
    return render_template('show-channels.html', team_list=channels_list)
