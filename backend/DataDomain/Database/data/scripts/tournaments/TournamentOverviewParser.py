from html.parser import HTMLParser

from tournament import Tournament


class TournamentsOverviewParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.in_table_data = False
        self.in_tournament = False
        self.is_past_tournament = False
        self.last_tag = None
        self.tournament_array = []
        self.temp_name = ''
        self.temp_id = ''
        self.temp_country = ''
        self.temp_city = ''

    def handle_starttag(self, tag, attrs):
        if tag == 'h2':
            self.last_tag = tag
        if tag == 'tr' and self.is_past_tournament:
            self.in_tournament = True
        if tag == 'td' and self.is_past_tournament:
            self.in_table_data = True
            self.last_tag = tag
        if tag == 'a' and self.in_table_data:
            for name, value in attrs:
                if name == 'title' and value != 'Ergebnisse':
                    self.temp_name = value
                if (name == 'href' and value.split('?id=')[0] != 'tournament.result.php'
                        and value.split('?id=')[0] != 'tournament.signin.php'):
                    index = value.split('?id=')
                    self.temp_id = index[1]

        if tag == 'img' and self.in_table_data:
            self.last_tag = tag
            for name, value in attrs:
                if name == 'title':
                    self.temp_country = value

    def handle_endtag(self, tag):
        if tag == 'td':
            self.in_table_data = False
        if tag == 'tr':
            self.in_tournament = False
            if self.temp_name != '' and self.temp_id != '' and self.temp_country != '' and self.temp_city != '':
                tournament = Tournament(self.temp_id, self.temp_name, 'test', 'test', self.temp_city, self.temp_country)
                self.tournament_array.append(tournament)
                self.temp_name = ''
                self.temp_id = ''
                self.temp_country = ''
                self.temp_city = ''

    def handle_data(self, data):
        if self.last_tag == 'img' and self.in_table_data:
            self.temp_city = data.lstrip(' ')
        if self.last_tag == 'h2' and data == 'Vergangene Termine':
            self.is_past_tournament = True


parser = TournamentsOverviewParser()
