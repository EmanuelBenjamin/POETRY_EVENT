Para desarrollar el API REST que permite a los concursantes inscribirse y visualizar el listado de estudiantes inscritos, podemos seguir los siguientes pasos:

Crear un proyecto de Flask y configurar la conexión a la base de datos.
Definir la estructura de la tabla "concursantes" en la base de datos, utilizando SQLAlchemy.

Crear una ruta "/inscripcion" para recibir los datos de los concursantes y validar que los datos del carnet y la fecha de nacimiento sean válidos.

Calcular la fecha de declamación del concursante, siguiendo las reglas especificadas en el enunciado.

Guardar los datos del concursante en la base de datos y devolver la fecha de declamación al cliente.

Crear una ruta "/listado" para visualizar el listado de estudiantes inscritos, filtrando por carrera, edad, género de poesía y fecha de declamación.

import datetime
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'tu_uri_de_conexión_a_la_bd'
db = SQLAlchemy(app)

# Define la estructura de la tabla "concursantes" en la base de datos
class Concursante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    carnet = db.Column(db.String(6), unique=True)
    nombre = db.Column(db.String(50))
    direccion = db.Column(db.String(100))
    genero = db.Column(db.String(10))
    telefono = db.Column(db.String(10))
    fecha_nacimiento = db.Column(db.Date)
    carrera = db.Column(db.String(50))
    genero_poesia = db.Column(db.String(10))
    fecha_inscripcion = db.Column(db.Date)
    fecha_declamacion = db.Column(db.Date)

# Función para validar el carnet del concursante
def validar_carnet(carnet):
    if len(carnet) != 6:
        return False
    if carnet[0].upper() != 'A':
        return False
    if carnet[2] != '5':
        return False
    if carnet[-1] not in ('1', '3', '9'):
        return False
    return True

# Función para validar la fecha de nacimiento del concursante

def validar_fecha_nacimiento(fecha_nacimiento):
    hoy = datetime.datetime.today()
    edad_minima = datetime.timedelta(days=365.25*17)
    if hoy - edad_minima > fecha_nacimiento:
        return True
    return False

# Valida los datos del concursante
if not validar_carnet(carnet):
    return jsonify({'error': 'El carnet es inválido'}), 400
if not validar_fecha_nacimiento(fecha_nacimiento):
    return jsonify({'error': 'La fecha de nacimiento es inválida'}), 400

# Calcula la fecha de declamación del concursante
fecha_inscripcion = datetime.datetime.now().date()
ultimo_dia_mes = calendar.monthrange(fecha_inscripcion.year, fecha_inscripcion.month)[1]
if carnet[-1] == '1' and genero_poesia == 'dramático':
    dias_a_agregar = 5
    while dias_a_agregar > 0:
        fecha_inscripcion += datetime.timedelta(days=1)
        if fecha_insc

