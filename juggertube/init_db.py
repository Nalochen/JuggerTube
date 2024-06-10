from werkzeug.security import generate_password_hash

from juggertube.game_system_enum import GameSystem
from juggertube.models import db, Channel, User, Tournament, Team, Video
from juggertube.video_type_enum import VideoType


def init_db(app):
    with app.app_context():
        db.drop_all()
        db.create_all()

        tournament1 = Tournament(name='Pömmeltreff Karlsruhe', city='Erlangen', jtr_link='test', tugeny_link='')
        tournament2 = Tournament(name='16. Badische Meisterschaft', city='Freiburg', jtr_link='test', tugeny_link='test')
        tournament3 = Tournament(name='20. Deutsche Meisterschaft (DM 2017)', city='Darmstadt', jtr_link='test', tugeny_link='')

        team1 = Team(name='Pink Pain', country='Germany', city='Darmstadt')
        team2 = Team(name='Jugger Helden Bamberg', country='Germany', city='Bamberg')
        team3 = Team(name='Rigor Mortis', country='Germany', city='Berlin')

        user1 = User(email='test@test.de', username='Patrick', password_hash=generate_password_hash('test', method='scrypt'), team='1')
        user2 = User(email='test@test.de', username='Moritz L.', password_hash=generate_password_hash('test', method='scrypt'), team='2')
        user3 = User(email='test@test.de', username='Lester', password_hash=generate_password_hash('test', method='scrypt'), team='3')

        channel1 = Channel(name='ae²ae³', link='test', owner='1', team_id='1', content_type=VideoType.MATCH)
        channel2 = Channel(name='Jugger Helden Bamberg', link='test', owner='2', team_id='2',
                           content_type=VideoType.SONG)
        channel3 = Channel(name='JuggerBerlin', link='test', owner='3', team_id='3', content_type=VideoType.MATCH)

        video1 = Video(name='Jugger: 5. Frängsche Meisterschaft: Pink Pain - Gossenhauer', channel_id='1',
                       category=VideoType.MATCH, link='test', upload_date='2017-06-23', date_of_recording='2017-05-30', tournament_id='1',
                       team_one_id='1', team_two_id='2', game_system=GameSystem.STONES, weapon_type='', topic='',
                       guests='', comments='')
        video2 = Video(name='2011-BM-Trailer.mp4', channel_id='2', category=VideoType.OTHER, link='test',
                       upload_date='2011-05-23', date_of_recording='', tournament_id='', team_one_id='', team_two_id='',
                       game_system='', weapon_type='', topic='Trailer for BM; 2011', guests='', comments='')
        video3 = Video(name='Jugger Helden Bamberg vs. Rigor Mortis', channel_id='3', category=VideoType.MATCH,
                       link='test', upload_date='2002-02-24', date_of_recording='2002-01-12', tournament_id='3', team_one_id='2',
                       team_two_id='3', game_system=GameSystem.SETS, weapon_type='', topic='', guests='', comments='')

        db.session.add_all([tournament1, tournament2, tournament3])
        db.session.add_all([team1, team2, team3])
        db.session.add_all([user1, user2, user3])
        db.session.add_all([channel1, channel2, channel3])
        db.session.add_all([video1, video2, video3])

        db.session.commit()
