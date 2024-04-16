from fastapi import FastAPI,Path,Query,Body
from enum import Enum
from typing import Optional,List,Set,Dict,Literal
from pydantic import BaseModel,HttpUrl,EmailStr


app = FastAPI() 



class UserBase(BaseModel):
    username:str 
    email:EmailStr
    full_name:Optional[str]=None



class UserIn(UserBase):
    password:str
    


@app.post("/user/",response_model=UserIn)
async def create_user(user:UserIn):
    return user



class Item(BaseModel):
    name:str
    description:Optional[str]=None
    price:float
    tax:Optional[float]=None
    tags:List[str]=None

items = {
    "foo": {"name": "foo", "price": 50.2},
    "bar": {"name": "Bae", "description": "this is first", "price": 50.2, "tax": 40.3},
    "baz": {"name": "Bze", "description": "this is second", "price": 40.2, "tags": []}
}

@app.post("/items/")
async def create_item(item:Item):
    return item

@app.get("/item/{item_id}",response_model=Item,response_model_exclude_unset=True)
async def read_item(item_id:Literal["foo","bar","baz"]):
    return items[item_id]


@app.get("/item/{item_id}/name",
response_model=Item,
response_model_include=["name","description"])
async def read_item_name(item_id:Literal["foo","bar","baz"]):
    return items[item_id]

@app.get("/item/{item_id}/public",
response_model=Item,
response_model_exclude=["tax"])
async def read_item_public_data(item_id:Literal["foo","bar","baz"]):
    return items[item_id]


"""
if we doesn't write the response_model_exclude_unset=True
we will get response as 
{
  "name": "foo",
  "description": null,
  "price": 50.2,
  "tax": null,
  "tags": null
}

"""