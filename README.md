# Sistema de Gestión de Cursos

## Descripción

Sistema de gestión de cursos, implementado en Python. Utiliza una base de datos MySQL para almacenar y gestionar la información de los cursos, como el código, nombre y créditos.

## Estructura

### 1. `conexion.py`

Este archivo contiene la clase **`ConexionBD`**, que se encarga de establecer la conexión con la base de datos MySQL y proporciona métodos para listar cursos, registrar nuevos cursos, actualizar información de cursos existentes y eliminar cursos.

### 2. `main.py`

En este archivo, se encuentra la función **`menuPrincipal`** que presenta un menú interactivo al usuario, permitiendo listar cursos, registrar un nuevo curso, actualizar un curso existente, eliminar un curso y salir del sistema. Se utiliza la clase **`ConexionBD`** para interactuar con la base de datos.

### 3. `functions.py`

Este archivo contiene funciones adicionales utilizadas en el programa principal (**`main.py`**) para agilizar las consultas realizadas a la base de datos. Incluye funciones para mostrar cursos, solicitar datos para registrar un nuevo curso, pedir datos para actualizar un curso y realizar la eliminación de un curso.

### 4. `database.sql`

El archivo **`database.sql`** contiene el script SQL para crear la base de datos `database` y la tabla `cursos`. Además, incluye algunos datos de ejemplo para la tabla. Asegúrate de ejecutar este script en tu servidor de base de datos antes de ejecutar el programa Python para garantizar que la base de datos esté configurada correctamente.

## Requisitos

- Python 3.x
- Biblioteca **`mysql-connector`** para la conexión a la base de datos MySQL.

## Instrucciones de Uso

1. Configure la conexión a la base de datos en el archivo **`conexion.py`**, proporcionando los detalles necesarios como el nombre de usuario, contraseña, host, puerto y nombre de la base de datos.

2. Ejecute el archivo **`main.py`**.

3. Utilice el menú principal para interactuar con el sistema.

4. Siga las indicaciones para listar, registrar, actualizar o eliminar cursos.
