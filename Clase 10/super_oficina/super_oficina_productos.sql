-- Eliminar las tablas si ya existen
DROP TABLE IF EXISTS detalle_pedido;
DROP TABLE IF EXISTS producto;

-- Creación de la tabla producto 
CREATE TABLE producto (
    id_producto SERIAL PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    precio NUMERIC CHECK (precio >= 0) NOT NULL,
    stock INT CHECK (stock >= 0) DEFAULT 0
);

-- Creación de detalle_pedido 
CREATE TABLE detalle_pedido (
    id SERIAL PRIMARY KEY,
    pedido_id INT NOT NULL,
    producto_id INT NOT NULL,
    cantidad INT CHECK (cantidad > 0) NOT NULL,
    subtotal NUMERIC CHECK (subtotal >= 0) NOT NULL,
    FOREIGN KEY (pedido_id) 
        REFERENCES pedidos_cabecera(id) 
        ON DELETE CASCADE,
    FOREIGN KEY (producto_id) 
        REFERENCES producto(id_producto) 
        ON DELETE CASCADE
);

-- 1. Insertar productos de ejemplo (asegurando IDs 4 y 5 para que coincidan con tus UPDATE de ejemplo)
INSERT INTO producto (id_producto, nombre, precio, stock) VALUES
(1, 'Agua Mineral 500ml', 5000, 50),
(2, 'Empanada de Carne', 6000, 30),
(3, 'Jugo en Botella', 8000, 20),
(4, 'Coca Cola 2L', 12000, 15),     -- Este coincide con el UPDATE de id_producto = 4
(5, 'Cerveza Pilsen 600ml', 9000, 40); -- Este coincide con el UPDATE de id_producto = 5

-- Nota: Para insertar un detalle de pedido, primero necesitamos asegurarnos de que 
-- exista un cliente y un pedido en la cabecera (como se vio en 'super_oficina_clientes.sql').
-- Si ya ejecutaste aquel script, el cliente con id=1 y el pedido con id=1 ya existen.

-- 2. Insertar detalles de pedido de ejemplo
INSERT INTO detalle_pedido (pedido_id, producto_id, cantidad, subtotal) VALUES
(1, 1, 2, 10000),  -- 2 unidades de Agua Mineral
(1, 4, 3, 36000);  -- 3 unidades de Coca Cola