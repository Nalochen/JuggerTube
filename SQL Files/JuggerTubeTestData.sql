USE JuggerTube;

INSERT INTO Tournaments VALUES ('5. (offizieller) LahnveilchenCup', '2024-05-04', '2024-05-06', 'Giessen', 'https://turniere.jugger.org/tournament.php?id=724');
INSERT INTO Tournaments VALUES ('2. Berlin Minors', '2024-04-20', '2024-04-20', 'Berlin', 'https://turniere.jugger.org/tournament.php?id=738');

INSERT INTO Teams VALUES ('Pink Pain', 'DE', 'Darmstadt');
INSERT INTO Teams VALUES ('Cranium Ex Machina', 'DE', 'Hamburg');

INSERT INTO Users VALUES ('unger.juli@gmx.de', 'Nalo', 'Passwort');
INSERT INTO Users VALUES ('nala.bibliander@gmail.com', 'Nalalinchen', 'Passwort2');

INSERT INTO Channels VALUES ('Nalos Videos', 'https://youtube.com/@Schlumpf');
INSERT INTO Channels VALUES ('Nalalinchens Videos', 'https://youtube.com/@Renzo69');

INSERT INTO Videos VALUES ('blub', 1, 'https://stuff', 1, 1, 2, '2020-04-05', 'reports');
INSERT INTO Videos VALUES ('blubb', 2, 'https://stuff', 2, 1, 2, '2020-04-05', 'reports');
INSERT INTO Videos VALUES ('blubbi', 1, 'https://stuff', 2, 1, 2, '2020-04-05', 'reports');
INSERT INTO Videos VALUES ('blubsi', 2, 'https://stuff', 1, 1, 2, '2020-04-05', 'reports');