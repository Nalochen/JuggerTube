def serialize_channel(channel):
    owners = [owner.username for owner in channel.owners]
    return {
        'channel_id': channel.id,
        'name': channel.name,
        'link': channel.link,
        'owners': owners
    }


def serialize_video(video):
    return {
        'video_id': video.id,
        'channel': video.channel.name,
        'category': video.category.value,
        'name': video.name,
        'link': video.link,
        'tournament': video.tournament.name if video.tournament else None,
        'team_one': video.team_one.name if video.team_one else None,
        'team_two': video.team_two.name if video.team_two else None,
        'upload_date': video.upload_date.strftime('%Y-%m-%d'),
        'date_of_recording': video.date_of_recording.strftime('%Y-%m-%d') if video.date_of_recording else None,
        'game_system': video.game_system.value if video.game_system else None,
        'weapon_type': video.weapon_type if video.weapon_type else None,
        'topic': video.topic if video.topic else None,
        'guests': video.guests if video.guests else None,
        'comments': video.comments if video.comments else None,
    }


def serialize_team(team):
    return {
        'team_id': team.id,
        'name': team.name,
        'country': team.country,
        'city': team.city,
    }


def serialize_tournament(tournament):
    return {
        'tournament_id': tournament.id,
        'name': tournament.name,
        'city': tournament.city,
        'jtr_link': tournament.jtr_link,
        'tugeny_link': tournament.tugeny_link,
    }


def serialize_user(user):
    teams = [team.name for team in user.teams]
    return {
        'user_id': user.id,
        'username': user.username,
        'email': user.email,
        'teams': teams
    }


def serialize_choices(choice):
    choice_id, name = choice
    return {
        'choice_id': choice_id,
        'name': name
    }


def serialize_device(device):
    return {
        'device_id': device.id,
        'device_name': device.device_name,
        'device_key': device.device_key,
        'device_owner': device.user.username
    }
