from fastapi import FastAPI,Path,Query,Body
from enum import Enum
from typing import Optional,List
from pydantic import BaseModel


app = FastAPI() 
@app.get("/",description="this is our first route")
async def root():
    return {"message":"hello world"}

class Item(BaseModel):
    name:str
    description:Optional[str]=None
    price:float
    tax:Optional[float]=None

class User(BaseModel):
    userName:str
    fullName:Optional[str]=None


@app.put("/items/{item_id}")
async def update_item(
    *, item_id:int=Path(...,title="THe Id of the item ",gt=0,le=150)
    ,q:Optional[str]=None,
    item:Optional[Item]=None,
    user:User =Body(...,embed=True),
    importance:int=Body(...)
    ):

    results={'item_id':item_id}
    if q:
        results.update({"q":q})
    if item:
        results.update({"item":item})
    if user:
        results.update({"user":user})
    if importance:
        results.update({"importance":importance})
    return results

