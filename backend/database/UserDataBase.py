#Users

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#DataBase SetUp
DataBase_URL = "sqlite:///database.db"

engine = create_engine(DataBase_URL, echo =True)

# declarative base:
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    name = Column(String)
    email = Column(String,unique=True)
    
#Create tables
Base.metadata.create_all(engine) 