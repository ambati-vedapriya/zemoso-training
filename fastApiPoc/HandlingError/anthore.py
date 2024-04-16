from typing import Optional, Union
from fastapi import FastAPI, Body, Form, HTTPException, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime, time, timedelta
from fastapi.exception_handlers import http_exception_handler, request_validation_exception_handler  # corrected import
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

app = FastAPI()

@app.exception_handler(StarletteHTTPException)
async def custom_exception_handler(request, exc):
    print(f"OMG! An HTTP error: {repr(exc)}")
    return await http_exception_handler(request, exc)  # corrected function call

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    print(f"OMG! A client sent invalidation data: {exc}")
    return await request_validation_exception_handler(request, exc)  # corrected function call

@app.get("/blah_items/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope1 i dont")
    return {"item_id": item_id}


#here we can able to the console also