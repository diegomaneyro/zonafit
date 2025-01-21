# archivo encargado de gestionar las operaciones de la app

from app.cliente import Cliente
from app.cliente_dao import ClienteDAO

print('*** Clientes de Zona Fit (GYM) ***')
opcion = None
while opcion != 5:
    print('''Menu:
    1. Listar clientes
    2. Agregar clientes
    3. Modificar clientes
    4. Eliminar clientes
    5. Salir''')
    opcion = int(input('Escribir tu opcion (1-5): '))
    if opcion == 1: # Listar clientes
        clientes = ClienteDAO.seleccionar()
        print('\n*** Listado de Clientes ***')
        for cliente in clientes:
            print(cliente)
        print()

    elif opcion == 2: # Agregar cliente
        nombre_var = input('Escribe el nombre: ')
        apellido_var = input('Escribe el apellido: ')
        membresia_var = int(input('Escribe la membresia: '))
        cliente = Cliente(nombre=nombre_var, apellido=apellido_var, membresia=membresia_var)
        clientes_insertados = ClienteDAO.insertar(cliente)
        print(f'Clientes insertados: {clientes_insertados}')
        print()

    elif opcion == 3: # Actualizar cliente
        id_cliente_var = int(input('Escribe id del cliente a actualizar: '))
        nombre_var = input('Escribe el nombre: ')
        apellido_var = input('Escribe el apellido: ')
        membresia_var = input('Escribe la mambresia: ')
        cliente = Cliente(id_cliente_var, nombre_var, apellido_var, membresia_var)
        clientes_modificados = ClienteDAO.actualizar(cliente)
        print(f'Clienes modificados: {clientes_modificados}')
        print()

    elif opcion == 4: # Eliminar cliente
        id_cliente_var = int(input('Escribe el id del cliente a eliminar: '))
        cliente = Cliente(id=id_cliente_var)
        clientes_eliminados = ClienteDAO.eliminar(cliente)
        print(f'Clientes modificados: {clientes_modificados}')
        print()
    
    else:
        print('Salimos de la aplicacion...')