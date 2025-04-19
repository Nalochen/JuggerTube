class Video:
    def __init__(self, name, channel_name, category, link, upload_date, tournament, team_one, team_two,
                 game_system):
        self.name = name
        self.channel_name = channel_name
        self.category = category
        self.link = link
        self.upload_date = upload_date
        self.tournament = tournament
        self.team_one = team_one
        self.team_two = team_two
        self.game_system = game_system
        self.comment = ''
