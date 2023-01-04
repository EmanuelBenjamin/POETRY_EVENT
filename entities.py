import datetime

class Contestant():
    def __init__(self, id, card = None, full_name = None, direction = None, gender =None, phone_number = None, date_of_birth = None, student_career =None,   genre_of_poetry = None, registration_date =None, declamation_date = None, age = None):
        self.id= id
        self.card = card
        self.full_name = full_name
        self.direction = direction
        self.gender = gender
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.student_career = student_career
        self.genre_of_poetry  = genre_of_poetry 
        self.registration_date = datetime.date.today()
        self.declamation_date  = declamation_date 
        self.age = age

class List():
    def __init__(self, id,  card = None, full_name = None, direction = None, gender =None, phone_number = None, date_of_birth = None, student_career =None,   genre_of_poetry = None, registration_date =None, declamation_date = None, age = None):
        self.id= id
        self.card = card
        self.full_name = full_name
        self.direction = direction
        self.gender = gender
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.student_career = student_career
        self.genre_of_poetry  =  genre_of_poetry
        self.registration_date = registration_date
        self.declamation_date  = declamation_date
        self.age = age

        
        

    def to_JSON(self):
        return{
            'card': self.card,
            'full_name':self.full_name,
            'direction':self.direction,
            'gender':self.gender,
            'phone_number':self.phone_number,
            'student_career':self.student_career,
            'genre_of_poetry':self.genre_of_poetry,
            }

            