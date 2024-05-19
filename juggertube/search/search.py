from flask import Blueprint, render_template

from juggertube.models import Video

search_bp = Blueprint('search_blueprint', __name__)


@search_bp.route('/')
def list():
    videos = Video.query.all()
    return render_template('videos/list.html', videos=videos)

@search_bp.route('/<int:video_id')
def list(video_id):
    video = Video.query.get(video_id)
    return render_template('videos/list.html', video=video)

@search_bp.route('/<int:team_id')
# überlegen wie Funktionalität
def list(team_id):
    videos = Video.query.get(team_id)
    return render_template('team/videos/list.html', videos=videos)
