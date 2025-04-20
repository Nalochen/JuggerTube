import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from TournamentTeamsParser import TournamentTeamsParser

# Disable SSL verification warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class DataFetcher:
    def __init__(self, base_url='https://turniere.jugger.org/'):
        self.base_url = base_url
        self.previous_suffix = 'index.event.php#previous'
        self.tournament_suffix = 'tournament.php?id='
        self.results_suffix = 'tournament.result.php?id='

    def fetch_previous_tournaments(self):
        """Fetch the HTML content of the previous tournaments page"""
        url = self.base_url + self.previous_suffix
        response = requests.get(url, verify=False)
        return response.text

    def fetch_tournament_details(self, tournament_id):
        """Fetch the HTML content of a specific tournament's details page"""
        url = self.base_url + self.tournament_suffix + tournament_id
        response = requests.get(url, verify=False)
        return response.text, url

    def fetch_tournament_teams(self, tournament_id):
        """Fetch and parse teams from a tournament's results page"""
        url = self.base_url + self.results_suffix + tournament_id
        try:
            response = requests.get(url, verify=False)
            parser = TournamentTeamsParser()
            parser.feed(response.text)
            return parser.get_teams()
        except Exception as e:
            print(f"Error fetching teams for tournament {tournament_id}: {str(e)}")
            return [] 