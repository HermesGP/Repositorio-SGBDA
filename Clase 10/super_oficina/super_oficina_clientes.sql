DROP TABLE IF EXISTS pedidos_cabecera;
DROP TABLE IF EXISTS clientes;

CREATE TABLE clientes(
id SERIAL PRIMARY KEY,
nombre_completo VARCHAR(200) NOT NULL,
email VARCHAR(100) UNIQUE,
RUC VARCHAR(15) UNIQUE NOT NULL,
telefono VARCHAR(20) UNIQUE
);

CREATE TABLE pedidos_cabecera(
id SERIAL PRIMARY KEY,
cliente_id INT NOT NULL,
total NUMERIC CHECK (total >= 0),
fecha TIMESTAMP DEFAULT NOW(),
FOREIGN KEY (cliente_id)
	REFERENCES clientes(id)
	ON DELETE CASCADE
);

INSERT INTO clientes (nombre_completo, RUC)
VALUES ('Kily Gonzalez', '3643646-3');

UPDATE clientes 
SET email='erkilly@gmail.com', telefono='+595991457356'
WHERE id=1;

INSERT INTO pedidos_cabecera (cliente_id,total)
VALUES (1,550000);

DELETE FROM clientes;