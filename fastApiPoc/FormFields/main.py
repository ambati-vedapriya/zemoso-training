from typing import Optional, Union
from fastapi import FastAPI, Body, Form
from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime, time, timedelta

app = FastAPI()

#When you need to receive form fields instead of JSON, you can use Form

class User(BaseModel):
    userName: str
    password: str

@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    print("password", password) 
    return {"username": username}


@app.post("/login-json/")
async def login_json(user:User):
    return user