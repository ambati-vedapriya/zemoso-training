from api_module.database import Base
from sqlalchemy import Integer, Column, String


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index = True)


class Book(Base):
    __tablename__="books"

    id = Column(Integer, primary_key=True, unique=True)
    title = Column(String(50))

