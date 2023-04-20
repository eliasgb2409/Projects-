-- Oppgave 0
SELECT count (*) FROM film ;

-- DEL 1

--Oppgave 1
SELECT firstname, lastname, filmcharacter
FROM person
INNER JOIN filmparticipation AS fp ON (person.personid = fp.personid AND parttype = 'cast')
INNER JOIN film ON (film.filmid = fp.filmid AND title = 'Star Wars')
INNER JOIN filmcharacter AS fc ON (fp.partid = fc.partid);

--Oppgave 2
SELECT country, COUNT(filmid)
FROM filmcountry
GROUP BY country
ORDER BY COUNT(filmid) DESC

--Oppgave 3
SELECT country, AVG(CAST(time AS INTEGER))
FROM runningtime
WHERE time ~ '^\d+$' AND country IS NOT NULL
GROUP BY country
HAVING COUNT(country) >= 200
ORDER BY AVG(CAST(time AS INTEGER)) DESC;

--OR

SELECT country, AVG(CAST(time AS INTEGER)) AS avg_runtime
FROM runningtime
WHERE time ~ '^\d+$' AND country IS NOT NULL
GROUP BY country
HAVING COUNT(country) >= 200
ORDER BY avg_runtime DESC;

--Oppgave 4
SELECT title, COUNT(genre) AS genre_count
FROM film
INNER JOIN filmgenre AS fg ON(film.filmid = fg.filmid)
GROUP BY title
HAVING COUNT(genre) > 10
ORDER BY COUNT(genre)DESC,title
LIMIT 10

--Oppgave 5
WITH top_genre AS(
SELECT country, genre, COUNT(genre) AS tg
FROM filmcountry
INNER JOIN filmgenre AS fg ON(filmcountry.filmid = fg.filmid)
GROUP BY country, genre
ORDER BY tg DESC
),
avg_rank AS(
SELECT country, AVG(rank) AS average
FROM filmcountry
INNER JOIN filmrating ON (filmcountry.filmid = filmrating.filmid)
GROUP BY country
),
total_films AS(
SELECT country, COUNT(filmid) AS counter
FROM filmcountry
GROUP BY country
)

SELECT c.country, (SELECT genre FROM top_genre WHERE c.country = top_genre.country LIMIT 1),
(SELECT average FROM avg_rank WHERE c.country = avg_rank.country),
(SELECT counter FROM total_films WHERE c.country = total_films.country)
FROM country AS c


--Oppgave 6

WITH actor AS (SELECT lastname, firstname, filmparticipation.partid AS parts, filmparticipation.filmid AS films
FROM filmparticipation
INNER JOIN person USING (personid)
INNER JOIN filmcountry AS fc ON (fc.filmid = filmparticipation.filmid
AND country = 'Norway')
INNER JOIN filmitem ON (filmitem.filmid = filmparticipation.filmid AND filmitem.filmtype = 'C')
GROUP BY lastname, firstname, filmparticipation.partid,filmparticipation.filmid )

SELECT DISTINCT actor.lastname, actor.firstname, a2.lastname, a2.firstname
FROM actor
INNER JOIN actor AS a2 USING (films)
WHERE actor.lastname != a2.lastname AND actor.lastname > a2.lastname
GROUP BY actor.lastname, actor.firstname, a2.lastname, a2.firstname
HAVING COUNT(actor.parts) > 40 AND COUNT(a2.parts) > 40
--Del 2

--Oppgave 7


(SELECT prodyear, title
FROM film
INNER JOIN filmcountry AS fc ON (fc.filmid = film.filmid)
WHERE (title LIKE '%Dark%' OR title LIKE '%Night%') AND fc.country = 'Romania')
UNION
(SELECT prodyear, title
FROM film
INNER JOIN filmgenre AS fg ON (fg.filmid = film.filmid)
WHERE (title LIKE '%Dark%' OR title LIKE '%Night%')
AND genre = 'Horror')

---Oppgave 8

SELECT title, COUNT(partid)
FROM film
INNER JOIN filmparticipation AS fp ON(fp.filmid = film.filmid)
GROUP BY title, film.prodyear
HAVING CAST(film.prodyear AS int) >= 2010 AND COUNT(partid) <= 2;

--Oppgave 9
SELECT COUNT(filmid)
FROM film
INNER JOIN filmgenre USING (filmid)
WHERE filmgenre.genre != 'Sci-fi' OR filmgenre.genre != 'Horror'

--Oppgave 10

WITH votes AS(
	SELECT film.title AS title, film.filmid AS id
	FROM film
	INNER JOIN filmrating USING (filmid)
	INNER JOIN filmitem USING (filmid)
	WHERE rank >= 8 AND votes > 1000 AND filmtype = 'C'
	ORDER BY rank DESC, votes DESC
),
actor AS (
	(SELECT film.filmid AS id, film.title AS title FROM film
	INNER JOIN filmparticipation as fp ON (fp.filmid = film.filmid)
	INNER JOIN person AS p ON (fp.personid = p.personid)
	INNER JOIN filmgenre as g ON (film.filmid = g.filmid)
	INNER JOIN votes ON (votes.id = film.filmid)
	WHERE (p.lastname = 'Ford' AND p.firstname = 'Harrison')
	OR (g.genre = 'Comedy' OR g.genre = 'Romance')
	)
	UNION
	(SELECT votes.id, votes.title FROM votes LIMIT 10)

)SELECT actor.title, COUNT(fg.filmid) FROM actor
LEFT JOIN filmlanguage AS fg ON (fg.filmid = actor.id)
GROUP BY actor.title
