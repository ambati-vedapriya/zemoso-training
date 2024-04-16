"""from typing import Optional, Union, Set
from enum import Enum  # Added import for Enum
from fastapi import FastAPI, Body, Form, HTTPException, Request, status
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime, time, timedelta
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()

class Tags(Enum):
    items = "items"
    users = "users"

@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED, tags=[Tags.items], summary="create an item", description="created the item",
"name; description; price; tax; and set of"
"unique tags")
async def create_item(item: Item):
    return item

@app.get("/items/", tags=[Tags.items])
async def read_items():
    return [{"name": "fii", "price": 45}]

@app.get("/users/", tags=[Tags.users])
async def read_users():
    return [{"username": "veda"}]
"""
from typing import Set, Union

from enum import Enum
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()


class Tags(Enum):
    items = "items"
    users = "users"

@app.post("/items/", response_model=Item, summary="Create an item",response_description="The created item",)
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item

@app.get("/items/", tags=[Tags.items])
async def get_items():
    return ["Portal gun", "Plumbus"]


@app.get("/users/", tags=[Tags.users])
async def read_users():
    return ["Rick", "Morty"]