# main.py

from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing_extensions import Annotated
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models  
from typing import Optional, Union



app = FastAPI()
models.Base.metadata.create_all(bind=engine)



class BookBase(BaseModel):
    title: str
    author_id: int



class AuthorBase(BaseModel):
    name: str

class AuthorUpdate(BaseModel):
    name: Optional[str] = None

class BookBase(BaseModel):
    title: str
    author_id: int

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/authors/", status_code=status.HTTP_201_CREATED)
async def create_author(author: AuthorBase, db: db_dependency):
    db_author = models.Author(**author.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

@app.get("/authors/{author_id}", status_code=status.HTTP_200_OK)
async def read_author(author_id: int, db: db_dependency):
    author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

@app.put("/authors/{author_id}", status_code=status.HTTP_200_OK)
async def update_author(author_id: int, author_update: AuthorUpdate, db: db_dependency):
    db_author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")

    if author_update.name is not None:
        db_author.name = author_update.name

    db.commit()
    db.refresh(db_author)
    return db_author

@app.delete("/authors/{author_id}", status_code=status.HTTP_200_OK)
async def delete_author(author_id: int, db: db_dependency):
    db_author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")

    db.delete(db_author)
    db.commit()
    return {"message": "Author deleted successfully"}

@app.post("/books/", status_code=status.HTTP_201_CREATED)
async def create_book(book: BookBase, db: db_dependency):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int, db: db_dependency):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
