DROP TABLE IF EXISTS productos;
CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    descripcion VARCHAR(255) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
	cantidad DECIMAL(10,2) NOT NULL,
    fecha_fabricacion DATE NOT NULL
);