from flask import jsonify
from db import get_conection
from entietes import Movie
import requests

class MovieModel():
    @classmethod
    def get_movies(self):
        try:
            connection = get_conection()
            movies=[]
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, title, url, classification FROM movies ORDER BY title ASC")
                resulset = cursor.fetchall()

                for row in resulset:
                    movie = Movie(row[0], row[1], row[2], row[3])
                    movies.append(movie.to_JSON())
            connection.close()
            return movies
        except Exception as ex:
            raise Exception(ex)
