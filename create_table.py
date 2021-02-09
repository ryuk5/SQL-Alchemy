from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# first step is to create an engine
# the create engine func. take a params:
# 1-: the type of the db: postgresql
# 2-: the username
# 3-: the password
# 4-: the adress @localhost:5432
# 5-: the name of the db alchemy
engine = create_engine('postgresql://postgres:admin@localhost:5432/alchemy', echo=False)

# Second step is to create a session
Session = sessionmaker(bind=engine)
session = Session()

# Third step is creating the table

# Preapring the Base class
Base = declarative_base() 

# create our class which will be our table in the db and inherits from Base
class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))

# Fourth step is to migrate our class to reflect that inside our db
# Base.metadata.create_all(engine) # This code is used to migrate
# ==> This cmd is used once we don't need to migrate anything in the upcoming execution of our pyhon program