--Elegir todos los paises
SELECT * FROM country;
--Contar todos los paises
SELECT COUNT(*) FROM country;
--Contar los paises con expectativa de vida no nula
SELECT COUNT(lifeexpectancy) FROM country;
--Sumar la poblacion de Asia
SELECT SUM(population) FROM country WHERE continent='Asia';
--La mayor poblacion de Oceanía
SELECT MAX(population) FROM country WHERE continent='Oceania';
--La menor poblacion de Sudamérica
SELECT MIN(population) FROM country WHERE continent='South America';
--Los paises con extectativa de vida mayor a la media
SELECT * FROM country WHERE lifeexpectancy > (SELECT AVG(lifeexpectancy) FROM country);
--Población total de los continentes
SELECT continent,sum(population) FROM country GROUP BY continent;
--Superficie total de los continentes
SELECT region, sum(surfacearea) FROM country GROUP BY region;
--Superficie total de los continentes con superficie media mayor a 100000
SELECT region, sum(surfacearea) FROM country GROUP BY region HAVING avg(surfacearea) > 100000;