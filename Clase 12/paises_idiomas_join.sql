-- seleccion de los paises que hablan inglés
-- y la población que habla inglés en cada país
SELECT c.name AS "Nombre del pais", (cl.percentage*c.population)/100 AS "Población que habla inglés" FROM countrylanguage AS cl
JOIN country AS c
ON cl.countrycode = c.code
WHERE cl.isofficial = true AND cl.language = 'English' AND cl.percentage > 0
ORDER BY "Población que habla inglés" DESC;