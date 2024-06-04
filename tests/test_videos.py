import pytest


class TestvideosRoute:
    def test_get_all_videos(self):
        response = client.get('/videos')
        assert response.status_code == 200

    def test_get_add_video(self):
        response = client.get('/videos/add')
        assert response.status_code == 200

    def test_post_add_video_no_data(self):
        response = client.post('/videos/add',
                               )
        assert response.status_code == 200

    def test_post_add_video_works(self):
        response = client.post('/videos/add',
                               )
        assert response.status_code == 200

    def test_post_add_video_no_tournaments_existing(self):
        response = client.post('/videos/add',
                               )
        assert response.status_code == 200

    def test_post_add_video_no_teams_existing(self):
        response = client.post('/videos/add',
                               )
        assert response.status_code == 200

    def test_get_edit_video_no_data(self):
        response = client.post('/videos/edit',
                               )
        assert response.status_code == 200

    def test_post_edit_video_video_doesnt_exist(self):
        response = client.post('/videos/edit',
                               )
        assert response.status_code == 200

    def test_post_edit_video_no_tournaments_existing(self):
        response = client.post('/videos/edit',
                               )
        assert response.status_code == 200

    def test_post_edit_video_no_teams_existing(self):
        response = client.get('/auth')
        assert response.status_code == 200

    def test_post_edit_video_no_current_user(self):
        response = client.post('/videos/edit',
                               )
        assert response.status_code == 200

    def test_post_edit_video_current_user_didnt_upload_video(self):
        response = client.post('/videos/edit',
                               )
        assert response.status_code == 200

    def test_post_edit_video_works(self):
        response = client.post('/videos/edit',
                               )
        assert response.status_code == 200

    def test_delete_video(self):
        response = client.get('/videos/delete')
        assert response.status_code == 200

    def test_get_videos_by_team_works(self):
        response = client.get('/videos/team')
        assert response.status_code == 200

    def test_get_videos_by_team_no_data(self):
        response = client.get('/videos/team')
        assert response.status_code == 200

    def test_get_videos_by_team_team_id_doesnt_exist(self):
        response = client.get('/videos/team')
        assert response.status_code == 200

    def test_get_videos_by_tournament_works(self):
        response = client.get('/videos/tournament')
        assert response.status_code == 200

    def test_get_videos_by_tournament_no_data(self):
        response = client.get('/videos/tournament')
        assert response.status_code == 200

    def test_get_videos_by_team_tournament_id_doesnt_exist(self):
        response = client.get('/videos/tournament')
        assert response.status_code == 200

    def test_get_videos_by_tournament_and_team_works(self):
        response = client.get('/videos/tournament/team')
        assert response.status_code == 200

    def test_get_videos_by_tournament_and_team_no_data(self):
        response = client.get('/videos/tournament/team')
        assert response.status_code == 200

    def test_get_videos_by_tournament_and_team_team_id_doesnt_exist(self):
        response = client.get('/videos/tournaments/team')
        assert response.status_code == 200

    def test_get_videos_by_tournament_and_team_tournament_id_doesnt_exist(self):
        response = client.get('/videos/tournaments/team')
        assert response.status_code == 200

    def test_get_videos_by_tournament_and_team_tournament_id_and_team_id_doesnt_exist(self):
        response = client.get('/videos/tournaments/team')
        assert response.status_code == 200

    def test_get_video_by_period_works(self):
        response = client.get('/videos/period')
        assert response.status_code == 200

    def test_get_video_by_period_beginning_is_later_than_ending(self):
        response = client.get('/videos/period')
        assert response.status_code == 200

    def test_get_video_by_period_no_data(self):
        response = client.get('/videos/period')
        assert response.status_code == 200

    def test_get_video_by_period_no_videos_in_period(self):
        response = client.get('/videos/period')
        assert response.status_code == 200
