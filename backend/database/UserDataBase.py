#Users

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

#DataBase SetUp

DataBase_URL = "sqlite:///database.db"
engine = create_engine(DataBase_URL, echo =True)

# declarative base:

Base = declarative_base()

#Defining the Model

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    name = Column(String)
    email = Column(String,unique=True)
    transactions = relationship("Transactions",back_populates="user")
      
#Create tables

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine) 

#Create Session

Session = sessionmaker(bind=engine)
session =Session()

#CRUD Operation
#Create

def create(username,useremail):
    new_user = User(name=username, email=useremail)
    session.add(new_user)
    session.commit()
create('Tshepang','tshepamok@gmail.com')

#Read

users = session.query(User).all()
for user in users:
    print(user.name,user.email)
    
# Update

user = session.query(User).filter_by(email='tshepamok@gmail.com').first()
user.name = 'Bob'
session.commit()

# delete 

def delete(user):
     
    session.delete(user)
    session.commit()
        
