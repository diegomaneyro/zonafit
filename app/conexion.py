from mysql.connector import pooling, Error
from dotenv import load_dotenv
import os
import logging

# Configuración del logger
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# carga las variables de entorno desde el archivo .env
load_dotenv()


class Conexion:
    DATABASE = os.getenv('MYSQL_DATABASE')
    USERNAME = os.getenv('MYSQL_USER')
    PASSWORD = os.getenv('MYSQL_PASSWORD')
    DB_PORT = os.getenv('MYSQL_PORT')
    HOST = os.getenv('MYSQL_HOST')
    POOL_SIZE = 5
    POOL_NAME = 'zona_fit_pool'
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None: # Se crea el objeto pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name = cls.POOL_NAME,
                    pool_size = cls.POOL_SIZE,
                    host = cls.HOST,
                    port = int(cls.DB_PORT),
                    database = cls.DATABASE,
                    user = cls.USERNAME,
                    password = cls.PASSWORD
                )
                return cls.pool
            except Error as e:
                logging.error(f'Ocurrió un error al obtener el pool de conexiones: {e}')
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def devolver_conexion(cls, conexion):
        conexion.close()


if __name__ == '__main__':
    # Creamos un objeto pool
    pool = Conexion.obtener_pool()
    print(pool)
    conexion1 = pool.get_connection()
    print(conexion1)
    Conexion.devolver_conexion(conexion1)
    print(f'Se ha liberado el objeto conexion1')
