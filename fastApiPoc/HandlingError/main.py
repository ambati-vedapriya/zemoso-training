from typing import Optional, Union
from fastapi import FastAPI, Body, Form, HTTPException, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime, time, timedelta
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY  # Added import for status

app = FastAPI()

items = {"foo": "the foos"}

@app.get("/items/{item_id}/")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"x-error": "there goes my error"}
        )
    return {"item": items[item_id]}

class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name

@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=410,
        content={"message": f"OOPs! {exc.name} did something"}
    )

@app.get("/unicorn/{name}")
async def read_unicorn(name: str):
    if name == 'yolo':
        raise UnicornException(name=name)

    return {"unicorn_name": name}


"""@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400) 

@app.exception_handler(StarletteHTTPException)
async def http_excption_handler(request,exc):
    return PlainTextResponse(str(exc.detail),status_code=exc.status_code)"""

    

@app.get("/validation_items/{item_id}")
async def read_validation(item_id:int):
    if item_id ==3:
        raise HTTPException(status_code=418,detail="Oops I dont like 3")
    return {"item_id":item_id}

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,  # Corrected reference to HTTP status code
        content=jsonable_encoder({"detail": exc.errors(), "see this": exc.body})
    )

class Item(BaseModel):
    title:str
    size:int

@app.post("/items/")
async def create_item(item: Item):
    return item


