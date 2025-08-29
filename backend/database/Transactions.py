from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, sessionmaker, relationship
import sqlite3
from .UserDataBase import Base

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
    newTransaction = Transactions(reference=reference, recipient=recipient, amount=amount)

    session.add(newTransaction)
    session.commit()

# read

def fetchTransactions():
    transactions = session.query(Transactions).all()

    for transaction in transactions:
        print(transaction.reference, transaction.recipient, transaction.amount, transaction.currency)

def userTransactions(User):
    return session.query(Transactions).filter_by(User).first()