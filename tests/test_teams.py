import pytest


class TestTeamsRoute:
    def test_get_all_teams(self):
        response = client.get('/teams')
        assert response.status_code == 200

    def test_get_add_team(self):
        response = client.get('/teams/add')
        assert response.status_code == 200

    def test_post_add_team_no_data(self):
        response = client.post('/teams/add',
                               )
        assert response.status_code == 200

    def test_post_add_team_works(self):
        response = client.post('/teams/add',
                               )
        assert response.status_code == 200

    def test_get_edit_team_no_data(self):
        response = client.post('/teams/edit',
                               )
        assert response.status_code == 200

    def test_post_edit_team_team_doesnt_exist(self):
        response = client.post('/teams/edit',
                               )
        assert response.status_code == 200

    def test_post_edit_team_no_current_user(self):
        response = client.post('/teams/edit',
                               )
        assert response.status_code == 200

    def test_post_edit_team_works(self):
        response = client.post('/teams/edit',
                               )
        assert response.status_code == 200

    def test_delete_team(self):
        response = client.get('/teams/delete')
        assert response.status_code == 200
