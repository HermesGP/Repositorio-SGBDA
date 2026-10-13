DROP TABLE IF EXISTS empleados;
CREATE TABLE empleados(
id SERIAL PRIMARY KEY,
nombre_completo VARCHAR(150) NOT NULL,
edad INT CHECK (edad >= 18),
email VARCHAR(100) UNIQUE NOT NULL,
cargo VARCHAR(50) NOT NULL,
salario NUMERIC DEFAULT 2899048
);

INSERT INTO empleados (nombre_completo, edad, email, cargo, salario)
VALUES ('Juan Martinez', 20, 'juanma56@gmail.com', 'conserje', 900000);
INSERT INTO empleados (nombre_completo, edad, email, cargo, salario)
VALUES ('Ana Gomez', 60, 'anago45@hotmail.com', 'secretaria', 3500000);
INSERT INTO empleados (nombre_completo, edad, email, cargo)
VALUES ('Hugo Lopez', 39, 'hugorlon@hotmail.com', 'contratista');