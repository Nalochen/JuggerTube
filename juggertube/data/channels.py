from juggertube.models import db, Channel, User

new_channels = [
    {"channel": Channel(name='ae²ae³', link='https://www.youtube.com/channel/UCoMgxsjBb1jWfFuyXGT4LdA'),
     "owner": ["Patrick"]},
    {"channel": Channel(name='Anima Equorum', link='https://www.youtube.com/channel/UCDLlRK8kv9EZf7xMip3tMrw')},
    {"channel": Channel(name='Bavaria Scouts ', link='https://www.youtube.com/channel/UCEyObGMhRUKQnD-T6cFbkKg')},
    {"channel": Channel(name='Der Dodo', link='https://www.youtube.com/user/DerDodoDerUeberlebte/videos')},
    {"channel": Channel(name='Eike Engelmann', link='https://www.youtube.com/channel/UCNt5A5d69EO_xAEtp7rPBRw')},
    {"channel": Channel(name='Fuchsigel', link='https://www.youtube.com/user/FuchsIgel'), "owner": ["{Peter}"]},
    {"channel": Channel(name='Jugger Basel', link='https://www.youtube.com/channel/UCvdd5RoFdmzJhBTeesXZ6og'),
     "owner": ["Max CH"]},
    {"channel": Channel(name='Jugger Bonn', link='https://www.youtube.com/channel/UC3JG4yWBV231GEiEx39CTSQ'),
     "owner": ["Jonas"]},
    {"channel": Channel(name='Jugger e. V.', link='https://www.youtube.com/channel/UCNWJAJND0Br6XXfgfSUZvlA'),
     "owner": ["David GAG"]},
    {"channel": Channel(name='Jugger Helden Bamberg', link='https://www.youtube.com/channel/UC51R2lzV3fDLkctA7oB36vQ')},
    {"channel": Channel(name='Jugger Köln', link='https://www.youtube.com/channel/UC-USkE95FmRuhr74K5fLaKg')},
    {"channel": Channel(name='Jugger Masterclass', link='https://www.youtube.com/channel/UCWhQ8e2hrjiE1dRxf4QleBw'),
     "owner": ["David"]},
    {"channel": Channel(name='Jugger Vienna', link='https://www.youtube.com/channel/UC-USkE95FmRuhr74K5fLaKg')},
    {"channel": Channel(name='JuggerBerlin', link='https://www.youtube.com/user/JuggerBerlin'), "owner": ["Lester"]},
    {"channel": Channel(name='JuggerHagen', link='https://www.youtube.com/user/JuggerHagen'), "owner": ["Kurt"]},
    {"channel": Channel(name='Juggerland 786', link='https://www.youtube.com/c/Juggerland786/videos')},
    {"channel": Channel(name='Juggerlicious', link='https://www.youtube.com/user/EvomSports')},
    {"channel": Channel(name='Juggerliga', link='https://www.youtube.com/user/Juggerliga')},
    {"channel": Channel(name='Julinho9', link='https://www.youtube.com/channel/UC0IvZWrPJGnbGDnqj8-iMog'),
     "owner": ["Jules"]},
    {"channel": Channel(name='KJG Goldbach', link='https://www.youtube.com/channel/UC0tV2hOJtu6JFnms_2eOKpQ')},
    {"channel": Channel(name='Kuhdorf Vereinigung',
                        link='https://www.youtube.com/channel/UCWo6wUAPyxvdZX6swEN04_A/videos')},
    {"channel": Channel(name='Linus Smid', link='https://www.youtube.com/channel/UCBMUWrcA09C-e9weWGxeJLQ'),
     "owner": ["Linus"]},
    {"channel": Channel(name='MicalLex', link='https://www.youtube.com/user/MicalLex')},
    {"channel": Channel(name='NLG Jugger', link='https://www.youtube.com/c/peterspawns'), "owner": ["Manuel"]},
    {"channel": Channel(name='Peters Pawns', link='https://www.youtube.com/c/peterspawns'), "owner": ["Max V."]},
    {"channel": Channel(name='Pompfritz', link='https://www.youtube.com/channel/UCkxGVt10fX3xVrhRXYfruLg'),
     "owner": ["Marc"]},
    {"channel": Channel(name='Robert Kruse', link='https://www.youtube.com/user/Krusesensei')},
    {"channel": Channel(name='Setanta Jugger Club', link='https://www.youtube.com/channel/UCQlzSKPouMfrETbGZiaAwcA')},
    {"channel": Channel(name='Simba (LNW)', link='https://www.youtube.com/channel/UC05M-gM2gLXlF8VbC1pGagQ'),
     "owner": ["Simba"]},
    {"channel": Channel(name='Sloth Machine Jugger', link='https://www.youtube.com/channel/UCYM6cD6AYFZOuF8GR90hI8A'),
     "owner": ["Nadine"]},
    {"channel": Channel(name='Sonnenwende', link='https://www.youtube.com/channel/UCS6FpXwF7ePQpn0d2N5fupg')},
    {"channel": Channel(name='Thomas Haase', link='https://www.youtube.com/channel/UCBEwN3Yh8TnSI5f8M0PoQMg')},
    {"channel": Channel(name='Tobias Lunever (Saarland)',
                        link='https://www.youtube.com/channel/UCff21s6RdFLmXd3pgmnzKig/')},
    {"channel": Channel(name='Trashcore', link='https://soundcloud.com/trashcore1'), "owner": ["Jens"]},
    {"channel": Channel(name='Uhus Jugger Tutorials', link='https://www.youtube.com/user/EinUhu'),
     "owner": ["Uhu/Ruben"]},
    {"channel": Channel(name='Verstörte Zernichter', link='https://www.youtube.com/channel/UCpnNhuA3b_6v4BZaZHmM8kQ'),
     "owner": ["Nikolay"]},
    {"channel": Channel(name='Zonenkinder Jena', link='https://www.youtube.com/channel/UCzM4B-wkOn9q9o4I1u2mdHA')},
    {"channel": Channel(name='Felix Superbike', link='https://www.youtube.com/channel/UC8ICgb-mZqwPaHa2yMFY7_Q')},
    {"channel": Channel(name='Cervisia Ultima', link='https://www.youtube.com/user/CervisiaUltima/featured')},
    {"channel": Channel(name='Johnatan Blum', link='https://www.youtube.com/user/semtext44/'), "owner": ["Joni"]},
    {"channel": Channel(name='Magazin des Unpopulären Sports (MUS)', link='https://www.musmagazin.de/')},
    {"channel": Channel(name='MeinSportPodcast', link='https://meinsportpodcast.de/')},
    {"channel": Channel(name='Jugglers Jugg', link='https://www.youtube.com/channel/UCzn5cLOLdVim_loT0F3qY3g')},
    {"channel": Channel(name='Rigor Mortis', link='https://www.youtube.com/channel/UCw3u9TFaD-cSW8CwdZZblDQ/videos')},
    {"channel": Channel(name='Heidelberg Hobbiz',
                        link='https://www.youtube.com/channel/UCEQ1LdfVPa7XBsF_jNtCiYg/videos')},
    {"channel": Channel(name='Oldenburger Keiler',
                        link='https://www.youtube.com/channel/UCwJakWhiTG6zcOkmQrqoEDw/videos')},
    {"channel": Channel(name='Manololo Justen', link='https://www.youtube.com/user/ffmmtklkf/videos')},
    {"channel": Channel(name='Federación Española de Jugger',
                        link='https://www.youtube.com/c/Federaci%C3%B3nEspa%C3%B1oladeJugger/videos')},
    {"channel": Channel(name='Play Jugger', link='https://www.youtube.com/channel/UCB3PRRTaOFH-x4cQlb0y_Jg/videos')},
    {"channel": Channel(name='Jugger Australis', link='https://www.youtube.com/channel/UCoYS3KjNmlkP1HWl_Vkm9Yw')},
    {"channel": Channel(name='Peter Sanzén', link='https://www.youtube.com/channel/UCc792Fu8RU56D6BbLuSSRjw')},
    {"channel": Channel(name='Rubén Durbán', link='https://www.youtube.com/user/Rdg18/videos')},
    {"channel": Channel(name='Carlos Gómez Gónzalez', link='https://www.youtube.com/user/camaitz/videos')},
    {"channel": Channel(name='Team Hunter.Jugger',
                        link='https://www.youtube.com/channel/UCNaHT0-1fR3uM66_NmbtdRw/videos')},
    {"channel": Channel(name='Jugger Murcia Videos',
                        link='https://www.youtube.com/channel/UCJiwJ5B2226OcaDilJ5ftYA/videos')},
    {"channel": Channel(name='Barcelona Jugger Club',
                        link='https://www.youtube.com/channel/UCt5WjP8b_EChKddE2ZZetmQ/videos')},
    {"channel": Channel(name='AMUJugger', link='https://www.youtube.com/user/AMUJugger/videos')},
    {"channel": Channel(name='Indiwi', link='https://www.youtube.com/channel/UCtqOtj28OGFgvXStCH2WXcw')},
    {"channel": Channel(name='Sassy Sunbird Productions',
                        link='https://www.youtube.com/channel/UCEIawSh9Gw16WCL4PNP5hVw'),
     "owner": ["{Peter}"]},
    {"channel": Channel(name='Jugger Clips', link='https://www.youtube.com/channel/UCH50YT2n2Vzw3EYr5ForU9Q'),
     "owner": ["Ludwig"]},
    {"channel": Channel(name='Yps', link='https://www.youtube.com/channel/UCIbhF_XN4X1HvanbVgozeXA'), "owner": ["Yps"]},
    {"channel": Channel(name='Jugger Paris', link='https://www.youtube.com/channel/UCLAPGNLYBU8oEO9qFJhdQIQ'),
     "owner": ["Luca"]},
    {"channel": Channel(name='Watch JUGGER', link='https://www.youtube.com/channel/UC1EXd2J8aqwiKC64yvIMKGQ'),
     "owner": ["Manuel", "Finn Eh"]},
    {"channel": Channel(name='Karlshorster Kollektiv',
                        link='https://www.youtube.com/channel/UC3LwAWYx-sPRvqVS5DdZqDg/videos'), "owner": ["Robert"]},
    {"channel": Channel(name='Asociacíon Aragonesa de Jugger',
                        link='https://www.youtube.com/user/juggeraragon/featured')},
    {"channel": Channel(name='Leipziger Nachtwache', link='https://www.youtube.com/@leipzigernachtwache92800'),
     "owner": ["Ludwig"]}
]

for new_channel in new_channels:
    db.session.add(new_channel.channel)
    db.session.flush()
    channel = db.session.query(Channel).get(new_channel.channel.id)

    user_id = User.query.filter_by(name=new_channel.owner).id
    user = db.session.query(User).get(user_id)

    channel.owners.append(user)
    user.channels.append(channel)

db.session.commit()