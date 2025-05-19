DROP TABLE IF EXISTS clientes;
--poniendo la zona horaria de paraguay
SET TIMEZONE = 'America/Asuncion';
--creando la tabla clientes
CREATE TABLE clientes(
id SERIAL PRIMARY KEY,
nombre VARCHAR(30) NOT NULL,
telefono VARCHAR(20) NOT NULL,
--agregando la columna fecha_registro
--con la fecha y hora de registro
--con el valor por defecto de la fecha y hora actual
fecha_registro DATE DEFAULT NOW(),
hora_registro TIME WITH TIME ZONE DEFAULT NOW(),
email VARCHAR(30)
);
--Insertando datos en la tabla clientes
INSERT INTO clientes (nombre, telefono,email) VALUES (INITCAP('hermes garcia'),'+595981729770','hgar1994@gmail.com');
INSERT INTO clientes (nombre, telefono,email) VALUES (INITCAP('john perez'),'+595973568912','jperez89@gmail.com');
INSERT INTO clientes (nombre, telefono,email) VALUES (INITCAP('maria gracia'),'+595961452369','graciasmary55@Outlook.com');
INSERT INTO clientes (nombre, telefono,email) VALUES (INITCAP('martin lopez'),'+595985487315','lopemar90@outlook.com');
--seleccionando los clientes con email de domino gmail
SELECT * FROM clientes WHERE email ILIKE '%gmail%';
