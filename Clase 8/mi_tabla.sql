-- esta sentencia borra una tabla
DROP TABLE IF EXISTS datos_personales;
-- esto crea el enum estado_civil
CREATE TYPE ESTADO_CIVIL AS
ENUM('Casado','Soltero','Viudo','Divorciado');
-- esta sentencia crea una tabla
CREATE TABLE datos_personales(
numero_id SERIAL,
nombre VARCHAR(30),
cedula VARCHAR(7),
email VARCHAR(20),
edad INT,
estatura FLOAT,
dolares_que_tiene NUMERIC(10,2),
sobre_mi TEXT,
le_gusta_viajar BOOLEAN,
comidas_que_le_gustan VARCHAR(15) [],
estado_civil ESTADO_CIVIL
);
-- esta sentencia inserta datos en la tabla
INSERT INTO mis_clientes(nombre,cedula,email,edad,estatura,dolares_que_tiene,sobre_mi,le_gusta_viajar,comidas_que_le_gustan,estado_civil)
VALUES ('Hermes','3642494','hgar1994@gmail.com',31, 1.81,67894.87,'soy un profesor de bases de datos en la universidad autonoma','yes',ARRAY['milanesa','morcilla','costilla'],'Soltero');
INSERT INTO mis_clientes(nombre,cedula,email,edad,estatura,dolares_que_tiene,sobre_mi,le_gusta_viajar,comidas_que_le_gustan,estado_civil)
VALUES ('Dario','4859631','dariobros@gmail.com',38, 1.71,2564.77,'soy un restaurador de armas','no','{ensalada,tofu,empanada}','Divorciado');

