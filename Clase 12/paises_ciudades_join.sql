-- Consulta para obtene el nombre del país, el nombre de la capital y la población de la capital
-- utilizando un LEFT JOIN entre las tablas country y city
/*SELECT country.name AS "Nombre del Pais", 
country.population AS "Población del Pais", 
city.name AS "Capital", city.population AS "Poblacion de la capital" 
FROM country
LEFT JOIN city
ON country.capital=city.id;*/

/*SELECT * FROM country
RIGHT JOIN city
ON country.capital=city.id;*/

-- Consulta para obtener el nombre de la ciudad, el nombre del país, el nombre local del país y la población de la ciudad
-- utilizando un RIGHT JOIN entre las tablas city y country
SELECT city.name AS "Nombre de la ciudad",
country.name AS "Nombre del pais",
country.localname AS "Nombre local del pais",
city.population AS "Población de la ciudad"
FROM city
RIGHT JOIN country
ON city.countrycode = country.code
WHERE city.population > 100000
ORDER BY city.population DESC;
