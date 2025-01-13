import pymysql
from pymysql import MySQLError

try:
    # Conexión a la base de datos
    conexion = pymysql.connect(
        host='localhost',
        user='root',
        password='admin'
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
    if 'connection' in locals() and conexion.open:
        cursor.close()
        conexion.close()
        print("Conexión a MySQL cerrada.")

