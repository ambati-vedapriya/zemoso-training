from typing import Optional, Union,List
from fastapi import FastAPI, Body,Cookie,Header
from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime,time,timedelta

app = FastAPI()

@app.get("/cookie")
async def read_items(
    cookie_id:Optional[str]=Cookie(None),
accept_encoding:Optional[str]=Header(None,convert_underscores=False),
sec_ch_ua:Optional[str]=Header(None),
user_agent:Optional[str]=Header(None),
x_token:Optional[List[str]]=Header(None)
):
    return {"cookie_id":cookie_id,
    "Accept_encoding":accept_encoding,
    "Sec_ch_ua":sec_ch_ua,
    "User_agent":user_agent,
    "X_token":x_token}