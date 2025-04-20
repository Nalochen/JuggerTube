from html.parser import HTMLParser


class TournamentDetailsParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.start_date = None
        self.end_date = None
        self.current_tag = None
        self.current_data = None
        self.in_date_field = False

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        # Look for date fields in the tournament details
        if tag == 'div' and any(attr for attr in attrs if attr[0] == 'class' and 'tournament-details' in attr[1]):
            self.in_date_field = True

    def handle_endtag(self, tag):
        if tag == 'div' and self.in_date_field:
            self.in_date_field = False
        self.current_tag = None

    def handle_data(self, data):
        if not self.in_date_field:
            return
            
        data = data.strip()
        if 'Beginn:' in data:
            # Extract the date part after "Beginn:"
            self.start_date = data.split('Beginn:')[1].strip()
        elif 'Ende:' in data:
            # Extract the date part after "Ende:"
            self.end_date = data.split('Ende:')[1].strip()

    def get_dates(self):
        return {
            'start_date': self.start_date,
            'end_date': self.end_date
        }


parser = TournamentDetailsParser()
