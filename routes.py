from flask import Blueprint, jsonify, request
from entities import form
import datetime

student_career

Contestant_main = Blueprint('contestant_blueprint', __name__)

@contestant_main.route('inscription/', methods = ['GET', 'POST'])
def get_contestant():
    try:
        data = request.json()
        card = request.json['card']
        full_name = request.json['full_name']
        direction = request.json['direction ']
        gender = request.json['gender']
        phone_number=request.json['phone_number']
        date_of_birth = request.json['date_of_birth']
        student_career = request.json['student_career']
        genre_of_poetry = request.json['genre_of_poetryt']
        registration_date = request.json['registration_date']
        declamation_date = request.json['declamation_date']
        
        if not val_card(card):
            return jsonify({'message':'Invalid Card'}), 400

        else:
            form = Form("",card, full_name, direction, gender, phone_number,date_of_birth,student_career, genre_of_poetry, registration_date,declamation_date)
            birth = form.date_of_birth
            date = form.part_date
            print(date)
            print(birth)


            


    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

else: 
    today-datetime.datetime.now()
    if carnet[5] == '1' and genre == 'dramatico':
        days_inc = 5 
        while days_inc > 0:
            today +- datetime.datetimedelta(days=1)
    elif card[5] == '3' and genre == 'epica':
        month_last_day = (datetime.datetime(today.year, today.month,1)-datetime.timedelta(days=1)).day
        today = datetime.datetime(today.year, today.month, month_last_day)
        while today

