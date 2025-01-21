from flask import Flask, redirect, render_template, url_for
from dotenv import load_dotenv
import os
from cliente import Cliente
from cliente_dao import ClienteDAO
from cliente_form import ClienteForm

app = Flask(__name__)

# Cargar variables de entorno
load_dotenv()

# Configuración de la base de datos usando variables de entorno
app.config['MYSQL_DATABASE'] = os.getenv('MYSQL_DATABASE')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_PORT'] = os.getenv('MYSQL_PORT')
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')


app.config['SECRET_KEY'] = 'lkñlsdksdsldñsld'
titulo_app = "Zona Fit (GYM)"

@app.route("/")
def index():
    app.logger.debug("a call was made to the home page")
    # Recuperar clientes de la bsae de datos
    clientes_db = ClienteDAO.seleccionar()
    # Crear un objeto de cliente vacio
    cliente = Cliente()
    cliente_form = ClienteForm(obj=cliente)

    return render_template("index.html", titulo=titulo_app, clientes_db=clientes_db, forma=cliente_form)

@app.route("/guardar", methods=['POST'])
def guardar():
    # Crear los objetos de cliente vacio
    cliente = Cliente()
    cliente_forma = ClienteForm(obj=cliente)
    if cliente_forma.validate_on_submit():
        # LLenar el objeto cliente con los valores del formulario
        cliente_forma.populate_obj(cliente)
        if not cliente.id:            
            # Guardar el nuevo cliente en la base de datos
            ClienteDAO.insertar(cliente)
        else:
            ClienteDAO.actualizar(cliente)
    # Redireccionar  la pagina de inicio
    return redirect(url_for('index'))

@app.route("/limpiar")
def limpiar():
    return redirect(url_for('index'))

@app.route("/editar/<int:id>")
def editar(id):
    cliente = ClienteDAO.seleccionar_por_id(id)
    cliente_forma = ClienteForm(obj=cliente)
    clientes_db = ClienteDAO.seleccionar()
    return render_template('index.html', 
                    titulo=titulo_app,
                    forma=cliente_forma,
                    clientes_db=clientes_db)

@app.route("/eliminar/<int:id>")
def eliminar(id):
    cliente = Cliente(id=id)
    ClienteDAO.eliminar(cliente)
    return redirect(url_for("index"))
        
