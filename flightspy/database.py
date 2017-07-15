from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()

class Flights(Base):
    __tablename__ = 'flightdata'

    id = Column(Integer, primary_key=True)
