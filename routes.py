from flask import Blueprint, jsonify, request
from entities import Form
import datetime
from models import formModel, ListModel
from dateutil.relativedelta import relativedelta
from age import obAge



Contestant_main = Blueprint('contestant_main_blueprint', __name__)
ContestantList_main = Blueprint('contestantList_main_blueprint', __name__)

@contestantList_main.route('/', methods = ['GET'])
def List_contestants():
    try:

        contestants = Listcontestants.get_Contestant()
        return jsonify(contestants)
    except Exception as ex:
        return jsonify({'Message':str(ex)}),500

@studentForm_main.route('/', methods = ['POST'])
def form():
    try:
        #lo datos que pediremos desde postman
        carnet = request.json['carnet']
        fullname = request.json['fullname']
        address = request.json['address']
        gender = request.json['gender']
        phone_number = request.json['phone_number']
        birth_date = request.json['birth_date']
        career = request.json['career']
        genre = request.json['genre']
        if not val_carnet(carnet):
            return jsonify({'message': 'Carnet no valido'}), 400
        else:
            if not val_birth_date(birth_date):
                return jsonify({'message': 'Eres menor de edad'}), 400
            else:
                #codigo para subir datos a db
                today = datetime.datetime.now()
                if carnet[5] == '1' and genre == 'dramatico':
                    days_inc = 5
                    while days_inc > 0:
                        today += datetime.timedelta(days=1)
                        if today.weekday() not in (5, 6):
                            days_inc -= 1
                elif carnet[5] == '3' and genre == 'epica':
                    month_last_day = (datetime.datetime(today.year, today.month, 1) - datetime.timedelta(days=1)).day
                    today = datetime.datetime(today.year, today.month, month_last_day)
                    while today.weekday() in (5, 6):
                        today -= datetime.timedelta(days=1)
                else: 
                    while today.weekday() != 4:
                        today += datetime.timedelta(days=1)      
                part_date = today.strftime('%Y-%m-%d')
                edad = obEdad(birth_date)
                age = edad.years
                form = Form("", carnet, fullname, address, gender, phone_number, birth_date, career, genre, "", part_date, age )
                affected_row = formModel.form(form)
                if affected_row == 1:
                    return jsonify('Agregado')
                else: 
                        return None
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
def val_carnet(carnet):
            if len(carnet) != 6:
                return False
            if carnet[0].upper() != 'A':
                return False
            if carnet[2] != '5':
                return False
            if carnet[-1] not in ('1','3','9'):
                return False
            return True
def val_birth_date(birth_date):
    try:
        birth_date = datetime.datetime.strptime(birth_date, '%Y-%m-%d')
    except ValueError:
        return False
    today = datetime.datetime.now()

    return (today - birth_date).days // 365 >= 17

