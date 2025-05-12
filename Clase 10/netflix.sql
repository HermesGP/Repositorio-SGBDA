--restaurar el backup netflix_backup.backup para probar estos SELECT
--el título, director y duración de las 30 peliculas americanas más viejas
SELECT title,director,duration FROM netflix_shows 
WHERE type='Movie' AND country='United States'
ORDER BY release_year ASC
LIMIT 30;
--el título y categorías de las 20 últimas series internacionales agregadas a netflix
SELECT title,listed_in FROM netflix_shows
WHERE type='TV Show' AND country<>'United States'
ORDER BY date_added DESC
LIMIT 20;
--el título y año de las 10 películas más largas de netflix
SELECT title,release_year FROM netflix_shows
WHERE type='Movie'
ORDER BY duration DESC
LIMIT 10;


