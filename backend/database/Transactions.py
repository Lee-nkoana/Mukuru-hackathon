from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, sessionmaker, relationship
import sqlite3
from UserDataBase import Base
import datetime

engine = create_engine('sqlite:///database.db', echo=True)

class Base(DeclarativeBase):
    pass
    
class Transactions(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    reference = Column(String)
    recipient = Column(String)
    amount = Column(Integer)
    date = Column(String)
    # currency = Column(String)
    
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)

session = Session()

# create

def addTransaction(reference, recipient, amount):
    newTransaction = Transactions(reference=reference, recipient=recipient, amount=amount, date=datetime.datetime.now())

    session.add(newTransaction)
    session.commit()
    return True

# read

def fetchTransactions():
    transactions = session.query(Transactions).all()

    for transaction in transactions:
        print(transaction.reference, transaction.recipient, transaction.amount)

def userTransactions(ID):
    return session.query(Transactions).filter_by(ID).first()

addTransaction("REF:Spoil Yourself", "1126315", 40)
addTransaction("REF:For School", "1955725", 2000)
addTransaction("REF:Shoes", "1946883", 100)
addTransaction("REF:Thanks", "4586265", 300)