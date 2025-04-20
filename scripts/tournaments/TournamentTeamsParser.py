from html.parser import HTMLParser


class TournamentTeamsParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.teams = []
        self.current_tag = None
        self.current_attrs = None
        self.in_table = False
        self.in_row = False
        self.current_team = {}
        self.column_index = 0
        self.current_cell_data = []

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        self.current_attrs = dict(attrs)

        if tag == 'table':
            self.in_table = True
        elif tag == 'tr' and self.in_table:
            self.in_row = True
            self.column_index = 0
            self.current_team = {}
        elif tag == 'td' and self.in_row:
            self.current_cell_data = []

    def handle_endtag(self, tag):
        if tag == 'table':
            self.in_table = False
        elif tag == 'tr' and self.in_row:
            self.in_row = False
            if self.current_team and 'name' in self.current_team and 'city' in self.current_team:
                self.teams.append(self.current_team.copy())
        elif tag == 'td' and self.in_row:
            # Process the complete cell data when the td tag ends
            cell_content = ' '.join(self.current_cell_data).strip()

            if self.column_index == 2:  # Third column (index 2) contains team name
                self.current_team['name'] = cell_content
            elif self.column_index == 3:  # Fourth column (index 3) contains city
                # The city is in the text content, no need to split country
                self.current_team['city'] = cell_content
            self.column_index += 1

    def handle_data(self, data):
        if self.in_row:
            data = data.strip()
            if data:  # Only append non-empty data
                self.current_cell_data.append(data)

    def get_teams(self):
        return self.teams 