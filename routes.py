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

@contestant_main.route('/', methods = ['POST'])
def form():
    try:
        #lo datos que pediremos desde postman
        card = request.json['card']
        full_name = request.json['full_name']
        direction = request.json['direction']
        gender = request.json['gender']
        phone_number = request.json['phone_number']
        date_of_birth = request.json['date_of_birth']
        student_career = request.json['student_career']
        genre_of_poetry  = request.json['genre_of_poetry ']
        if not val_card(card):
            return jsonify({'message': 'Invalid card'}), 400
        else:
            if not val_date_of_birth (date_of_birth):
                return jsonify({'message': 'You are underage'}), 400
            else:
                #codigo para subir datos a db
                today = datetime.datetime.now()
                if card[5] == '1' and genre == 'dramatic':
                    days_inc = 5
                    while days_inc > 0:
                        today += datetime.timedelta(days=1)
                        if today.weekday() not in (5, 6):
                            days_inc -= 1
                elif card[5] == '3' and genre == 'epic':
                    month_last_day = (datetime.datetime(today.year, today.month, 1) - datetime.timedelta(days=1)).day
                    today = datetime.datetime(today.year, today.month, month_last_day)
                    while today.weekday() in (5, 6):
                        today -= datetime.timedelta(days=1)
                else: 
                    while today.weekday() != 4:
                        today += datetime.timedelta(days=1)      
                part_date = today.strftime('%Y-%m-%d')
                age = obAge(date_of_birth)
                age = age.years
                form = Form("", card, full_name, direction, gender, phone_number, date_of_birth, student_career, genre_of_poetry, "", genre_of_poetry, age )
                affected_row = formModel.form(form)
                if affected_row == 1:
                    return jsonify('Agregado')
                else: 
                        return None
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
def val_card(card):
            if len(card) != 6:
                return False
            if card[0].upper() != 'A':
                return False
            if card[2] != '5':
                return False
            if card[-1] not in ('1','3','9'):
                return False
            return True
def val_date_of_birth(date_of_birth):
    try:
        date_of_birth = datetime.datetime.strptime(date_of_birth, '%Y-%m-%d')
    except ValueError:
        return False
    today = datetime.datetime.now()

    return (today - date_of_birth).days // 365 >= 17

