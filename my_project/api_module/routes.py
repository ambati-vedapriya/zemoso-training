from fastapi import Depends, APIRouter
from fastapi.responses import JSONResponse
from typing_extensions import Annotated,List
from sqlalchemy.orm import Session
from api_module.database import Base, engine
from api_module import schemas, crud
from api_module.utils import get_db
from api_module.exceptions import BookIdNotFoundException, AuthorNotFoundException

router = APIRouter(tags=["Routes"])

Base.metadata.create_all(bind=engine)

db_dependency = Annotated[Session, Depends(get_db)]

#---------------------------------------------------

@router.get("/books",response_model=List[schemas.Books])
def get_all_books(db: db_dependency, skip: int = 0, limit: int = 100):
    return crud.get_all_books(db,skip,limit)

@router.get("/authors",response_model=List[schemas.Authors])
def get_all_authors(db: db_dependency, skip: int = 0, limit: int = 100):
    return crud.get_all_authors(db,skip,limit)

#---------------------------------------------------

@router.post("/books", response_model=schemas.Books)
def create_new_book(db: db_dependency, new_book: schemas.BookCreate):
    return crud.create_book(db, new_book)
    
@router.post("/authors", response_model=schemas.Authors)
def create_new_book(db: db_dependency, new_author: schemas.AuthorCreate):
    return crud.create_author(db, new_author)

#---------------------------------------------------

@router.get('/books/{book_id}',response_model=schemas.Books)
def get_book_by_id(db: db_dependency, book_id: int):
    db_book = crud.get_book_by_id(db, book_id)
    if db_book is None :
        raise BookIdNotFoundException(book_id)
    return crud.get_book_by_id(db, book_id)
      
@router.get('/authors/{author_id}',response_model=schemas.Authors)
def get_author_by_id(db: db_dependency, author_id: int):
    db_author = crud.get_author_by_id(db, author_id)
    if db_author is None :
        raise AuthorNotFoundException(author_id)
    return crud.get_author_by_id(db, author_id)

#---------------------------------------------------

@router.put('/books/{book_id}', response_model=schemas.Books)
def update_book(db: db_dependency, book_id: int, book: schemas.BookCreate):
    return crud.update_book(db, book_id, book)
   
@router.put('/authors/{author_id}', response_model=schemas.Authors)
def update_author(db: db_dependency, author_id: int, author: schemas.AuthorCreate):
    return crud.update_author(db, author_id, author)

#---------------------------------------------------

@router.delete('/books/{book_id}', response_class = JSONResponse)
def delete_book_by_id(db: db_dependency, book_id: int):
    return crud.delete_book(db, book_id)
   
@router.delete('/authors/{author_id}', response_class = JSONResponse)
def delete_author_by_id(db: db_dependency, author_id: int):
    return crud.delete_author(db, author_id)

#---------------------------------------------------