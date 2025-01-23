import pymysql
from pymysql import MySQLError
import os
from dotenv import load_dotenv

load_dotenv()

try:
    # Conexión a la base de datos
    conexion = pymysql.connect(
        host= os.getenv('MYSQL_DATABASE'),
        user= os.getenv('MYSQL_USER'),
        password= os.getenv('MYSQL_PASSWORD')
        
    )

    if conexion.open:
        print("Conexión establecida.")
        cursor = conexion.cursor()

        # Leer y ejecutar el archivo SQL
        with open('config_db.sql', 'r') as file:
            sql_script = file.read()
        
        # Ejecutar cada sentencia
        for statement in sql_script.split(';'):
            if statement.strip():
                cursor.execute(statement + ';')
        conexion.commit()
        print("Sentencias ejecutadas.")

except MySQLError as e:
    print(f"Error al conectar a MySQL: {e}")

finally:
    if 'conexion' in locals() and conexion.open:
        cursor.close()
        conexion.close()
    elif 'conexion' in locals():
        conexion.close()
        print("Conexión a MySQL cerrada.")

