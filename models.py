from flask import jsonify
from db import get_conection
from entities import List

class ListModel():
    @classmethod
    def get_Contestant(self):
        try:
            connection = get_conection()
            contestants = []
            with connection.cursor() as cursor:
                cursor.execute("""SELECT card, full_name, direction, gender, phone_number, date_of_birth, student_career,  genre_of_poetry, registration_date, declamation_date, age FROM contestant ORDER BY full_name ASC""")
                resulset = cursor.fetchall()

                for row in resulset:
                    contestant =List(row[0], row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])
                    contestants.append(contestant.to_JSON())
            connection.close()
            return contestants
        except Exception as ex:
            raise Exception(ex)  

class contestantsModel():
    @classmethod
    def contestants(self,contestant):
        try:
            connection = get_conection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO contestant(card, full_name, direction, gender, phone_number, date_of_birth, student_career,  genre_of_poetry, registration_date, declamation_date, age)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""".format(), (contestant.card,contestant.full_name, contestant.direction, contestant.gender, contestant.phone_number,contestant.date_of_birth, contestant.student_career,  contestant.genre_of_poetry, contestant.registration_date, contestant.declamation_date, contestant.age))
                affected_row = cursor.rowcount
                connection.commit()
            connection.close()

            return affected_row
        except Exception as ex:
            raise Exception(ex)

