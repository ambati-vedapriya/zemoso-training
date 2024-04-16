from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import schemas, models
from api_module.exceptions import BookIdNotFoundException, AuthorNotFoundException

def create_book(db:Session,book: schemas.BookCreate):
    try:
        new_book = models.Book(title=book.title)
        db.add(new_book)
        db.commit()
        db.refresh(new_book)
        return new_book
    except:
        raise HTTPException(status_code=500, detail="Internal Server Error")

def create_author(db:Session,author: schemas.AuthorCreate):
    try:
        new_author = models.Author(name=author.name)
        db.add(new_author)
        db.commit()
        db.refresh(new_author)
        return new_author
    except:
        raise HTTPException(status_code=500, detail="Internal Server Error")

def get_all_books(db:Session, skip: int = 0, limit:int = 100):
    try:
        return db.query(models.Book).offset(skip).limit(limit).all()
    except:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    

def get_all_authors(db:Session, skip: int = 0, limit:int = 100):
    try:
        return db.query(models.Author).offset(skip).limit(limit).all()
    except:
        raise HTTPException(status_code=404, detail="There is no data")

    
def get_book_by_id(db:Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()
    
def get_author_by_id(db:Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()
  
def update_book(db: Session, book_id: int, book: schemas.BookCreate):
    try:
        db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
        db_book.title = book.title
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book
    except:
        raise BookIdNotFoundException(book_id) 

def update_author(db: Session, author_id: int, author: schemas.AuthorCreate):
    try:
        db_author = db.query(models.Author).filter(models.Author.id == author_id).first()
        db_author.name = author.name
        db.add(db_author)
        db.commit()
        db.refresh(db_author)
        return db_author
    except:
        raise AuthorNotFoundException(author_id)
   
def delete_book(db: Session, book_id: int):
    try:
        db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
        db.delete(db_book)
        db.commit()
        return {f"Book of {book_id} has been deleted":True}
    except:
        raise BookIdNotFoundException(book_id)
    

def delete_author(db: Session, author_id: int):
    try:
        db_author = db.query(models.Author).filter(models.Author.id == author_id).first()
        db.delete(db_author)
        db.commit()
        return {f"Author of {author_id} has been deleted":True}
    except:
        raise AuthorNotFoundException(author_id)