from sqlalchemy import Boolean, Column, String, Integer
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    last_name = Column(String, unique=True, index=True)
    email = Column(String, index=True)
    phone = Column(Integer)
    birthday = Column(String)
    extra_data = Column(String)