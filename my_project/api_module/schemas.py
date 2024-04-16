from typing import List
from pydantic import BaseModel

class AuthorBase(BaseModel):
    name: str

class BookBase(BaseModel):
    title: str

class AuthorCreate(AuthorBase):
    pass


class BookCreate(BookBase):
    pass

class Books(BookBase):
    id: int

    class Config:
        orm_mode = True

class Authors(AuthorBase):
    id: int

    class Config:
        orm_mode = True
