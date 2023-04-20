--DEL 1--

--Oppgave 2

--a)

SELECT navn
FROM planet
WHERE stjerne = 'Proxima Centauri';

--b)

SELECT DISTINCT oppdaget
FROM planet
WHERE stjerne = 'TRAPPIST-1' or stjerne = 'Kepler-154';


--c)

SELECT COUNT(*)-COUNT(masse) As masse
FROM planet;


--d)

SELECT navn, masse
FROM planet
WHERE oppdaget = '2020' and masse > (SELECT AVG(masse) FROM planet);

--e)

SELECT (MAX(oppdaget) - MIN(oppdaget))
FROM planet;


--Oppgave 3

--a)

SELECT navn
FROM planet INNER JOIN materie
	ON(navn = materie.planet)
WHERE planet.masse BETWEEN 3 and 10 AND
      molekyl = 'H2O';

--b)

SELECT DISTINCT planet.navn
FROM planet INNER JOIN stjerne ON (planet.stjerne = stjerne.navn)
	        INNER JOIN materie ON (planet.navn = materie.planet)
WHERE materie.molekyl LIKE '%H%' AND stjerne.avstand < (12*stjerne.masse);


--c)

SELECT pl.navn
FROM planet AS pl 
INNER JOIN stjerne ON (pl.stjerne = stjerne.navn AND stjerne.avstand < 50)
INNER JOIN planet AS pl2 ON (pl2.masse > 10)
WHERE pl.navn != pl2.navn AND pl.masse > 10 AND pl2.stjerne = pl.stjerne;

--Oppgave 4

/*

Denne spørringen vil ikke fungere da NATURAL JOIN slår sammen tabeller basert på
verdier fra kolonner med samme navn. I vårt tilfelle vil den forsøke å finne sammenligninger
med verdiene i kolonnonen "navn". Her er ingen av navnene like, derfor retunerer den 0 rader.

For at denne spørringen skal fungere, så kan man forsøke å skrive (tror jeg da..):

            SELECT planet.oppdaget
            FROM planet INNER JOIN stjerne on (planet.stjerne = stjerne.navn) 
            WHERE stjerne.avstand > 8000;

*/


--DEL 2--

--Oppgave 5

--a)

INSERT INTO stjerne
VALUES ('Sola', 0, 1);

--b) 

INSERT INTO planet
VALUES ('Jorda', 0.003146, NULL,'Sola');

--Oppgave 6

CREATE TABLE observasjon (
   observasjons_id int PRIMARY KEY,
   tidspunkt timestamp NOT NULL,
   planet text REFERENCES planet(navn) NOT NULL,
   kommentar text 
);




