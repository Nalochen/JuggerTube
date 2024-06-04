import pytest


class TestTournamentsRoute:
    def test_get_all_tournaments(self):
        response = client.get('/tournaments')
        assert response.status_code == 200

    def test_get_add_tournament(self):
        response = client.get('/tournaments/add')
        assert response.status_code == 200

    def test_post_add_tournament_no_data(self):
        response = client.post('/tournaments/add',
                               )
        assert response.status_code == 200

    def test_post_add_tournament_works(self):
        response = client.post('/tournaments/add',
                               )
        assert response.status_code == 200

    def test_get_edit_tournament_no_data(self):
        response = client.post('/tournaments/edit',
                               )
        assert response.status_code == 200

    def test_post_edit_tournament_tournament_doesnt_exist(self):
        response = client.post('/tournaments/edit',
                               )
        assert response.status_code == 200

    def test_post_edit_tournament_no_current_user(self):
        response = client.post('/tournaments/edit',
                               )
        assert response.status_code == 200

    def test_post_edit_tournament_works(self):
        response = client.post('/tournaments/edit',
                               )
        assert response.status_code == 200

    def test_delete_tournament(self):
        response = client.get('/tournaments/delete')
        assert response.status_code == 200

    def test_get_tournament_by_period_works(self):
        response = client.get('/tournaments/period')
        assert response.status_code == 200

    def test_get_tournament_by_period_beginning_is_later_than_ending(self):
        response = client.get('/tournaments/period')
        assert response.status_code == 200

    def test_get_tournament_by_period_no_data(self):
        response = client.get('/tournaments/period')
        assert response.status_code == 200

    def test_get_tournament_by_period_no_tournaments_in_period(self):
        response = client.get('/tournaments/period')
        assert response.status_code == 200
