import pytest


class TestTeamsRoute:
    def test_get_all_teams(self, client):
        response = client.get('/teams')
        assert response.status_code == 200

    def test_get_add_team(self, client):
        response = client.get('/teams/add')
        assert response.status_code == 200

    @pytest.mark.parametrize('test_input, expected',
                             [
                                 ({'name': 'Pink Pain', 'city': 'Darmstadt', 'country': 'Germany'}, 200),
                                 ({'name': '', 'city': '', 'country': ''}, 404),
                                 ({'name': '12', 'city': '13', 'country': 'Germany'}, 500),
                             ]
                             )
    def test_post_add_team(self, client, test_input, expected):
        assert client.post('/teams/add', data=test_input).status_code == expected

    def test_get_edit_team(self, client):
        response = client.get('/teams/edit')
        assert response.status_code == 200

    @pytest.mark.parametrize('test_input, expected',
                             [
                                 ({'id': 1, 'name': 'Pink Pain', 'city': 'Darmstadt', 'country': 'Germany'}, 200),
                                 ({'id': 5, 'name': 'Pink Pain', 'city': 'Darmstadt', 'country': 'Germany'}, 404),
                                 ({'id': 1, 'name': '', 'city': '', 'country': ''}, 404),
                             ]
                             )
    def test_post_edit_team(self, client, test_input, expected):
        assert client.post('/teams/edit/{test_input[id]}', data=test_input).status_code == expected

    @pytest.mark.parametrize('test_input, expected',
                             [
                                 ({'id': 1}, 200),
                                 ({'id': 5}, 500),
                             ]
                             )
    def test_delete_team(self, client, test_input, expected):
        assert client.post('/teams/delete/{test_input[id]}', data=test_input).status_code == expected
