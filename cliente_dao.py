'''Clase encargada del CRUD que usa el patrón de diseño DAO'''
from cliente import Cliente
from conexion import Conexion


class ClienteDAO:
    _SELECCIONAR = 'SELECT * FROM clientes ORDER BY id ASC'
    _SELECCIONAR_ID = 'SELECT * FROM clientes WHERE id=%s'
    _ACTUALIZAR = 'UPDATE clientes SET nombre = %s, apellido = %s, membresia = %s WHERE id = %s'
    _INSERTAR = 'INSERT INTO clientes (nombre, apellido, membresia) VALUES (%s, %s, %s)'
    _ELIMINAR = 'DELETE FROM clientes WHERE id = %s'

    @classmethod
    def seleccionar_por_id(cls, id):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = [id,]
            cursor.execute(cls._SELECCIONAR_ID, valores)
            registro = cursor.fetchone()
            # Mapeo de clase-tabla cliente
            cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
            return cliente
        except Exception as e:
            if conexion is not None:
                cursor.close()
                Conexion.devolver_conexion(conexion)

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            clientes = []
            for registro in registros:
                cliente = Cliente(id=registro[0],nombre=registro[1], apellido=registro[2], membresia=registro[3])
                clientes.append(cliente)
            return clientes
        
        except Exception as e:
            print('Ocurrió un error al listar la base de datos:', e)
        
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.devolver_conexion(conexion)

    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls._ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        
        except Exception as e:
            print(f'Ocurrio un error al actualizar el registro: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.devolver_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls._INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
            
        except Exception as e:
            print(f'Ocurrio un error al insertar el registro: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.devolver_conexion(conexion)

    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valor = (cliente.id,)
            cursor.execute(cls._ELIMINAR, valor)
            conexion.commit()
            return cursor.rowcount
            
        except Exception as e:
            print(f'Ocurrio un error al eliminar el registro: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.devolver_conexion(conexion)



    