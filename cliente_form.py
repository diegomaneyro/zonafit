from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, HiddenField
from wtforms.validators import DataRequired

class ClienteForm(FlaskForm):
    id = HiddenField("Id")
    nombre = StringField("Nombre", validators=[DataRequired()])
    apellido = StringField("Apellido", validators=[DataRequired()])
    membresia = IntegerField("Membresia", validators=[DataRequired()])
    guardar = SubmitField("Guardar")