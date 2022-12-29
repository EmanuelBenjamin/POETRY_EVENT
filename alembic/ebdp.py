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

# Crea la ruta "/inscripcion" para recibir los datos de los concursantes
@app.route('/inscripcion', methods=['POST'])
def inscripcion():
    # Recibe los datos del concursante en el cuerpo de la solicitud
    data = request.get_json()
    carnet = data['carnet']
    nombre = data['nombre']
    direccion = data['direccion']
    genero = data['genero']
    telefono = data['telefono']
    fecha_nacimiento = data['fecha_nacimiento']
    carrera = data['carrera']
    genero_poesia = data['genero_poesia']
    
    # Valida los datos del concursante
    if not validar_carnet(carnet):
        return jsonify({'error': 'El carnet es inválido'}), 400
    if not validar_fecha_nacimiento(fecha_nacimiento):
        return jsonify({'error': 'La fecha de nacimiento es inválida'}), 400
    
    # Calcula la fecha de declamación del concursante
Ahora que hemos validado los datos del concursante, podemos proceder a calcular
 la fecha de declamación del mismo. Para ello, podemos utilizar la siguiente función:

#FORMA UNO 
def calcular_fecha_declamacion(carnet, genero_poesia):
    hoy = datetime.datetime.now().date()
    if carnet[5] == '1' and genero_poesia == 'dramático':
        # Si el carnet termina en 1 y el género de poesía es dramático, concursará 5 días después de la inscripción
        fecha_declamacion = hoy + datetime.timedelta(days=5)
        while fecha_declamacion.weekday() in (5, 6):
            # Si la fecha es sábado o domingo, se salta ese día
            fecha_declamacion += datetime.timedelta(days=1)
    elif carnet[5] == '3' and genero_poesia == 'épico':
        # Si el carnet termina en 3 y el género de poesía es épico, concursará el último día del mes
        ultimo_dia_mes = calendar.monthrange(hoy.year, hoy.month)[1]
        fecha_declamacion = datetime.date(hoy.year, hoy.month, ultimo_dia_mes)
        while fecha_declamacion.weekday() in (5, 6):
            # Si la fecha es sábado o domingo, se salta ese día
            fecha_declamacion -= datetime.timedelta(days=1)
    else:
        # Si el carnet termina en otro dígito y/o el género de poesía es distinto de dramático o épico, concursará el viernes de la semana que se inscribió
        diferencia_dias = 4 - hoy.weekday()
        fecha_declamacion = hoy + datetime.timedelta(days=diferencia_dias)
    return fecha_declamacion

Esta función recibe como parámetros el carnet del concursante y su género de poesía, y devuelve un objeto
datetime.date con la fecha de declamación del concursante. En el primer caso, si el carnet termina en "1" y 
el género de poesía es dramático, se calcula la fecha de declamación sumando 5 días a la fecha actual. 
Si la fecha resultante es sábado o domingo, se salta ese día y se vuelve a calcular la fecha de declamación
sumando otro día. En el segundo caso, si el carnet termina en "3" y el género de poesía es épico, se calcula
la fecha de declamación como el último día del mes actual. Si la fecha resultante es sábado o domingo,
se salta ese día y se vuelve a calcular la fecha de declamación restando otro día. En el tercer caso,
para todos los demás carnets y géneros de poesía, se calcula la fecha de declamación como el viernes 
de la semana actual.

#FORMA DOS

# Calcula la fecha de declamación
hoy = datetime.datetime.now()
if carnet[5] == '1' and genero_poesia == 'dramático':
    # Si el carnet termina en 1 y el género de poesía es dramático, la fecha de declamación es 5 días después de la inscripción
    dias_a_sumar = 5
    while dias_a_sumar > 0:
        hoy += datetime.timedelta(days=1)
        if hoy.weekday() not in (5, 6): # Si no es sábado ni domingo
            dias_a_sumar -= 1
elif carnet[5] == '3' and genero_poesia == 'épica':
    # Si el carnet termina en 3 y el género de poesía es épica, la fecha de declamación es el último día del mes que se inscribió
    ultimo_dia_del_mes = (datetime.datetime(hoy.year, hoy.month+1, 1) - datetime.timedelta(days=1)).day
    hoy = datetime.datetime(hoy.year, hoy.month, ultimo_dia_del_mes)
    while hoy.weekday() in (5, 6): # Si es sábado o domingo
        hoy -= datetime.timedelta(days=1)
else:
    # Para todas las demás terminaciones de carnets válidos y géneros de poesía, la fecha es el viernes de la semana que se inscribió
    while hoy.weekday() != 4: # Mientras no sea viernes
        hoy += datetime.timedelta(days=1)
fecha_declamacion = hoy.strftime('%Y-%m-%d')

# Guarda los datos en la base de datos
cursor = cnx.cursor()
query = 'INSERT INTO concursantes (carnet, nombre, direccion, genero, telefono, fecha_nacimiento, carrera, genero_poesia, fecha_inscripcion, fecha_declamacion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, CURDATE(), %s)'
values = (carnet, nombre, direccion, genero, telefono, fecha_nacimiento, carrera, genero_poesia, fecha_declamacion)
cursor.execute(query, values)
cnx.commit()




