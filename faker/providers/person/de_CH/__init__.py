# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats = (
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}-{{last_name}}',
        '{{first_name_female}} {{last_name}} {{last_name}}',
        '{{prefix}} {{first_name}} {{last_name}}',
    )

    first_names_male = (
        'Adolf', 'Adrian', 'Alain', 'Albert', 'Alberto', 'Aldo', 'Alex',
        'Alexander', 'Alexandre', 'Alfons', 'Alfred', 'Alois', 'Andre',
        'Andrea', 'Andreas', 'André', 'Angelo', 'Antoine', 'Anton', 'Antonio',
        'Armin', 'Arnold', 'Arthur', 'Beat', 'Bernard', 'Bernhard', 'Bruno',
        'Carlo', 'Charles', 'Christian', 'Christoph', 'Christophe', 'Claude',
        'Claudio', 'Daniel', 'David', 'Denis', 'Didier', 'Dieter', 'Dominique',
        'Edgar', 'Eduard', 'Edwin', 'Emil', 'Enrico', 'Eric', 'Erich', 'Ernst',
        'Erwin', 'Eugen', 'Felix', 'Ferdinand', 'Francesco', 'Francis',
        'Franco', 'Franz', 'François', 'Fredy', 'Fridolin', 'Friedrich',
        'Fritz', 'Frédéric', 'Georg', 'Georges', 'Gerhard', 'Gianni',
        'Gilbert', 'Giovanni', 'Giuseppe', 'Gottfried', 'Guido', 'Guy',
        'Gérald', 'Gérard', 'Hans', 'Hans-Peter', 'Hans-Rudolf', 'Hans-Ulrich',
        'Hansjörg', 'Hanspeter', 'Hansruedi', 'Heinrich', 'Heinz', 'Helmut',
        'Henri', 'Herbert', 'Hermann', 'Hubert', 'Hugo', 'Jacques', 'Jakob',
        'Jan', 'Jean', 'Jean-Claude', 'Jean-Daniel', 'Jean-François',
        'Jean-Jacques', 'Jean-Louis', 'Jean-Luc', 'Jean-Marc', 'Jean-Marie',
        'Jean-Paul', 'Jean-Pierre', 'Johann', 'Johannes', 'Josef', 'Joseph',
        'Jörg', 'Jürg', 'Karl', 'Klaus', 'Konrad', 'Kurt', 'Laurent', 'Leo',
        'Louis', 'Luigi', 'Manfred', 'Manuel', 'Marc', 'Marcel', 'Marco',
        'Mario', 'Markus', 'Martin', 'Massimo', 'Matthias', 'Maurice', 'Max',
        'Michael', 'Michel', 'Nicolas', 'Niklaus', 'Norbert', 'Olivier',
        'Oskar', 'Otto', 'Paolo', 'Pascal', 'Patrick', 'Paul', 'Peter',
        'Philipp', 'Pierre', 'Pierre-Alain', 'Pierre-André', 'Rainer',
        'Raymond', 'Reinhard', 'Remo', 'Renato', 'Rene', 'René', 'Reto',
        'Richard', 'Robert', 'Roberto', 'Roger', 'Roland', 'Rolf', 'Roman',
        'Rudolf', 'Ruedi', 'Samuel', 'Sandro', 'Serge', 'Silvio', 'Simon',
        'Stefan', 'Stephan', 'Stéphane', 'Theo', 'Theodor', 'Thomas', 'Toni',
        'Ueli', 'Ulrich', 'Urs', 'Victor', 'Viktor', 'Walter', 'Werner',
        'Willi', 'Willy', 'Wolfgang', 'Yves',
    )

    first_names_female = (
        'Alice', 'Andrea', 'Anita', 'Anna', 'Anne', 'Anne-Marie', 'Annemarie',
        'Astrid', 'Barbara', 'Beatrice', 'Bernadette', 'Brigitta', 'Brigitte',
        'Béatrice', 'Carmen', 'Catherine', 'Chantal', 'Christiane',
        'Christina', 'Christine', 'Claudia', 'Claudine', 'Corinne', 'Cornelia',
        'Daniela', 'Danielle', 'Denise', 'Dominique', 'Dora', 'Doris', 'Edith',
        'Eliane', 'Elisabeth', 'Elsbeth', 'Erika', 'Esther', 'Eva', 'Evelyne',
        'Fabienne', 'Florence', 'Franziska', 'Françoise', 'Gabriela',
        'Gabrielle', 'Gertrud', 'Gisela', 'Heidi', 'Helen', 'Helena', 'Helene',
        'Hildegard', 'Irene', 'Isabelle', 'Jacqueline', 'Janine', 'Jeannette',
        'Johanna', 'Jolanda', 'Josiane', 'Judith', 'Karin', 'Katharina',
        'Laura', 'Laurence', 'Liliane', 'Liselotte', 'Lydia', 'Madeleine',
        'Manuela', 'Margrit', 'Margrith', 'Maria', 'Marianne', 'Marlies',
        'Marlis', 'Martha', 'Martina', 'Martine', 'Maya', 'Monica', 'Monika',
        'Monique', 'Myriam', 'Nathalie', 'Nelly', 'Nicole', 'Paola',
        'Patricia', 'Petra', 'Pia', 'Priska', 'Regina', 'Regula', 'Renata',
        'Renate', 'Rita', 'Rosemarie', 'Rosmarie', 'Ruth', 'Sabine', 'Sandra',
        'Silvia', 'Simone', 'Sonja', 'Susanna', 'Susanne', 'Suzanne', 'Sylvia',
        'Therese', 'Ursula', 'Verena', 'Vreni', 'Véronique', 'Yvonne',
    )

    first_names = first_names_male + first_names_female

    last_names = (
        'Ackermann', 'Aebi', 'Albrecht', 'Ammann', 'Amrein', 'Arnold',
        'Bachmann', 'Bader', 'Bär', 'Bättig', 'Bauer', 'Baumann',
        'Baumgartner', 'Baur', 'Beck', 'Benz', 'Berger', 'Bernasconi',
        'Betschart', 'Bianchi', 'Bieri', 'Blaser', 'Blum', 'Bolliger',
        'Bosshard', 'Braun', 'Brun', 'Brunner', 'Bucher', 'Bühler', 'Bühlmann',
        'Burri', 'Christen', 'Egger', 'Egli', 'Eichenberger', 'Erni', 'Ernst',
        'Eugster', 'Fankhauser', 'Favre', 'Fehr', 'Felber', 'Felder',
        'Ferrari', 'Fischer', 'Flückiger', 'Forster', 'Frei', 'Frey', 'Frick',
        'Friedli', 'Fuchs', 'Furrer', 'Gasser', 'Geiger', 'Gerber', 'Gfeller',
        'Giger', 'Gloor', 'Graf', 'Grob', 'Gross', 'Gut', 'Haas', 'Häfliger',
        'Hafner', 'Hartmann', 'Hasler', 'Hauser', 'Hermann', 'Herzog', 'Hess',
        'Hirt', 'Hodel', 'Hofer', 'Hoffmann', 'Hofmann', 'Hofstetter', 'Hotz',
        'Huber', 'Hug', 'Hunziker', 'Hürlimann', 'Imhof', 'Isler', 'Iten',
        'Jäggi', 'Jenni', 'Jost', 'Kägi', 'Kaiser', 'Kälin', 'Käser',
        'Kaufmann', 'Keller', 'Kern', 'Kessler', 'Knecht', 'Koch', 'Kohler',
        'Kuhn', 'Küng', 'Kunz', 'Lang', 'Lanz', 'Lehmann', 'Leu', 'Leunberger',
        'Lüscher', 'Lustenberger', 'Lüthi', 'Lutz', 'Mäder', 'Maier', 'Marti',
        'Martin', 'Maurer', 'Mayer', 'Meier', 'Meili', 'Meister', 'Merz',
        'Mettler', 'Meyer', 'Michel', 'Moser', 'Müller', 'Näf', 'Ott', 'Peter',
        'Pfister', 'Portmann', 'Probst', 'Rey', 'Ritter', 'Roos', 'Roth',
        'Rüegg', 'Schäfer', 'Schaller', 'Schär', 'Schärer', 'Schaub',
        'Scheidegger', 'Schenk', 'Scherrer', 'Schlatter', 'Schmid', 'Schmidt',
        'Schneider', 'Schnyder', 'Schoch', 'Schuler', 'Schumacher', 'Schürch',
        'Schwab', 'Schwarz', 'Schweizer', 'Seiler', 'Senn', 'Sidler',
        'Siegrist', 'Sigrist', 'Spörri', 'Stadelmann', 'Stalder', 'Staub',
        'Stauffer', 'Steffen', 'Steiger', 'Steiner', 'Steinmann', 'Stettler',
        'Stocker', 'Stöckli', 'Stucki', 'Studer', 'Stutz', 'Suter', 'Sutter',
        'Tanner', 'Thommen', 'Tobler', 'Vogel', 'Vogt', 'Wagner', 'Walder',
        'Walter', 'Weber', 'Wegmann', 'Wehrli', 'Weibel', 'Wenger',
        'Wettstein', 'Widmer', 'Winkler', 'Wirth', 'Wirz', 'Wolf', 'Wüthrich',
        'Wyss', 'Zbinden', 'Zehnder', 'Ziegler', 'Zimmermann', 'Zingg',
        'Zollinger', 'Zürcher',
    )

    prefixes = ('Dr.', 'Prof.',)
