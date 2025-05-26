-- Script para crear las tablas de comidas y postres, insertar datos y mostrar un menú combinado
-- con el precio total de cada combinación
DROP TABLE IF EXISTS comidas;
DROP TABLE IF EXISTS postres;

CREATE TABLE comidas(
codigo SERIAL PRIMARY KEY,
nombre VARCHAR(50) NOT NULL,
precio NUMERIC NOT NULL
);

CREATE TABLE postres(
codigo SERIAL PRIMARY KEY,
nombre VARCHAR (50) NOT NULL,
precio NUMERIC NOT NULL
);

INSERT INTO comidas (nombre,precio) VALUES ('Tallarin',10000); 
INSERT INTO comidas (nombre,precio) VALUES ('Guiso de Arroz', 8000);
INSERT INTO comidas (nombre,precio) VALUES ('Milanesas',12000);
INSERT INTO comidas (nombre,precio) VALUES ('Pollo Grille',10000);

INSERT INTO postres (nombre,precio) VALUES ('Flan', 6000);
INSERT INTO postres (nombre,precio) VALUES ('Yogur Grande', 8000);
INSERT INTO postres (nombre,precio) VALUES ('Pastafrola', 8500);

--Combinamos los registros de ambas tablas para mostras los menus combinados y su precio
--Con CROSS JOIN
SELECT c.nombre AS "Plato principal",
p.nombre AS "Postre",
c.precio + p.precio AS "Precio total del menú"
FROM comidas AS c
CROSS JOIN postres AS p;