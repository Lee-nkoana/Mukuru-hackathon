from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import sqlite3

engine = create_engine('sqlite:///database.db')

class Base(DeclarativeBase):
    pass
    
class Points(Base):
    __tablename__ = "Points"
    id = Column(Integer, primary_key=True)
    Activity = Column(String)
    Points = Column(Integer)

# class Tiers(Base):
#     __tablename__ = "Member Level"
#     id = Column(Integer, primary_key=True)


Base.metadata.create_all(engine)
