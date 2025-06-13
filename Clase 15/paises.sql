CREATE TABLE paises(
    id SERIAL PRIMARY KEY, 
    nombre VARCHAR(255), 
    capital VARCHAR(255), 
    region VARCHAR(255), 
    subregion VARCHAR(255), 
    poblacion INT, 
    area FLOAT, 
    bandera VARCHAR(255))