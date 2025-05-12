DROP TABLE empleados;
--Creación de la tabla con sus respectivas restricciones, se puede poner más de una a la vez
--El tipo de dato SERIAL es un entero que se autoincrementa
--El tipo de dato NUMERIC es un número decimal
--El tipo de dato VARCHAR(n) es una cadena de caracteres de longitud variable
CREATE TABLE empleados(
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(50) NOT NULL,
	edad INT CHECK(edad >= 20),
	email VARCHAR(30) UNIQUE NOT NULL,
	cargo VARCHAR(50) NOT NULL,
	salario NUMERIC NOT NULL
);
--Insertar datos en la tabla empleados
--Se puede insertar más de una fila a la vez
INSERT INTO empleados (nombre, edad, email, cargo, salario) VALUES
('Carlos López', 28, 'carlos.lopez@email.com', 'Analista de datos', 4200),
('María Fernández', 35, 'maria.fernandez@email.com', 'Gerente de proyectos', 6500),
('Juan Pérez', 42, 'juan.perez@email.com', 'Desarrollador Senior', 5800),
('Ana Gómez', 30, 'ana.gomez@email.com', 'Diseñadora UX/UI', 4800),
('Luis Ramírez', 25, 'luis.ramirez@email.com', 'Programador Junior', 3500),
('Sofía Herrera', 29, 'sofia.herrera@email.com', 'Ingeniera de software', 5000),
('Miguel Torres', 38, 'miguel.torres@email.com', 'Administrador de bases de datos', 5300),
('Laura Vázquez', 27, 'laura.vazquez@email.com', 'Especialista en seguridad', 4600),
('Roberto Medina', 33, 'roberto.medina@email.com', 'Consultor IT', 6200),
('Patricia Sánchez', 31, 'patricia.sanchez@email.com', 'Arquitecta de software', 7000);
INSERT INTO empleados (nombre, edad, email, cargo, salario) VALUES
('Gabriel Ríos', 26, 'gabriel.rios@email.com', 'Analista de seguridad', 4800),
('Elena Castro', 34, 'elena.castro@email.com', 'Especialista en redes', 5200),
('Daniel Vera', 40, 'daniel.vera@email.com', 'Desarrollador Backend', 5700),
('Lucía Morales', 29, 'lucia.morales@email.com', 'Ingeniera en datos', 6000),
('Fernando Guzmán', 31, 'fernando.guzman@email.com', 'Scrum Master', 6500);

--Selecciona la id, nombre y salario de los 8 empleados más jovenes que ganen 5000 o más
SELECT id,nombre,salario FROM empleados WHERE salario>=5000
ORDER BY edad ASC
LIMIT 8;
--Selecciona la id, nombre y salario de los 5 empleados más viejos que ganen 5000 o más
SELECT id,nombre,salario FROM empleados WHERE salario>=5000
ORDER BY edad DESC
LIMIT 5;
--Seleccionar el nombre, edad y cargo de los empleados ordenados por nombre
SELECT nombre,edad,cargo FROM empleados
ORDER BY nombre;
