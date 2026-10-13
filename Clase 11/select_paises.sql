--Paises independientes
SELECT name,continent,region,indepyear 
FROM country 
WHERE indepyear IS NOT NULL;
--Paises con expectativa de vida mayor a 60
SELECT name,population,lifeexpectancy 
FROM country 
WHERE lifeexpectancy > 60;
--Paises que no son republicas
SELECT name,region,governmentform,headofstate 
FROM country 
WHERE governmentform <> 'Republic' 
AND governmentform <> 'Federal Republic';
--Paises que se independizaron de la union sovietica
SELECT name,region,indepyear 
FROM country 
WHERE indepyear = 1991 
AND region <> 'Southern Europe';
--Paises entre 10mil y 100mil metros cuadrados
SELECT name,region,surfacearea 
FROM country 
WHERE surfacearea <= 100000 
AND surfacearea >= 10000;