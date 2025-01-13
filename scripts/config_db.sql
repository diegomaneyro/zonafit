-- Eliminar base de datos si existe
DROP DATABASE IF EXISTS zona_fit;

-- Crear base de datos 
CREATE DATABASE zona_fit;

-- Usar base de datos
USE zona_fit;

-- Crear tabla
CREATE TABLE clientes (
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50) NULL,
    apellido VARCHAR(50) NULL,
    membresia INT NULL,
    PRIMARY KEY (id),
    UNIQUE INDEX membresia_UNIQUE(membresia ASC) VISIBLE
);

-- ingresar datos a la tabla
INSERT INTO clientes(nombre, apellido, membresia) VALUES
    ('Daniel', 'Torres',450),
    ('Ivonne', 'Lopez', 500),
    ('Sofia', 'Britez', 300),
    ('Julieta', 'Maneyro', 200),
    ('Diego', 'Maneyro', 600);