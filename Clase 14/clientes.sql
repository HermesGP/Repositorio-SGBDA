DROP TABLE IF EXISTS clientes CASCADE;
DROP TABLE IF EXISTS grupos_clientes;
CREATE TABLE grupos_clientes (
    id SERIAL PRIMARY KEY,
    nombre_grupo VARCHAR(50) NOT NULL
);
INSERT INTO grupos_clientes (nombre_grupo) VALUES
('Clientes VIP'),
('Clientes Regulares'),
('Clientes Ocasionales'),
('Clientes Inactivos'),
('Clientes Nuevos');
CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nombre_completo VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    direccion VARCHAR(255) NOT NULL,
    localidad_y_codigo_postal VARCHAR(100) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_grupo_cliente INTEGER NOT NULL,
    FOREIGN KEY (id_grupo_cliente) REFERENCES grupos_clientes(id) ON DELETE CASCADE
);