import pytest


class TestTournamentsRoute:
    def test_get_all_tournaments(self, client):
        response = client.get('/tournaments')
        assert response.status_code == 200

    def test_get_add_tournament(self, client):
        response = client.get('/tournaments/add')
        assert response.status_code == 200

    @pytest.mark.parametrize('test_input, expected',
                             [
                                 ({'name': '3. LahnveilchenCup-Cake', 'city': 'Gießen', 'jtr_link': 'https://xxx.de',
                                   'tugeny_link': 'https://xxx.de'}, 200),
                                 ({'name': '3. LahnveilchenCup-Cake', 'city': 'Gießen', 'jtr_link': 'https://xxx.de',
                                   'tugeny_link': ''}, 200),
                                 ({'name': '3. LahnveilchenCup-Cake', 'city': 'Gießen', 'jtr_link': '',
                                   'tugeny_link': 'https://xxx.de'}, 200),
                                 ({'name': '3. LahnveilchenCup-Cake', 'city': 'Gießen'}, 200),
                                 ({'name': '3. LahnveilchenCup-Cake', 'city': 'Gießen',
                                   'jtr_link': 'https://xxx.de'}, 200),
                                 ({'name': '3. LahnveilchenCup-Cake', 'city': 'Gießen',
                                   'tugeny_link': 'https://xxx.de'}, 200),
                                 ({'city': 'Gießen', 'jtr_link': 'https://xxx.de',
                                   'tugeny_link': 'https://xxx.de'}, 500),
                                 ({'name': '3. LahnveilchenCup-Cake', 'jtr_link': 'https://xxx.de',
                                   'tugeny_link': 'https://xxx.de'}, 500),
                                 ({'jtr_link': 'https://xxx.de', 'tugeny_link': 'https://xxx.de'}, 500),
                             ]
                             )
    def test_post_add_tournament(self, client, test_input, expected):
        assert client.post('/tournaments/add', data=test_input).status_code == expected

    def test_get_edit_tournament(self, client):
        response = client.post('/tournaments/edit/{test_input[id]}',
                               )
        assert response.status_code == 200

    @pytest.mark.parametrize('test_input, expected',
                             [
                                 ({'id': 1, 'name': '3. LahnveilchenCup-Cake', 'city': 'Gießen', 'jtr_link': 'https://xxx.de',
                                   'tugeny_link': 'https://xxx.de'}, 200),
                                 ({'id': 1, 'name': '3. LahnveilchenCup-Cake', 'city': 'Gießen', 'jtr_link': 'https://xxx.de',
                                   'tugeny_link': ''}, 200),
                                 ({'id': 1, 'name': '3. LahnveilchenCup-Cake', 'city': 'Gießen', 'jtr_link': '',
                                   'tugeny_link': 'https://xxx.de'}, 200),
                                 ({'id': 5, 'name': '3. LahnveilchenCup-Cake', 'city': 'Gießen', 'jtr_link': '',
                                   'tugeny_link': 'https://xxx.de'}, 404),
                                 ({'id': 1, 'name': '3. LahnveilchenCup-Cake', 'city': 'Gießen'}, 200),
                                 ({'id': 1, 'name': '3. LahnveilchenCup-Cake', 'city': 'Gießen',
                                   'jtr_link': 'https://xxx.de'}, 200),
                                 ({'id': 1, 'name': '3. LahnveilchenCup-Cake', 'city': 'Gießen',
                                   'tugeny_link': 'https://xxx.de'}, 200),
                                 ({'city': 'Gießen', 'jtr_link': 'https://xxx.de',
                                   'tugeny_link': 'https://xxx.de'}, 500),
                                 ({}, 500),
                                 ({'name': '3. LahnveilchenCup-Cake', 'jtr_link': 'https://xxx.de',
                                   'tugeny_link': 'https://xxx.de'}, 500),
                                 ({'jtr_link': 'https://xxx.de', 'tugeny_link': 'https://xxx.de'}, 500),
                             ]
                             )
    def test_post_edit_tournament_works(self, client, test_input, expected):
        assert client.post(f'/tournaments/edit/{test_input.id}', data=test_input).status_code == expected

    @pytest.mark.parametrize('test_input, expected',
                             [
                                 ({'id': 1}, 200),
                                 ({'id': 5}, 500),
                             ]
                             )
    def test_delete_tournament(self, client, test_input, expected):
        assert client.post('/teams/edit/{test_input[id]}', data=test_input).status_code == expected

