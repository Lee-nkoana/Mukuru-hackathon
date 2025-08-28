from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import sqlite3
from UserDataBase import Base

engine = create_engine('sqlite:///database.db', echo=True)
    
class Points(Base):
    __tablename__ = "points"
    id = Column(Integer, primary_key=True)
    activity = Column(String)
    points = Column(Integer)

class Tiers(Base):
    __tablename__ = "Tiers"
    id = Column(Integer, primary_key=True)
    tier = Column(String)
    description = Column(String)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)

session = Session()

# create Tiers

Silver = Tiers(tier="Silver",description="New members or those with a low level of activity/spend.")
Gold = Tiers(tier="Gold", description="Members who reach a moderate spending threshold or maintain consistent engagement.")
Platinum = Tiers(tier="Platinum", description="High-value members who achieve the highest spending/engagement threshold.")

session.add_all([Silver, Gold, Platinum])

session.commit()

# read Tiers


def tiers():
    tiers = session.query(Tiers).all()
    for tier in tiers:
        print(f"Tier: {tier} \nDescription: {tier.description}")


#create points

transactions = session.add(Points(activity="Transaction", points=1))
session.commit()
# read points

def points():
    activities = session.query(Points).all()
    for activity in activities:
        print(f"Activity: {activity}")