--Eliminando a la cliente Florencia
DELETE FROM cliente 
WHERE nombre = 'Florencia';
--Eliminando los productos que valen menos de 10000
DELETE FROM producto 
WHERE precio < 10000;
--Eliminando TODOS los datos de detalle_pedido
DELETE FROM detalle_pedido;