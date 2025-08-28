# #Users

# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# #DataBase SetUp

# DataBase_URL = "sqlite:///database.db"
# engine = create_engine(DataBase_URL, echo =True)

# # declarative base:

# Base = declarative_base()

# #Defining the Model

# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer,primary_key=True)
#     name = Column(String)
#     email = Column(String,unique=True)
      
# #Create tables

# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine) 

# #Create Session

# Session = sessionmaker(bind=engine)
# session =Session()

# #CRUD Operation
# #Create

# def create(username,useremail):
#     new_user = User(name=username, email=useremail)
#     session.add(new_user)
#     session.commit()
# create('Tshepang','tshepamok@gmail.com')

# #Read

# users = session.query(User).all()
# for user in users:
#     print(user.name,user.email)
    
# # Update

# user = session.query(User).filter_by(email='tshepamok@gmail.com').first()
# user.name = 'Bob'
# session.commit()

# # delete 

# def delete(user):
     
#     session.delete(user)
#     session.commit()


#Users

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError


DataBase_URL = "sqlite:///database.db"
engine = create_engine(DataBase_URL, echo=True)

Base = declarative_base()

#Defining the Model

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)  # Add password field

#Create tables
Base.metadata.create_all(engine)  # Commented out to prevent auto-creation

#Create Session
Session = sessionmaker(bind=engine)
session = Session()

#User Database Operations
def create_user(username, email, password):
    """Create a new user in the database"""
    try:
        new_user = User(name=username, email=email, password=password)
        session.add(new_user)
        session.commit()
        return new_user
    except IntegrityError:
        session.rollback()
        return None
    except Exception as e:
        session.rollback()
        print(f"Error creating user: {e}")
        return None

def get_user_by_email(email):
    """Get user by email address"""
    try:
        return session.query(User).filter_by(email=email).first()
    except Exception as e:
        print(f"Error getting user by email: {e}")
        return None

def get_user_by_id(user_id):
    """Get user by ID"""
    try:
        return session.query(User).filter_by(id=user_id).first()
    except Exception as e:
        print(f"Error getting user by ID: {e}")
        return None