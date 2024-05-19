from flask import Blueprint, jsonify
from app.models import Video

video_blueprint = Blueprint('videos', __name__)


# Helper function to serialize video data
def serialize_video(video):
    return {
        'video_id': video.video_id,
        'name': video.name,
        'channel_id': video.channel_id,
        'link': video.link,
        'tournament_id': video.tournament_id,
        'team_one_id': video.team_one_id,
        'team_two_id': video.team_two_id,
        'upload_date': video.upload_date.isoformat(),
        'comments': video.comments,
        'type': video.type
    }


@video_blueprint.route('/videos', methods=['GET'])
def get_videos():
    videos = Video.query.all()
    video_list = [serialize_video(video) for video in videos]
    return jsonify(video_list)


@video_blueprint.route('/videos/team/<int:team_id>', methods=['GET'])
def get_videos_by_team(team_id):
    videos = Video.query.filter((Video.team_one_id == team_id) | (Video.team_two_id == team_id)).all()
    video_list = [serialize_video(video) for video in videos]
    return jsonify(video_list)


@video_blueprint.route('/videos/tournament/<int:tournament_id>', methods=['GET'])
def get_videos_by_tournament(tournament_id):
    videos = Video.query.filter_by(tournament_id=tournament_id).all()
    video_list = [serialize_video(video) for video in videos]
    return jsonify(video_list)


@video_blueprint.route('/videos/tournament/<int:tournament_id>/team/<int:team_id>', methods=['GET'])
def get_videos_by_tournament_and_team(tournament_id, team_id):
    videos = Video.query.filter_by(tournament_id=tournament_id).filter(
        (Video.team_one_id == team_id) | (Video.team_two_id == team_id)
    ).all()
    video_list = [serialize_video(video) for video in videos]
    return jsonify(video_list)
