# Zona Fit (GYM)

Zona Fit es una aplicación web desarrollada con Flask y MySQL para la gestión integral de clientes de un gimnasio.

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

## Instalación

1. Clona el repositorio:
    ```sh
    git clone <URL_DEL_REPOSITORIO>
    ```
2. Navega al directorio del proyecto:
    ```sh
    cd zona_fit
    ```
3. Crea y activa un entorno virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```
4. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

## Configuración de la Base de Datos

1. Asegúrate de tener MySQL instalado y en funcionamiento.
2. Ejecuta el script SQL para configurar la base de datos:
    ```sh
    python scripts/config.py
    ```

## Ejecución de la Aplicación

1. Inicia la aplicación Flask:
    ```sh
    flask