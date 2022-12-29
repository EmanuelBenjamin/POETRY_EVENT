import psycopg2
from decouple import config
from psycopg2 import DatabaseError
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, create_engine, Date  

Base = declarative_base()
def get_conection():
    try:
        return psycopg2.connect(
            host = config('PGSQL_HOST'),
            user = config('PGSQL_USER'),
            password = config ('PGSQL_PASSWORD'),
            database = config('PGSQL_DATABASE')
         )
    except DatabaseError as ex:
        raise ex

class contestant (Base):
    __tablename__ = 'contestant'

    id = Column(Integer,primary_key = True)
    card = Column(String, nullable = False)
    full_name = Column(String, nullable = False)
    direction = Column(String, nullable = False)
    gender = Column(String, nullable = False )
    phone_number=Column(String, nullable = False)
    date_of_birth = Column(String,nullable = False )
    student_career = Column(String,nullable = False )
    genre_of_poetry = Column(String,nullable = False )
    Registration_date = Column(Date,nullable = False )
    declamation_date = Column(Date,nullable = False )
    age = Column(Integer, nullable = False)


engine = create_engine('postgresql://postgres:12345@localhost/database1')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
