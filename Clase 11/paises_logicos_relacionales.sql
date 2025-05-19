--paises que no son de Asia ni Europa y son republicas
SELECT * FROM country WHERE NOT(continent = 'Asia' OR continent = 'Europe') AND (governmentform = 'Republic') ORDER BY population ASC;
--paises que son de Europa o America del Norte
SELECT * FROM country WHERE continent IN('Europe','North America');
--paises sin datos de expectativa de vida
SELECT * FROM country WHERE lifeexpectancy IS NULL;