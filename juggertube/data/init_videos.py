from datetime import datetime

from juggertube.data.videos import videos

from juggertube.models import db, Channel, Tournament, Team, Video


videos_with_missing_attributes = []


def init_videos(app):
    with app.app_context():
        for video in videos:
            channel = Channel.query.filter_by(name=video["channel"]).first()

            if not channel:
                print(video["name"])
                videos_with_missing_attributes.append(video)
                continue

            if ('dateOfUpload' or 'name' or 'link' or 'category') not in video:
                videos_with_missing_attributes.append(video)
                continue

            video_data = {
                'category': video["category"],
                'name': video["name"],
                'link': video["link"],
                'channel': Channel.query.filter_by(name=video["channel"]).first(),
                'upload_date': datetime.strptime(video["dateOfUpload"], '%Y-%m-%dT%H:%M:%S')
            }

            if "comments" in video:
                video_data['comments'] = video["comments"]

            if "tournament" in video:
                video_data['tournament'] = Tournament.query.filter_by(name=video["tournament"]).first()

                if "dateOfRecording" in video:
                    video_data['date_of_recording'] = video["dateOfRecording"]
                if "team1" in video and "team2" in video:
                    video_data['team_one'] = Team.query.filter_by(name=video["team1"]).first()
                    video_data['team_two'] = Team.query.filter_by(name=video["team2"]).first()
                if "gameSystem" in video:
                    video_data['game_system'] = video["gameSystem"]
            if "typeOfWeapon" in video:
                video_data['weapon_type'] = video["typeOfWeapon"]
            if "topic" in video:
                video_data['topic'] = video["topic"]
            if "guests" in video:
                video_data['guests'] = video["guests"]

            existing_video = Video.query.filter_by(name=video_data['name']).first()

            if not existing_video:
                new_video = Video(**video_data)
                db.session.add(new_video)

            db.session.commit()
