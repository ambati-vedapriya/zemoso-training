from sqlalchemy import Boolean, Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    phone_number=Column(String())

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    content = Column(String(70))
    user_id = Column(Integer(20))
