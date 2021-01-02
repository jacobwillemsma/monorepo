import datetime
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column('id', Integer, primary_key=True)
    email = Column('email', String, unique=True)
    first_name = Column('first_name', String)
    last_name = Column('last_name', String)
    created = Column(DateTime, default=datetime.datetime.now)
