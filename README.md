# Zona Fit (GYM)

Zona Fit es una aplicación web desarrollada con Flask y MySQL para la gestión integral de clientes de un gimnasio.

## Deploy
[Demo](https://zonafit.onrender.com/)

## Descripción

Esta aplicación permite realizar diversas operaciones sobre los clientes del gimnasio, tales como la creación, edición, eliminación y visualización de registros. La interfaz es intuitiva y fácil de usar, facilitando la administración de los datos de los clientes.

## Estructura del Proyecto

- **Backend:** Flask
- **Base de Datos:** MySQL
- **Frontend:** HTML, CSS, Bootstrap

## Características

- **Añadir nuevos clientes:** Permite registrar nuevos clientes en la base de datos.
- **Editar información de clientes existentes:** Facilita la actualización de los datos de los clientes.
- **Eliminar clientes:** Permite eliminar registros de clientes de la base de datos.
- **Visualizar la lista de clientes:** Muestra un listado completo de todos los clientes registrados.

## Capturas de Pantalla

Aquí encntrara screenshot de la app

### Página de Inicio

![home](https://github.com/user-attachments/assets/812c4b39-517c-47db-b32c-2654339bdcb3)

## Seguridad

Para mejorar la seguridad de la aplicación, se han implementado las siguientes medidas:

- **Uso de variables de entorno:** Las credenciales de la base de datos y otra información sensible no se incluyen en código duro, sino que se almacenan en variables de entorno. Esto evita la exposición de credenciales en el código fuente.

- **Consultas Parametrizadas:** Todas las consultas a la base de datos utilizan sentencias preparadas y consultas parametrizadas para prevenir la inyección SQL. 
