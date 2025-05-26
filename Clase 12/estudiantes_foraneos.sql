
DROP TABLE IF EXISTS estudiantes CASCADE;
DROP TABLE IF EXISTS cursos CASCADE;
DROP TABLE IF EXISTS inscripciones;
--creando las tablas estudiantes, cursos e inscripciones
-- con las relaciones correspondientes
CREATE TABLE estudiantes(
id SERIAL PRIMARY KEY,
nombre VARCHAR(100),
correo VARCHAR(100) UNIQUE
);

CREATE TABLE cursos(
id SERIAL PRIMARY KEY,
nombre VARCHAR(100)
);

CREATE TABLE inscripciones(
id SERIAL PRIMARY KEY,
--relacionando las tablas estudiantes y cursos
-- con las claves foraneas correspondientes
estudiante_id INT REFERENCES estudiantes(id) ON DELETE CASCADE,
curso_id INT REFERENCES cursos(id) ON DELETE CASCADE,
fecha_inscripcion DATE DEFAULT CURRENT_DATE
);

-- Insertando datos en las tablas estudiantes, cursos e inscripciones
INSERT INTO estudiantes (nombre,correo) VALUES
('Martin Gomez','margo@gmail.com'),
('Felicia Fernandez', 'felfer@gmail.com'),
('Hermes Garcia', 'hgar1994@gmail.com');

INSERT INTO cursos (nombre) VALUES
('Base de Datos'),
('Estadistica');

INSERT INTO inscripciones (estudiante_id,curso_id) VALUES
(1,1), --Martin en Base de Datos
(1,2), --Martin en Estadistica
(2,1), --Felicia en Base de Datos
(3,2); --Hermes en Estadística

-- Consulta para obtener los datos de las inscripciones
-- incluyendo el nombre del estudiante, el curso y la fecha de inscripción
SELECT 
	i.id AS "Id de inscripción",
	e.nombre AS "Estudiante",
	c.nombre AS "Curso",
	i.fecha_inscripcion AS "Fecha de Inscripción"
FROM inscripciones AS i
JOIN estudiantes AS e
ON i.estudiante_id = e.id
JOIN cursos AS c
ON i.curso_id = c.id

