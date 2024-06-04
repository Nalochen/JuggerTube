import pytest


def test_get_all_teams(client):
    response = client.get('/teams')
    assert response.status_code == 200


def test_get_add_team(client):
    response = client.get('/teams/add')
    assert response.status_code == 200


@pytest.mark.parametrize('test_input, expected',
                         [
                             ({'name': 'Pink Pain', 'city': 'Darmstadt', 'country': 'Germany'}, 200),
                             ({'name': '', 'city': '', 'country': ''}, 404),
                             ({'name': '12', 'city': '13', 'country': 'Germany'}, 500),
                         ]
                         )
def test_post_add_team(client, test_input, expected):
    assert client.post('/teams/add', data=test_input).status_code == expected


def test_get_edit_team(client):
    response = client.get('/teams/edit')
    assert response.status_code == 200


@pytest.mark.parametrize('test_input, expected',
                         [
                             ({'id': 1, 'name': 'Pink Pain', 'city': 'Darmstadt', 'country': 'Germany',
                               'current_user': 1}, 200),
                             ({'id': 5, 'name': 'Pink Pain', 'city': 'Darmstadt', 'country': 'Germany',
                               'current_user': 1}, 404),
                             ({'id': 1, 'name': '', 'city': '', 'country': '',
                               'current_user': 1}, 404),
                             ({'id': 1, 'name': 'Pink Pain', 'city': 'Darmstadt', 'country': 'Germany',
                               'current_user': 5}, 200),
                         ]
                         )
def test_post_edit_team(client, test_input, expected):
    assert client.post('/teams/edit', data=test_input).status_code == expected


def test_delete_team(client):
    # video existiert
    # video existiert nicht
    response = client.get('/teams/delete')
    assert response.status_code == 200
