DROP TABLE IF EXISTS titanic;
DROP TABLE IF EXISTS clases_titanic;
--Creando tablas para cargar datos del dataset Titanic
CREATE TABLE clases_titanic(
    clase_id INTEGER UNIQUE,
    clase_nombre VARCHAR(25) NOT NULL
);
INSERT INTO clases_titanic (clase_id, clase_nombre)
VALUES
(1, 'Primera Clase'),
(2, 'Segunda Clase'),
(3, 'Tercera Clase');
CREATE TABLE titanic (
    numero_pasajero INTEGER PRIMARY KEY,
    supervivencia BOOLEAN,
    clase_id INTEGER,
    nombre VARCHAR(100) NOT NULL,
    sexo VARCHAR(10) NOT NULL,
    edad NUMERIC(3, 1),
	FOREIGN KEY (clase_id) REFERENCES clases_titanic(clase_id) ON DELETE CASCADE
);
