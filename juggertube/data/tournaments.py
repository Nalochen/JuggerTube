from juggertube.models import Tournament, db

tournaments = [
    Tournament(name='NRW Winterliga 2019/20 Hagen', city='Hagen',
               jtr_link='https://turniere.jugger.org/tournament.php?id=522'),
    Tournament(name='1. Rheinhessischer Rauf- und Saufcup', city='Bingen',
               jtr_link='https://turniere.jugger.org/tournament.php?id=498'),
    Tournament(name='5. Frängsche Meisterschaft', city='Erlangen'),
    Tournament(name='Pömmeltreff Karlsruhe', city='Karlsruhe',
               jtr_link='https://turniere.jugger.org/tournament.php?id=506'),
    Tournament(name='16. Badische Meisterschaft', city='Freiburg',
               jtr_link='https://turniere.jugger.org/tournament.php?id=497'),
    Tournament(name='Catch the Fish - Kiel International Tournament', city='Kiel',
               jtr_link='https://turniere.jugger.org/tournament.php?id=365'),
    Tournament(name='20. Deutsche Meisterschaft (DM 2017)', city='Darmstadt',
               jtr_link='https://turniere.jugger.org/tournament.php?id=335'),
    Tournament(name='3. Rheinland-Pfälzische Meisterschaft', city='Mainz',
               jtr_link='https://turniere.jugger.org/tournament.php?id=334'),
    Tournament(name='1. Darmstädter Meisterschaft', city='Darmstadt',
               jtr_link='https://turniere.jugger.org/tournament.php?id=333'),
    Tournament(name='9. Hessische Meisterschaft', city='Rotenburg an der Fulda',
               jtr_link='https://turniere.jugger.org/tournament.php?id=310'),
    Tournament(name='4. Südwest Regionalturnier', city='Homburg',
               jtr_link='https://turniere.jugger.org/tournament.php?id=313'),
    Tournament(name='Open Jugger League 2016', city='Darmstadt',
               jtr_link='https://turniere.jugger.org/tournament.php?id=332'),
    Tournament(name='16. Bayerische Meisterschaft', city='Waidhaus',
               jtr_link='https://turniere.jugger.org/tournament.php?id=273'),
    Tournament(name='Holt euch die Banane! 2016', city='Sulzbach-Rosenberg',
               jtr_link='https://turniere.jugger.org/tournament.php?id=260'),
    Tournament(name='2. Rheinland-Pfälzische Meisterschaft', city='Mainz'),
    Tournament(name='14. Badische Meisterschaft 2016', city='Villingen',
               jtr_link='https://turniere.jugger.org/tournament.php?id=271'),
    Tournament(name='3. Südwest Regionalturnier', city='Homburg',
               jtr_link='https://turniere.jugger.org/tournament.php?id=264'),
    Tournament(name='Open Jugger League 2015', city='Freiburg',
               jtr_link='https://turniere.jugger.org/tournament.php?id=235'),
    Tournament(name='German Jugger League Playoffs 2016', city='Jena',
               jtr_link='https://turniere.jugger.org/tournament.php?id=281'),
    Tournament(name='18. Deutsche Meisterschaft (DM 2015)', city='Berlin',
               jtr_link='https://turniere.jugger.org/tournament.php?id=212'),
    Tournament(name='2. Karlsruher Pömmelturnier', city='Karlsruhe',
               jtr_link='https://turniere.jugger.org/tournament.php?id=265'),
    Tournament(name='1. Rheinland-Pfälzische Meisterschaft', city='Mainz',
               jtr_link='https://turniere.jugger.org/tournament.php?id=221'),
    Tournament(name='15. Bayerische Meisterschaft', city='Sulzbach- Rosenberg',
               jtr_link='https://turniere.jugger.org/tournament.php?id=200'),
    Tournament(name='2. Frängsche Meisterschaft', city='Nürnberg',
               jtr_link='https://turniere.jugger.org/tournament.php?id=211'),
    Tournament(name='7. Hessische Meisterschaft', city='Darmstadt',
               jtr_link='https://turniere.jugger.org/tournament.php?id=231'),
    Tournament(name='1. Juggerturnier am Hohen Ufer', city='Hannover',
               jtr_link='https://turniere.jugger.org/tournament.php?id=207'),
    Tournament(name='2. Südwest Regionalturnier', city='Homburg',
               jtr_link='https://turniere.jugger.org/tournament.php?id=192'),
    Tournament(name='9. Saarländische Meisterschaft', city='Homburg',
               jtr_link='https://turniere.jugger.org/tournament.php?id=194'),
    Tournament(name='13. Badische Meisterschaft', city='Villingen',
               jtr_link='https://turniere.jugger.org/tournament.php?id=196'),
    Tournament(name='Holt euch die Banane! 2015', city='Sulzbach-Rosenberg',
               jtr_link='https://turniere.jugger.org/tournament.php?id=195'),
    Tournament(name='1. Karlsruher Pömmelturnier', city='Karlsruhe',
               jtr_link='https://turniere.jugger.org/tournament.php?id=199'),
    Tournament(name='3. Göttinger Winterturnier', city='Göttingen',
               jtr_link='https://turniere.jugger.org/tournament.php?id=191'),
    Tournament(name='Open Jugger League 2014', city='Freiburg',
               jtr_link='https://turniere.jugger.org/tournament.php?id=186'),
    Tournament(name='7. Thüringer Meisterschaft (TM 2014)', city='Jena',
               jtr_link='https://turniere.jugger.org/tournament.php?id=150'),
    Tournament(name='6. Hessische Meisterschaft', city='Darmstadt',
               jtr_link='https://turniere.jugger.org/tournament.php?id=159'),
    Tournament(name='2. Bergische Meisterschaft', city='Wuppertal',
               jtr_link='https://turniere.jugger.org/tournament.php?id=177'),
    Tournament(name='12. Badische Meisterschaft ', city='Villingen',
               jtr_link='https://turniere.jugger.org/tournament.php?id=145'),
    Tournament(name='5. Hessische Meisterschaft', city='Darmstadt',
               jtr_link='https://turniere.jugger.org/tournament.php?id=125'),
    Tournament(name='8. Berliner Juggerpokal/ 7. Thüringer Meisterschaft'),
    Tournament(name='1. Mitteldeutsche Meisterschaft', city='Halle (Saale)',
               jtr_link='https://turniere.jugger.org/tournament.php?id=176'),
    Tournament(name='3. Berlin Masters (BM 2014)', city='Berlin',
               jtr_link='https://turniere.jugger.org/tournament.php?id=166'),
    Tournament(name='OWL 2014/15 - 1. Spieltag', city='Leipzig'),
    Tournament(name='OWL 2014/15 - 2. Spieltag', city='Jena'),
    Tournament(name='Mitteldeutsche Juggerliga 2015'),
    Tournament(name='Trainingsspiel Jugger Vienna', city='Wien'),
    Tournament(name='15. Deutsche Meisterschaft (DM 2012)', city='Berlin',
               jtr_link='https://turniere.jugger.org/tournament.php?id=72'),
    Tournament(name='OWL 2013/14', city='Cottbus'),
    Tournament(name='1. Berlin Masters (BM 2011)', city='Berlin',
               jtr_link='https://turniere.jugger.org/tournament.php?id=60'),
    Tournament(name='1. Juggerturnier zu Oldenburg', city='Oldenburg',
               jtr_link='https://turniere.jugger.org/tournament.php?id=56'),
    Tournament(name='7. Schleswig-Holstein Meisterschaft', city='Rethwisch',
               jtr_link='https://turniere.jugger.org/tournament.php?id=78'),
    Tournament(name='6. Berliner Juggerpokal (BJP 2012)', city='Berlin',
               jtr_link='https://turniere.jugger.org/tournament.php?id=79'),
    Tournament(name='5. Thüringer Meisterschaft (TM 2012)', city='Jena',
               jtr_link='https://turniere.jugger.org/tournament.php?id=74'),
    Tournament(name='OWL 2012/13', city='Greifswald'),
    Tournament(name='7. Berliner Juggerpokal (BJP 2013)', city='Berlin',
               jtr_link='https://turniere.jugger.org/tournament.php?id=112'),
    Tournament(name='1. Hanseatic Jugger Cup', city='Lübeck',
               jtr_link='https://turniere.jugger.org/tournament.php?id=105'),
    Tournament(name='8. Schleswig-Holstein Meisterschaft', city='Rethwisch',
               jtr_link='https://turniere.jugger.org/tournament.php?id=114'),
    Tournament(name='2. Berlin Masters (BM 2013)', city='Berlin',
               jtr_link='https://turniere.jugger.org/tournament.php?id=104'),
    Tournament(name='8. Berliner Juggerpokal (BJP 2014)', city='Berlin',
               jtr_link='https://turniere.jugger.org/tournament.php?id=112'),
    Tournament(name='2. Hallesche Stadtbalgerei', city='Halle (Saale)',
               jtr_link='https://turniere.jugger.org/tournament.php?id=109'),
    Tournament(name='19. Hamburger Meisterschaft', city='Hamburg',
               jtr_link='https://turniere.jugger.org/tournament.php?id=131'),
    Tournament(name='6. Thüringer Meisterschaft (TM 2013)', city='Jena',
               jtr_link='https://turniere.jugger.org/tournament.php?id=113'),
    Tournament(name='3. Stuttgarter Kessel-Cup', city='Stuttgart',
               jtr_link='https://turniere.jugger.org/tournament.php?id=565'),
    Tournament(name='3. Württemberg Cup', city='Lauffen am Neckar',
               jtr_link='https://turniere.jugger.org/tournament.php?id=531'),
    Tournament(name='1. Bonner Wintercup', city='Bonn', jtr_link='https://turniere.jugger.org/tournament.php?id=320'),
    Tournament(name='2. Bonner Wintercup', city='Bonn', jtr_link='https://turniere.jugger.org/tournament.php?id=399'),
    Tournament(name='4. Bonner Wintercup', city='Bonn'),
    Tournament(name='Drake´s Landrattenregatta', city='Bonn'),
    Tournament(name='NRW WL 2015/16 ', city='#REF!'),
    Tournament(name='NRW WL 2016/17 ', city='Ahaus', jtr_link='https://turniere.jugger.org/tournament.php?id=308'),
    Tournament(name='1. Bonner Hafenderby ', city='Bonn'),
    Tournament(name='1. Bonner Hafenderby', city='Bonn'),
    Tournament(name='10. Berliner Juggerpokal (BJP 2016)', city='Berlin',
               jtr_link='https://turniere.jugger.org/tournament.php?id=258'),
    Tournament(name='12. Berliner Juggerpokal (BJP 2018)', city='Berlin',
               jtr_link='https://turniere.jugger.org/tournament.php?id=415'),
    Tournament(name='7. Berlin Masters (BM 2018)', city='Berlin',
               jtr_link='https://turniere.jugger.org/tournament.php?id=411'),
    Tournament(name='11. Thüringer Meisterschaft (TM 2018)', city='Jena',
               jtr_link='https://turniere.jugger.org/tournament.php?id=405'),
    Tournament(name='12. Schleswig- Holstein Meisterschaft', city='Rethwisch',
               jtr_link='https://turniere.jugger.org/tournament.php?id=403'),
    Tournament(name='5. Mitteldeutsche Meisterschaft', city='Halle (Saale)',
               jtr_link='https://turniere.jugger.org/tournament.php?id=398'),
    Tournament(name='24. Hamburger Meisterschaft', city='Hamburg',
               jtr_link='https://turniere.jugger.org/tournament.php?id=426'),
    Tournament(name='Sommerfest 2018', city='Berlin'),
    Tournament(name='21. Deutsche Meisterschaft (DM 2018)', city='Rethwisch',
               jtr_link='https://turniere.jugger.org/tournament.php?id=417'),
    Tournament(name='OWL 2018/19', city='Berlin'),
    Tournament(name='Einladungsturnier Potsdam 2020', city='Potsdam'),
    Tournament(name='OWL 2019/20', city='Jena'),
    Tournament(name='13. Schleswig-Holstein Meisterschaft', city='Rethwisch',
               jtr_link='https://turniere.jugger.org/tournament.php?id=467'),
    Tournament(name='1. World Club Championship (WCC 2018)', city='Darmstadt',
               jtr_link='https://turniere.jugger.org/tournament.php?id=412'),
    Tournament(name='6. Kieler Nordderby', city='Kiel', jtr_link='https://turniere.jugger.org/tournament.php?id=445'),
    Tournament(name='13. Berliner Juggerpokal (BJP 2019)', city='Berlin',
               jtr_link='https://turniere.jugger.org/tournament.php?id=492'),
    Tournament(name='8. Berlin Masters (BM 2019)', city='Berlin',
               jtr_link='https://turniere.jugger.org/tournament.php?id=455'),
    Tournament(name='9. Berlin Masters (BM 2020)', city='Berlin',
               jtr_link='https://turniere.jugger.org/tournament.php?id=569',
               tugeny_link='https://tugeny_link.org/tournaments/view/49'),
    Tournament(name='Rotenburger Stadtklopperei -Jugendturnier-', city='Roteburg a. d. Fulda',
               jtr_link='https://turniere.jugger.org/tournament.php?id=297'),
    Tournament(name='4. Bamberger Jugger Turnier - zur goldenen Pompfe', city='Bamberg',
               jtr_link='https://turniere.jugger.org/tournament.php?id=432'),
    Tournament(name='12. Thüringer Meisterschaft (TM 2019)', city='Jena',
               jtr_link='https://turniere.jugger.org/tournament.php?id=481'),
    Tournament(name='22. Deutsche Meisterschaft (DM 2019)', city='Jena',
               jtr_link='https://turniere.jugger.org/tournament.php?id=515'),
    Tournament(name='25. Hamburger Meisterschaft', city='Hamburg',
               jtr_link='https://turniere.jugger.org/tournament.php?id=500'),
    Tournament(name='Järnsvenskan 2019', city='Järnboås', jtr_link='https://turniere.jugger.org/tournament.php?id=483'),
    Tournament(name='14. Deutsche Meisterschaft (DM 2011)', city='Waidhaus',
               jtr_link='https://turniere.jugger.org/tournament.php?id=62'),
    Tournament(name='4. Freundschaftliche Winterspiele', city='Berlin',
               jtr_link='https://turniere.jugger.org/tournament.php?id=80'),
    Tournament(name='1. Berliner Juggerpokal (BJP 2007)', city='Berlin'),
    Tournament(name='13. Deutsche Meisterschaft (DM 2010)', city='Berlin',
               jtr_link='https://turniere.jugger.org/tournament.php?id=19'),
    Tournament(name='5. Berliner Juggerpokal (BJP 2011)', city='Berlin',
               jtr_link='https://turniere.jugger.org/tournament.php?id=53'),
    Tournament(name='11. Saarländische Meisterschaft', city='Homburg',
               jtr_link='https://turniere.jugger.org/tournament.php?id=314'),
    Tournament(name='2. Deutsche Meisterschaft für Kinder- und Jugendmannschaften (DKJM 2015)', city='Hagen',
               jtr_link='https://turniere.jugger.org/tournament.php?id=217'),
    Tournament(name='23. Hamburger Meisterschaft', city='Hamburg',
               jtr_link='https://turniere.jugger.org/tournament.php?id=364'),
    Tournament(name='NRW WL 2014/15', city='#REF!'),
    Tournament(name='2. TORNEO INTERNACIONAL DE ESPAÑA (TIE) 2017', city='Madrid',
               jtr_link='https://turniere.jugger.org/tournament.php?id=379'),
    Tournament(name='NRW WL 2013/14', city='Hagen'),
    Tournament(name='4. NRW Turnier', city='Duisburg', jtr_link='https://turniere.jugger.org/tournament.php?id=170'),
    Tournament(name='12. Deutsche Meisterschaft (DM 2009)', city='Berlin',
               jtr_link='https://turniere.jugger.org/tournament.php?id=2'),
    Tournament(name='10. Deutsche Meisterschaft (DM 2007)', city='Berlin'),
    Tournament(name='Training', city='Berlin'),
    Tournament(name='17. Deutsche Meisterschaft (DM 2014)', city='Villingen',
               jtr_link='https://turniere.jugger.org/tournament.php?id=168'),
    Tournament(name='9. Berliner Juggerpokal (BJP 2015)', city='Berlin',
               jtr_link='https://turniere.jugger.org/tournament.php?id=203'),
    Tournament(name='Graf-Bernhard-Pokal 2016', city='Lippstadt',
               jtr_link='https://turniere.jugger.org/tournament.php?id=256'),
    Tournament(name='NRW WL 2017/18', city='#REF!'),
    Tournament(name='3. Westfälische Meisterschaft', city='Lippstadt',
               jtr_link='https://turniere.jugger.org/tournament.php?id=27'),
    Tournament(name='1. Lauffener Grabsteinturnier', city='Lauffen',
               jtr_link='https://turniere.jugger.org/tournament.php?id=471'),
    Tournament(name='1. NLG Spieltag', city='Lauffen', jtr_link='https://turniere.jugger.org/tournament.php?id=566'),
    Tournament(name='11. Hessische Meisterschaft', city='Darmstadt',
               jtr_link='https://turniere.jugger.org/tournament.php?id=510'),
    Tournament(name='18. Bayerische Meisterschaft', city='Waidhaus',
               jtr_link='https://turniere.jugger.org/tournament.php?id=495'),
    Tournament(name='2. SaarJuggerCup', city='Homburg', jtr_link='https://turniere.jugger.org/tournament.php?id=549'),
    Tournament(name='2. Württemberg Cup', city='Heilbronn',
               jtr_link='https://turniere.jugger.org/tournament.php?id=518'),
    Tournament(name='6. Deutsche Meisterschaft für Kinder- und Jugendmannschaften (DKJM 2019)', city='Berlin',
               jtr_link='https://turniere.jugger.org/tournament.php?id=486'),
    Tournament(name='4. Flensburger Nordstern Turnier', city='Flensburg',
               jtr_link='https://turniere.jugger.org/tournament.php?id=480'),
    Tournament(name='Paderborner Winterspieltag 19/20', city='Paderborn',
               jtr_link='https://turniere.jugger.org/tournament.php?id=533'),
    Tournament(name='Wuppertal WL-Spieltag 2019/20', city='Wuppertal',
               jtr_link='https://turniere.jugger.org/tournament.php?id=556'),
    Tournament(name='2. Hagener WL-Einladungsturnier', city='Hagen'),
    Tournament(name='NRW Winterliga 2019/20 Münster', city='Münster',
               jtr_link='https://turniere.jugger.org/tournament.php?id=539'),
    Tournament(name='Zoff im Pott im Winter', city='Bochum',
               jtr_link='https://turniere.jugger.org/tournament.php?id=524'),
    Tournament(name='Besten im Westen 2019', city='Paderborn',
               jtr_link='https://turniere.jugger.org/tournament.php?id=527'),
    Tournament(name='5. Juggerturnier am Hohen Ufer', city='Hannover',
               jtr_link='https://turniere.jugger.org/tournament.php?id=489'),
    Tournament(name='5. Turnier zu Münster', city='Münster',
               jtr_link='https://turniere.jugger.org/tournament.php?id=494'),
    Tournament(name='Zoff im Pott 2019', city='Bochum', jtr_link='https://turniere.jugger.org/tournament.php?id=469'),
    Tournament(name='6. Bergische Meisterschaft', city='Wuppertal',
               jtr_link='https://turniere.jugger.org/tournament.php?id=505'),
    Tournament(name='Kölner Sommerfest (Jurassic Cup) 2019', city='Köln'),
    Tournament(name='13. Saarländische Meisterschaft', city='Homburg',
               jtr_link='https://turniere.jugger.org/tournament.php?id=458'),
    Tournament(name='5 1/2 Bergische Meisterschaft', city='Wuppertal',
               jtr_link='https://turniere.jugger.org/tournament.php?id=435'),
    Tournament(name='NRW WL 2018/19', city='Padernborn', jtr_link='https://turniere.jugger.org/tournament.php?id=470'),
    Tournament(name='1. Ostrhauderfehner Juggerturnier', city='Ostrhauderfehn',
               jtr_link='https://turniere.jugger.org/tournament.php?id=452'),
    Tournament(name='15. Badische Meisterschaft', city='Freiburg'),
    Tournament(name='NRW WL 2017/18 ', city='Paderborn', jtr_link='https://turniere.jugger.org/tournament.php?id=418'),
    Tournament(name='4. Juggerturnier am Hohen Ufer', city='Hannover',
               jtr_link='https://turniere.jugger.org/tournament.php?id=430'),
    Tournament(name='5. Kieler Nordderby', city='Kiel', jtr_link='https://turniere.jugger.org/tournament.php?id=410'),
    Tournament(name='3. Hallenturnier zu Oldenburg', city='Oldenburg',
               jtr_link='https://turniere.jugger.org/tournament.php?id=378'),
    Tournament(name='Einladungsturnier Hagen 2018', city='Hagen'),
    Tournament(name='5. Bergische Meisterschaft', city='Wuppertal',
               jtr_link='https://turniere.jugger.org/tournament.php?id=328'),
    Tournament(name='2. Flensburger Nordstern Turnier', city='Flensburg',
               jtr_link='https://turniere.jugger.org/tournament.php?id=336'),
    Tournament(name='1. Rheinische Meisterschaft', city='Bonn',
               jtr_link='https://turniere.jugger.org/tournament.php?id=353'),
    Tournament(name='19. Deutsche Meisterschaft (DM 2016)', city='Waidhaus',
               jtr_link='https://turniere.jugger.org/tournament.php?id=284'),
    Tournament(name='2. Juggerturnier am Hohen Ufer', city='Hannover',
               jtr_link='https://turniere.jugger.org/tournament.php?id=279'),
    Tournament(name='4. Bergische Meisterschaft', city='Wuppertal',
               jtr_link='https://turniere.jugger.org/tournament.php?id=270'),
    Tournament(name='5. Hagener Jugger Cup ', city='Hagen',
               jtr_link='https://turniere.jugger.org/tournament.php?id=254'),
    Tournament(name='2. Rheinland-Pfälzische Meisterschaft ', city='Mainz',
               jtr_link='https://turniere.jugger.org/tournament.php?id=261'),
    Tournament(name='NRW WL 2015/16', city='Ahaus'),
    Tournament(name='3. Bergische Meisterschaft', city='Wuppertal',
               jtr_link='https://turniere.jugger.org/tournament.php?id=226'),
    Tournament(name='4. Hagener Jugger Cup', city='Hagen',
               jtr_link='https://turniere.jugger.org/tournament.php?id=190'),
    Tournament(name='8. Thüringer Meisterschaft (TM 2015)', city='Jena',
               jtr_link='https://turniere.jugger.org/tournament.php?id=201'),
    Tournament(name='NRW WL 2016/17', city='Ahaus'),
    Tournament(name='Irish International Tournament 2014', city='Dublin',
               jtr_link='https://turniere.jugger.org/tournament.php?id=409'),
    Tournament(name='Metallsvenskan Jugger Turnering 2015', city='Örebro',
               jtr_link='https://turniere.jugger.org/tournament.php?id=189'),
    Tournament(name='Respect Gaymes 2015', city='Berlin', jtr_link='https://turniere.jugger.org/tournament.php?id=209'),
    Tournament(name='4. Berlin Masters (BM 2015)', city='Berlin',
               jtr_link='https://turniere.jugger.org/tournament.php?id=214'),
    Tournament(name='2. Mitteldeutsche Meisterschaft', city='Halle (Saale)',
               jtr_link='https://turniere.jugger.org/tournament.php?id=213'),
    Tournament(name='1. Leipziger Juggernächte', city='Leipzig',
               jtr_link='https://turniere.jugger.org/tournament.php?id=225'),
    Tournament(name='21. Hamburger Meisterschaft', city='Hamburg',
               jtr_link='https://turniere.jugger.org/tournament.php?id=233'),
    Tournament(name='3. Greifswalder Strandturnier', city='Greifswald',
               jtr_link='https://turniere.jugger.org/tournament.php?id=229'),
    Tournament(name='GJL Playoff 2015', city='Berlin', jtr_link='https://turniere.jugger.org/tournament.php?id=204'),
    Tournament(name='Jenaer Neujahrjugger', city='Jena'),
    Tournament(name='OWL Frankfurt Oder', city='Frankfurt Oder'),
    Tournament(name='OWL Cottbus', city='Cottbus'),
    Tournament(name='1. Bergische Meisterschaft', city='Wuppertal',
               jtr_link='https://turniere.jugger.org/tournament.php?id=124'),
    Tournament(name='16. Deutsche Meisterschaft (DM 2013)', city='Berlin',
               jtr_link='https://turniere.jugger.org/tournament.php?id=127'),
    Tournament(name='Göttinger Hallencup 2014', city='Göttingen',
               jtr_link='https://turniere.jugger.org/tournament.php?id=163'),
    Tournament(name='14. Saarländische Meisterschaft', city='Homburg'),
    Tournament(name='WCC 2020+', city='Berlin'),
    Tournament(name='ANNE BONNY`S LANDRATTEN REGATTA', city='Bonn',
               jtr_link='https://turniere.jugger.org/tournament.php?id=593'),
    Tournament(name='14. Berliner Jugger Pokal (BJP 2022)', city='Berlin',
               jtr_link='https://turniere.jugger.org/tournament.php?id=614'),
    Tournament(name='14. Berliner Jugger Pokal', city='Berlin'),
    Tournament(name='Turnier in Hannover', city='Hannover'),
    Tournament(name='4. Thüringer Meisterschaft (TM 2011)', city='Jena'),
    Tournament(name='Göttinger Hallencup 2012', city='Göttingen'),
    Tournament(name='1. Hagener Juggercup', city='Hagen'),
    Tournament(name='5. Westfälische Meisterschaft', city='Lippstadt',
               jtr_link='https://turniere.jugger.org/tournament.php?id=87'),
    Tournament(name='2. Hagener Jugger Cup', city='Hagen',
               jtr_link='https://turniere.jugger.org/tournament.php?id=103'),
    Tournament(name='3. Oldenburger Kreismeisteschaft', city='Oldenburg',
               jtr_link='https://www.youtube.com/channel/UCLOZntsDJrCsWxeqfzyGMww'),
    Tournament(name='Järnsvenskan 2018', city='Järnboås', jtr_link='https://turniere.jugger.org/tournament.php?id=377'),
    Tournament(name='NRW-Winterliga 2019', city='Wuppertal'),
    Tournament(name='12. Saarländische Meisterschaft', city='Homburg',
               jtr_link='https://turniere.jugger.org/tournament.php?id=389'),
    Tournament(name='2. Dorfturnier zu Kerwa', city='Kerwa'),
    Tournament(name='10. Badische Meisterschaft', city='Villingen',
               jtr_link='https://turniere.jugger.org/tournament.php?id=76'),
    Tournament(name='2. NLG Spieltag', city='Lauffen',
               jtr_link='https://turniere.jugger.org/tournament.result.php?id=568'),
    Tournament(name='Göttinger Hallencup 2014', city='Göttingen'),
    Tournament(name='OWL Spieltag Cottbus 2014', city='Cottbus'),
    Tournament(name='1. Jugger Event Schmalkalden', city='Schmalkalden'),
    Tournament(name='5. Torneo Nacional de Zaragoza (TNZ 2014)', city='Zaragoza'),
    Tournament(name='10. Thüringer Meisterschaft (TM 2017)', city='Jena'),
    Tournament(name='11. Berliner Juggerpokal (BJP 2017)', city='Berlin'),
    Tournament(name='3. Frängsche Meisterschaft', city='Erlangen'),
    Tournament(name='9. Thüringer Meisterschaft (TM 2016)', city='Jena',
               jtr_link='https://turniere.jugger.org/tournament.result.php?id=278'),
    Tournament(name='3. Mitteldeutsche Meisterschaft', city='Halle (Saale)',
               jtr_link='https://turniere.jugger.org/tournament.result.php?id=272'),
    Tournament(name='OWL 2015/2016', city='Jena'),
    Tournament(name='6. Torneo nacional Zaragoza (TNZ 2015)', city='Zaragoza'),
    Tournament(name='OWL 2014/2015', city='#REF!'),
    Tournament(name='10. Saarländische Meisterschaft', city='Homburg'),
    Tournament(name='4. Rheinland-Pfälzische Meisterschaft', city='Mainz'),
    Tournament(name='5. Südwest Regionalturnier', city='Homburg',
               jtr_link='https://turniere.jugger.org/tournament.result.php?id=388'),
    Tournament(name='1. Bremer Landesmeisterschaft', city='Bremen',
               jtr_link='https://turniere.jugger.org/tournament.php?id=158'),
    Tournament(name='1. Ruhrpott-Pott', city='Bochum', jtr_link='https://turniere.jugger.org/tournament.php?id=174'),
    Tournament(name='2. Kampf um die rote Stadt', city='Rotenburg (Wümme)',
               jtr_link='https://turniere.jugger.org/tournament.php?id=198'),
    Tournament(name='4. TORNEO INTERNACIONAL DE ESPAÑA (TIE) 2019', city='Madrid'),
    Tournament(name='I Regional Alicantino', city='Alicante'),
    Tournament(name='X Open Murcia', city='Murcia'),
    Tournament(name='V Liga Murciana', city='Murcia'),
    Tournament(name='3. TORNEO INTERNACIONAL DE ESPAÑA (TIE) 2018', city='Madrid'),
    Tournament(name='1. Atún Cup (AC 2010)', city='Madrid'),
    Tournament(name='Liga Vanciana de Jugger', city='Valencia'),
    Tournament(name='Torneo Jugger Cromel 2011'),
    Tournament(name='Juggerslam'),
    Tournament(name='2. Summer Cup 2011', city='Valencia'),
    Tournament(name='2. Atún Cup (AC 2011)', city='Madrid'),
    Tournament(name='2. Torneo Future', city='Valencia'),
    Tournament(name='Liga Valenciana de los Retos', city='Valencia'),
    Tournament(name='3. Liga Valenciana de Jugger', city='Valencia'),
    Tournament(name='2nd Austrian Jugger Open', city='Wien'),
    Tournament(name='5. Deutsche Meisterschaft für Kinder- und Jugendmannschaften (DKJM 2018)', city='Halle (Saale)'),
    Tournament(name='1. Berlin Masters der Kinder (BMK 2016)', city='Berlin'),
    Tournament(name='5. Berlin Masters (BM 2016)', city='Berlin'),
    Tournament(name='3. Deutsche Meisterschaft für Kinder- und Jugendmannschaften (DKJM 2016)', city='Rethwisch'),
    Tournament(name='4. Berliner Juggerpokal der Jugend (BJPJ 2015)', city='Berlin'),
    Tournament(name='4. Berliner Juggerpokal der Kinder (BJPK 2015)', city='Berlin'),
    Tournament(name='5. Atún Cup (AC 2014)', city='Madrid'),
    Tournament(name='3. Berliner Juggerpokal der Kinder (BJPK 2014)', city='Berlin'),
    Tournament(name='1. Deutsche Meisterschaft für Kinder- und Jugendmannschaften (DKJM 2014)',
               city='Rothenburg a.d. Fulda'),
    Tournament(name='1. Berliner Juggerpokal der Jugend (BJPJ 2013)', city='Berlin'),
    Tournament(name='9. Summer Cup', city='Astillero'),
    Tournament(name='6. Spring Cup'),
    Tournament(name='Irish International Tournament 2018', city='Dublin'),
    Tournament(name='Järnsvenskan 2017', city='Järnboas', jtr_link='https://turniere.jugger.org/tournament.php?id=321'),
    Tournament(name='Irish International Tournament 2016', city='Dublin',
               jtr_link='https://turniere.jugger.org/tournament.php?id=283'),
    Tournament(name='1. TORNEO INTERNACIONAL DE ESPAÑA (TIE) 2016', city='Madrid',
               jtr_link='https://turniere.jugger.org/tournament.php?id=289'),
    Tournament(name='22. Hamburger Meisterschaft', city='Hamburg',
               jtr_link='https://turniere.jugger.org/tournament.php?id=294'),
    Tournament(name='3. Winter Cup 2015'),
    Tournament(name='8. Winter Cup 2020'),
    Tournament(name='7. Winter Cup 2019', city='Murcia'),
    Tournament(name='6. Winter Cup 2018', city='Murcia'),
    Tournament(name='1. Open 2. Levante Jugger League'),
    Tournament(name='3. Liga Jugger Murcia', city='Murcia'),
    Tournament(name='3. Atún Cup (AC 2012)', city='Madrid'),
    Tournament(name='1. Winter Cup 2013', city='Murcia'),
    Tournament(name='6. Regional  Jugger Murcia', city='Murcia'),
    Tournament(name='7. Regional Jugger Murcia', city='Murcia'),
    Tournament(name='4. Württemberg Cup', city='Lauffen',
               jtr_link='https://turniere.jugger.org/tournament.result.php?id=570'),
    Tournament(name='7. Südwest Regionalturnier', city='Homburg'),
    Tournament(name='13. Thüringer Meisterschaft (TM 21)', city='Jena',
               jtr_link='https://turniere.jugger.org/tournament.php?id=579',
               tugeny_link='https://tugeny_link.org/tournaments/tm-2021/all-teams'),
    Tournament(name='2. Lauffener Grabsteinturnier', city='Lauffen',
               jtr_link='https://turniere.jugger.org/tournament.php?id=582'),
    Tournament(name='10. Berlin Masters (BM 2021)', city='Berlin',
               jtr_link='https://turniere.jugger.org/tournament.php?id=529',
               tugeny_link='https://tugeny_link.org/tournaments/10-berlin-masters/all-teams'),
    Tournament(name='6. Bamberger Juggerturnier - zur Goldenen Pompfe', city='Bamberg',
               jtr_link='https://turniere.jugger.org/tournament.result.php?id=581'),
    Tournament(name='1. Berlin Minors', city='Berlin', jtr_link='https://turniere.jugger.org/tournament.php?id=577'),
    Tournament(name='5. Württemberg Cup', city='Lauffen',
               jtr_link='https://turniere.jugger.org/tournament.result.php?id=571',
               tugeny_link='https://tugeny_link.org/tournaments/5-wuerttemberg-cup-wcc-afterparty/all-teams'),
    Tournament(name='Bonner Buccaneer Brawl (BBB 21)', city='Bonn',
               jtr_link='https://turniere.jugger.org/tournament.result.php?id=590',
               tugeny_link='https://tugeny_link.org/tournaments/bonner-buccaneer-brawl/all-teams'),
    Tournament(name='Einladungsturnier Winterliga in Hagen 1/3',
               jtr_link='https://turniere.jugger.org/tournament.result.php?id=595',
               tugeny_link='https://tugeny_link.org/tournaments/einladungsturnier-winterliga-in-hagen-1-3/all-teams'),
    Tournament(name='Einladungsturnier Winterliga in Hagen 2/3', city='Hagen',
               jtr_link='https://turniere.jugger.org/tournament.result.php?id=596',
               tugeny_link='https://tugeny_link.org/tournaments/einladungsturnier-winterliga-in-hagen-2-3/all-teams'),
    Tournament(name='Einladungsturnier Winterliga in Hagen 3/3', city='Hagen',
               jtr_link='https://turniere.jugger.org/tournament.php?id=597'),
    Tournament(name='5. Bonner Wintercup', city='Bonn',
               jtr_link='https://turniere.jugger.org/tournament.result.php?id=591',
               tugeny_link='https://tugeny_link.org/tournaments/5-bonner-wintercup/all-teams'),
    Tournament(name='Einladungsturnier Speyer 2022', city='Speyer'),
    Tournament(name='1. Strandturnier in Rostock', city='Rostock',
               jtr_link='https://turniere.jugger.org/tournament.php?id=583'),
    Tournament(name='14. Thüringer Meisterschaft (TM 22)', city='Jena',
               jtr_link='https://turniere.jugger.org/tournament.result.php?id=607'),
    Tournament(name='4. Jugger.cz Open 2022', city='Prag'),
    Tournament(name='11. Berlin Masters (BM 2022)', city='Berlin',
               jtr_link='https://turniere.jugger.org/tournament.result.php?id=599'),
    Tournament(name='Schattentheater', city='Würzburg'),
    Tournament(name='6. Württemberg Cup', city='Lauffen', jtr_link='https://turniere.jugger.org/tournament.php?id=625',
               tugeny_link='https://tugeny_link.org/tournaments/6-wuerttemberg-cup/all-teams'),
    Tournament(name='Wessi Wettstreit', city='Bonn', jtr_link='https://turniere.jugger.org/tournament.php?id=626'),
    Tournament(name='6. Leipziger Juggernächte', city='Leipzig',
               jtr_link='https://turniere.jugger.org/tournament.result.php?id=605'),
    Tournament(name='7. Bamberger Juggerturnier - zur Goldenen Pompfe', city='Bamberg',
               jtr_link='https://turniere.jugger.org/tournament.result.php?id=609'),
    Tournament(name='3. Rheinische Meisterschaft', city='Bonn',
               jtr_link='https://turniere.jugger.org/tournament.result.php?id=628'),
    Tournament(name='5. Lahnveilchencup-Cake', city='Gießen',
               jtr_link='https://turniere.jugger.org/tournament.result.php?id=619'),
    Tournament(name='14. Schleswig-Holstein Meisterschaft', city='Rethwisch',
               jtr_link='https://turniere.jugger.org/tournament.php?id=602'),
    Tournament(name='6. Turnier zu Münster', city='Münster',
               jtr_link='https://turniere.jugger.org/tournament.php?id=620',
               tugeny_link='https://tugeny_link.org/tournaments/6-turnier-zu-muenster/all-teams'),
    Tournament(name='7. Bergische Meisterschaft', city='Wuppertal'),
    Tournament(name='23. Deutsche Meisterschaft (DM 22)', city='Berlin',
               jtr_link='https://turniere.jugger.org/tournament.php?id=630',
               tugeny_link='https://tugeny_link.org/tournaments/23-deutsche-meisterschaft/all-teams'),
    Tournament(name='3. königlich-sächsisches Hofturnier', city='Dresden',
               jtr_link='https://turniere.jugger.org/tournament.result.php?id=615'),
    Tournament(name='Kampf um den goldenen Jugg', city='Speyer',
               jtr_link='https://turniere.jugger.org/tournament.result.php?id=631'),
    Tournament(name='5. TORNEO INTERNACIONAL DE ESPAÑA (TIE) 2022', city='Madrid'),
    Tournament(name='7. Württemberg Cup', city='Lauffen',
               jtr_link='https://turniere.jugger.org/tournament.result.php?id=629'),
    Tournament(name='4. Ostdeutsche Meisterschaft', city='Frankfurt (Oder)',
               jtr_link='https://turniere.jugger.org/tournament.php?id=635'),
    Tournament(name='16.5 Badische Meisterschaft', city='Freiburg'),
    Tournament(name='FANTASTIC AWESOME JUGGER TOURNAMENT', city='Umea'),
    Tournament(name='Winterligaspiele Berlin 2022/23', city='Berlin'),
    Tournament(name='Winterligaspiele Berlin 2022/24', city='Berlin'),
    Tournament(name='3. königliches-sächsisches Hofturnier', city='Dresden'),
]

for tournament in tournaments:
    db.session.add(tournament)

db.session.commit()