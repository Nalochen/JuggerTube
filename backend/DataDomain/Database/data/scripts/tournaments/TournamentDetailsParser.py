from html.parser import HTMLParser


class TournamentsOverviewParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.last_tag = None
        self.is_begin = 0
        self.is_end = 0
        self.temp_begin = ''
        self.temp_end = ''

    def handle_starttag(self, tag, attrs):
        if tag == 'td':
            self.last_tag = tag

    def handle_data(self, data):
        if self.is_begin == 2:
            self.temp_begin = data
            self.is_begin = 0
        if self.is_end == 2:
            self.temp_end = data
            self.is_end = 0

        if self.is_begin == 1:
            self.is_begin = 2
        if self.is_end == 1:
            self.is_end = 2

        if self.last_tag == 'td' and data == 'Beginn:':
            self.is_begin = 1
        if self.last_tag == 'td' and data == 'Ende:':
            self.is_end = 1

    def get_temp_dates(self):
        return self.temp_begin, self.temp_end


parser = TournamentsOverviewParser()