#FORMA 3


import calendar


Con esto podemos continuar con el código que guarda los datos del concursante y su fecha de declamación 
en la base de datos.Aquí tienes cómo podría quedar el código completo de la función inscripcion():


Para poder utilizar la función calcular_fecha_declamacion() en nuestro código, es necesario importar 
el módulo calendar de la biblioteca estándar de Python. Así que debes agregar la siguiente línea al 
principio del archivo:

@app.route('/inscripcion', methods=['POST'])
def inscripcion():
    # Recibe los datos del concursante en el cuerpo de la solicitud
    data = request.get_json()
    carnet = data['carnet']
    nombre = data['nombre']
    direccion = data['direccion']
    telefono = data['telefono']
    fecha_nacimiento = data['fecha_nacimiento']
    carrera = data['carrera']
    genero_poesia = data['genero_poesia']
    
    # Valida los datos del concursante
    if not validar_carnet(carnet):
        return jsonify({'error': 'El carnet es inválido'}), 400
    if not validar_fecha_nacimiento(fecha_nacimiento):
        return jsonify({'error': 'La fecha de nacimiento es inválida'}), 400
    
    # Calcula la fecha de declamación del concursante
    fecha_declamacion = calcular_fecha_declamacion(carnet, genero_poesia)
    
    # Crea un nuevo registro en la tabla "concursantes"
    nuevo_concursante = Concursante(carnet=carnet, nombre=nombre, direccion=direccion, genero=genero,
                                    telefono=telefono, fecha_nacimiento=fecha_nacimiento, carrera=carrera,
                                    genero_poesia=genero_poesia, fecha_inscripcion=datetime.datetime.now().date(),
                                    fecha_declamacion=fecha_declamacion)
    db.session.add(nuevo_concursante)
    db.session.commit()
    
    return jsonify({'mensaje': 'El concursante ha sido inscrito exitosamente'}), 201


# ##########################################################Función para validar el carnet del concursante#######################################

La función validar_carnet(carnet) se encarga de verificar que el
carnet cumpla con las condiciones que se han especificado en el
 enunciado del problema. Por ejemplo, que tenga 6 caracteres, 
que el primer carácter sea "A" (indiferentemente si es mayúscula o minúscula),
que el tercer carácter sea "5" y que el último carácter termine en "1", "3" o "9".
Aquí tienes un ejemplo de cómo podría implementarse esta función:



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




De forma similar, la función validar_fecha_nacimiento(fecha_nacimiento)
 se encarga de verificar que la fecha de nacimiento sea válida y que el 
 oncursante tenga al menos 17 años. 

# ##########################################   forma 1:Función para validar la fecha de nacimiento del concursante  ########################################

 def validar_fecha_nacimiento(fecha_nacimiento):
    try:
        fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
    except ValueError:
        return False
    hoy = datetime.datetime.now()
    return (hoy - fecha_nacimiento).days // 365 >= 17


##############################   # forma 2: Función para validar la fecha de nacimiento del concursante  ##################################

def validar_fecha_nacimiento(fecha_nacimiento):
    hoy = datetime.datetime.today()
    edad_minima = datetime.timedelta(days=365.25*17)
    if hoy - edad_minima > fecha_nacimiento:
        return True
    return False





############################       EXTRA  ###############################################3

Para completar el ejemplo de código que te he proporcionado, también podemos añadir 
una ruta en la aplicación Flask que permita consultar los datos de los concursantes 
inscritos por carrera, edad, género de poesía y fecha de declamación. Para ello, podemos utilizar la siguiente función:
@app.route('/concursantes', methods=['GET'])
def concursantes():
    # Recibe los parámetros de filtrado (opcionales)
    carrera = request.args.get('carrera')
    genero_poesia = request.args.get('genero_poesia')

    # Crea la consulta a la base de datos
    cursor = cnx.cursor()
    query = 'SELECT carnet, nombre, direccion, genero, telefono, DATE_FORMAT(fecha_nacimiento, "%Y-%m-%d") as fecha_nacimiento, carrera, genero_poesia, DATE_FORMAT(fecha_inscripcion,
     "%Y-%m-%d") as fecha_inscripcion, DATE_FORMAT(fecha_declamacion, "%Y-%m-%d") as fecha_declamacion FROM concursantes'
    values = []
    if carrera:
        query += ' WHERE carrera = %s'
        values.append(carrera)
        if genero_poesia:
            query += ' AND genero_poesia = %s'
            values.append(genero_poesia)
    elif genero_poesia:
        query += ' WHERE genero_poesia = %s'
        values.append(genero_poesia)
    cursor.execute(query, values)

    # Devuelve los resultados de la consulta
    rows = cursor.fetchall()
    result = []
    for row in rows:
        result.append({
            'carnet': row[0],
            'nombre': row[1],
            'direccion': row[2],
            'genero': row[3],
            'telefono': row[4],
            'fecha_nacimiento': row[5],
            'carrera': row[6],
            'genero_poesia': row[7],
            'fecha_inscripcion': row[8],
            'fecha_declamacion': row[9]
        })
    return jsonify(result)
