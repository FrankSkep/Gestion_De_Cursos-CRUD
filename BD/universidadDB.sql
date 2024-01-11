	/* Crear base de datos */
CREATE DATABASE universidad;

	/* Mostrar bases de datos */
SHOW DATABASES;

	/* Usar base de datos */
USE universidad;

	/* Crear tabla */
CREATE TABLE cursos (
 codigo varchar (6) primary key,
 nombre varchar(50),
 creditos int not null);

	/* Mostrar la tabla */
SELECT * FROM cursos;

	/* Insertar datos en la tabla */
INSERT INTO cursos VALUES(342876, "Calculo Integral", 8);

	/* Eliminar datos de la tabla */
DELETE FROM cursos WHERE codigo = 234432 AND nombre = "sadadsa" AND creditos = 32; /* Eliminar un elemento */

	/* Cambiar longitud del nombre */
ALTER TABLE `cursos` CHANGE `nombre` `nombre` VARCHAR(40);