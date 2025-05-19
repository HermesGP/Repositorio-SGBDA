DROP TABLE IF EXISTS productos;
--creando la tabla productos
CREATE TABLE productos(
codigo SERIAL PRIMARY KEY,
nombre VARCHAR(30),
precio NUMERIC,
cantidad INTEGER,
categoria VARCHAR(20) DEFAULT 'Electronicos'
);
--Insertando datos en la tabla productos
INSERT INTO productos (nombre,precio,cantidad) VALUES ('notebook ASUS',2500000,10);
INSERT INTO productos (nombre,precio,cantidad) VALUES ('notebook ACER',1800000,20);
INSERT INTO productos (nombre,precio,cantidad) VALUES ('parlante JBL',250000,50);
INSERT INTO productos (nombre,precio,cantidad) VALUES ('playtation 5',3500000,8);
--cambiando los precios con un 10% de descuento
--actualizando los precios de los productos
UPDATE productos SET precio = precio - (precio * 0.1);
--reporte de productos con columna de encabezado "Descripción"
--concatenando nombre y categoria
--y columna calculada "Valor del Stock"
--que es el resultado de multiplicar precio por cantidad
SELECT codigo,nombre||', '||categoria AS "Descripción",precio,cantidad,
precio*cantidad AS "Valor del Stock"
FROM productos;