import pytest


class TestApiTeamsRoute:
    def test_get_all_teams(self, client):
        response = client.get('/api/teams/')
        assert response.status_code == 200

    @pytest.mark.parametrize('test_input, expected',
                             [
                                 ({'name': 'Pink Pain', 'city': 'Darmstadt', 'country': 'Germany'}, 200),
                                 ({'name': '', 'city': '', 'country': ''}, 400),
                             ]
                             )
    def test_post_add_team(self, client, test_input, expected):
        assert client.post('/api/teams/add', data=test_input).status_code == expected

    def test_get_edit_team_200(self, client):
        team_id = 5
        response = client.get(f'/api/teams/edit/{team_id}')
        assert response.status_code == 200

    def test_get_edit_team_404(self, client):
        team_id = 5
        response = client.get(f'/api/teams/edit/{team_id}')
        assert response.status_code == 404

    @pytest.mark.parametrize('test_input, expected',
                             [
                                 ({'id': 1, 'name': 'Pink Pain', 'city': 'Darmstadt', 'country': 'Germany'}, 200),
                                 ({'id': 5, 'name': '', 'city': '', 'country': ''}, 400),
                             ]
                             )
    def tes_get_edit_team(self, client, test_input, expected):
        video_id = test_input['id']
        assert client.get(f'/api/teams/edit/{video_id}', data=test_input).status_code == expected

