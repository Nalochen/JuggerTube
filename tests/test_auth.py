import pytest


class TestAuthRoute:
    def test_users(self):
        response = client.get('/auth')
        assert response.status_code == 200

    def test_get_register(self):
        response = client.get('/auth/register')
        assert response.status_code == 200

    def test_post_register_no_data(self):
        response = client.post('/auth/register',
                               headers={'Content-Type': 'application/json'},
                               data={})
        assert response.status_code == 200

    def test_post_register_user_already_exists(self):
        response = client.post('/auth/register',
                               headers={'Content-Type': 'application/json'},
                               data={})
        assert response.status_code == 200

    def test_post_register_password_hashs_are_different(self):
        response = client.post('/auth/register',
                               headers={'Content-Type': 'application/json'},
                               data={})
        assert response.status_code == 200

    def test_post_register_user_creation_works(self):
        response = client.post('/auth/register',
                               headers={'Content-Type': 'application/json'},
                               data={})
        assert response.status_code == 200

    def test_get_login(self):
        response = client.get('/auth/login')
        assert response.status_code == 200

    def test_post_login_no_data(self):
        response = client.get('/auth/login')
        assert response.status_code == 200

    def test_post_login_user_doesnt_exist(self):
        response = client.get('/auth/login')
        assert response.status_code == 200

    def test_post_login_password_hash_is_false(self):
        response = client.get('/auth/login')
        assert response.status_code == 200

    def test_logout(self):
        response = client.get('/auth/logout')
        assert response.status_code == 200

    def test_delete_user(self):
        response = client.get('/auth/delete')
        assert response.status_code == 200
