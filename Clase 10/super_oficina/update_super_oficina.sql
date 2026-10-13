--Comprando 20 botellas de coca
UPDATE producto 
SET stock = stock + 20 
WHERE id_producto = 4;
--Comprando 100 botellas de cerveza y asignando un nuevo precio
UPDATE producto 
SET stock = stock + 100 ,
precio = 10000
WHERE id_producto = 5;