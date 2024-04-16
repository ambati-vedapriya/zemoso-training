# models.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True)
    author_id = Column(Integer, ForeignKey('authors.id'))

    # Add relationship to Author model
    author = relationship("Author", back_populates="books")

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True)

    # Add relationship to Book model
    books = relationship("Book", back_populates="author")
