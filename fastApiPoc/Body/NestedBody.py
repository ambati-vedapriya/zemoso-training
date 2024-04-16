from fastapi import FastAPI,Path,Query,Body
from enum import Enum
from typing import Optional,List,Set,Dict
from pydantic import BaseModel,HttpUrl


app = FastAPI() 
@app.get("/",description="this is our first route")
async def root():
    return {"message":"hello world"}

"""class Image(BaseModel):
    url:str=Field(...,
    regex="^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)$")
    name:str"""
class Image(BaseModel):
    url:HttpUrl
    name:str

class Item(BaseModel):
    name:str
    description:Optional[str]=None
    price:float
    tax:Optional[float]=None
    tags:Set[str]=set()
    image:Optional[List[Image]]=None
class Offer(BaseModel):
    name:str
    description:Optional[str]=None
    price:float
    items:List[Item]

@app.put("/items/{item_id}")
async def update_item(item_id:int,item:Item):
    results={"item_id":item_id,"item":item}
    return results

@app.post("/offers")
async def create_offer(offer:Offer=Body(...,embed=True)):
    return offer

@app.post("/images/multiple")
async def create_mutiple_images(images:List[Image]):
    return images

@app.post("/blah")
async def create_some_blahs(blahs:Dict[int,float]):
    return blahs

"""{
  "1": 4,
  "2": 5,
  "4": 6
}"""