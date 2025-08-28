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
    __tablename__ = "Tiers"
    id = Column(Integer, primary_key=True)
    tier = Column(String)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)

session = Session()

# create

Silver = Tiers(tier="Silver")
Gold = Tiers(tier="Gold")
Platinum = Tiers(tier="Platinum")

session.add_all([Silver, Gold, Platinum])

session.commit()

# read

