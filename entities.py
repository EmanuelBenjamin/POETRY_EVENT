class Students():
    def __init__(self, id, card = None, full_name = None, direction = None, gender =None, phone_number = None, date_of_birth = None, student_career =None,   genre_of_poetry = None, Registration_date =None):
        self.id= id
        self.card = card
        self.full_name = full_name
        self.direction = direction
        self.gender = gender
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.student_career = student_career
        self. genre_of_poetry  =  genre_of_poetry 
        self.Registration_date = Registration_date
        self.student_career = student_career
        
        

    def to_JSON(self):
        return{
            'id':self.id,
            'title':self.title,
            'ulr':self.url,
            'classification':self.classification
        }
