from fastapi import FastAPI,Path,Query,Body
from enum import Enum
from typing import Optional,List
from pydantic import BaseModel,Field


app = FastAPI() 
@app.get("/",description="this is our first route")
async def root():
    return {"message":"hello world"}

class Item(BaseModel):
    name:str
    description:Optional[str]=Field(None,title="this is description",max_length=20)
    price:float=Field(...,gt=0,description="should greater than none")



@app.put("/items/{item_id}")
async def update_item(item_id:int,item:Item=Body(...,embed=True)):
    results={'item_id':item_id,"item":item}
    return results