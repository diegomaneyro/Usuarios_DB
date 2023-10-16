-- Elimina la base de datos si ya existe
DROP DATABASE IF EXISTS usuario_db;

-- Crea la base de datos
CREATE DATABASE usuario_db
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = 5;

-- Conéctate a la nueva base de datos
\c usuario_db

-- Crea una tabla en la nueva base de datos
CREATE TABLE usuario (
    id_usuario serial PRIMARY KEY,
    username varchar(50),
    password varchar(50)
);
