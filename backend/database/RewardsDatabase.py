from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import sqlite3

engine = create_engine('sqlite:///database.db', echo=True)

class Base(DeclarativeBase):
    pass
    
class Points(Base):
    __tablename__ = "points"
    id = Column(Integer, primary_key=True)
    activity = Column(String)
    points = Column(Integer)

class Tiers(Base):
    __tablename__ = "Member Level"
    id = Column(Integer, primary_key=True)
    tier = Column()


Base.metadata.create_all(engine)