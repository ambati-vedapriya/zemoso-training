
from fastapi import FastAPI
from enum import Enum
from typing import Optional
from pydantic import BaseModel

app = FastAPI() 
@app.get("/",description="this is our first route")
async def root():
    return {"message":"hello world"}


class Item(BaseModel):
    name:str
    description:Optional[str]=None
    price:float
    tax:Optional[float] =None

@app.post("/item")
async def create_item(item:Item):
    item_dict=item.dict()
    if item.tax:
        price_with_tax=item.price+item.tax
        item_dict.update({"price_with_tax":price_with_tax})
    return  item_dict

@app.put("/items/{item_id}")
async def create_item_with_put(item_id:int,item:Item,q:Optional[str]=None):
    result={"item-id":item_id,**item.dict()}
    if q:
        result.update({"q":q})
    return result
