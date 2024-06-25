from flask import Blueprint, request, render_template, current_app
from flask_login import login_required

from juggertube.api import video_api_blueprint
from juggertube.video_type_enum import VideoType

from juggertube.webforms import VideoForm

video_blueprint = Blueprint('videos', __name__, template_folder='templates')


@video_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add_video():
    with current_app.test_client() as client:
        form = VideoForm(request.form)
        response = video_api_blueprint.get_form_choices()
        data = response.get_json()

        form.tournament.choices = [(tournament['choice_id'], tournament['name']) for tournament in data["tournament_choices"]]
        form.team_one.choices = [(team['choice_id'], team['name']) for team in data["team_choices"]]
        form.team_two.choices = [(team['choice_id'], team['name']) for team in data["team_choices"]]
        form.channel.choices = [(channel['choice_id'], channel['name']) for channel in data["channel_choices"]]

        if request.method == 'GET':
            return render_template('post-video.html', form=form)

        if request.method == 'POST':
            post_data = {
                "name": form.name.data,
                "channel_id": form.channel.data,
                "link": form.link.data,
                "category": form.category.data,
                "upload_date": form.upload_date.data.strftime('%Y-%m-%dT23-00-00'),
                "tournament_id": form.tournament.data,
                "team_one_id": form.team_one.data,
                "team_two_id": form.team_two.data,
                "date_of_recording": form.date_of_recording.data.strftime('%Y-%m-%dT23-00-00'),
                "game_system": form.game_system.data,
                "weapon_type": form.weapon_type.data,
                "topic": form.topic.data,
                "guests": form.guests.data,
                "comments": form.comments.data
            }

            response = client.post('/api/videos/add', query_string=post_data)
            data = response.get_json()
            return data


@video_blueprint.route('/edit/<int:video_id>', methods=['GET', 'POST'])
@login_required
def edit_video(video_id):
    with current_app.test_client() as client:
        form = VideoForm(video=request.form)
        choice_response = video_api_blueprint.get_form_choices()
        choice_data = choice_response.get_json()

        form.tournament.choices = choice_data["tournament_choices"]
        form.team_one.choices = choice_data["team_choices"]
        form.team_two.choices = choice_data["team_choices"]
        form.channel.choices = choice_data["channel_choices"]

        if request.method == 'GET':
            response = video_api_blueprint.edit_video(video_id)
            data = response.get_json()

            form.name.data = data["name"]
            form.channel.data = data["channel"]
            form.link.data = data["link"]
            form.category.data = data["category"].value
            form.upload_date.data = data["upload_date"]
            form.tournament.data = data["tournament"]
            form.team_one.data = data["team_one"]
            form.team_two.data = data["team_two"]
            form.date_of_recording.data = data["date_of_recording"] if data["date_of_recording"] else ''
            form.game_system.data = data["game_system"].value if data["game_system"] else ''
            form.weapon_type.data = data["weapon_type"]
            form.topic.data = data["topic"]
            form.guests.data = data["guests"]
            form.comments.data = data["comments"]

            return render_template('post-video.html', form=form)

        if request.method == 'POST':
            if form.validate_on_submit():

                post_data = {
                    "name": form.name.data,
                    "channel_id": form.channel.data,
                    "link": form.link.data,
                    "category": form.category.data,
                    "upload_date": form.upload_date.data,
                    "tournament_id": form.tournament.data,
                    "team_one_id": form.team_one.data,
                    "team_two_id": form.team_two.data,
                    "date_of_recording": form.date_of_recording.data,
                    "game_system": form.game_system.data,
                    "weapon_type": form.weapon_type.data,
                    "topic": form.topic.data,
                    "guests": form.guests.data,
                    "comments": form.comments.data,
                }

                response = client.post(f'/api/videos/edit/{video_id}', query_string=post_data)
                data = response.get_json()
                return data
            else:
                return render_template('post-video.html', form=form)


@video_blueprint.route('/delete/<int:video_id>', methods=['GET'])
@login_required
def delete_video(video_id):
    response = video_api_blueprint.delete_video(video_id)
    deleted_video = response.get_json
    return deleted_video


@video_blueprint.route('/', methods=['GET'])
def get_videos():
    response = video_api_blueprint.get_videos()
    video_list = response.get_json()
    return render_template('show-videos.html', video_list=video_list, VideoType=VideoType)


@video_blueprint.route('/team/<int:team_id>', methods=['GET'])
def get_videos_by_team(team_id):
    response = video_api_blueprint.get_videos_by_team(team_id)
    video_list = response.get_json()
    return render_template('show-videos.html', video_list=video_list, VideoType=VideoType)


@video_blueprint.route('/tournament/<int:tournament_id>', methods=['GET'])
def get_videos_by_tournament(tournament_id):
    response = video_api_blueprint.get_videos_by_tournament(tournament_id)
    video_list = response.get_json()
    return render_template('show-videos.html', video_list=video_list, VideoType=VideoType)


@video_blueprint.route('/tournament/<int:tournament_id>/team/<int:team_id>', methods=['GET'])
def get_videos_by_tournament_and_team(tournament_id, team_id):
    response = video_api_blueprint.get_videos_by_tournament_and_team(tournament_id, team_id)
    video_list = response.get_json()
    return render_template('show-videos.html', video_list=video_list, VideoType=VideoType)


@video_blueprint.route('/period/<string:beginning>/<string:ending>', methods=['GET'])
def get_videos_by_period(beginning, ending):
    response = video_api_blueprint.get_videos_by_period(beginning, ending)
    video_list = response.get_json(beginning, ending)
    return render_template('show-videos.html', video_list=video_list, VideoType=VideoType)
