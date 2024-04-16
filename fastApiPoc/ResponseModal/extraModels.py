from fastapi import FastAPI,Path,Query,Body
from enum import Enum
from typing import Optional,List,Set,Dict,Literal,Union
from pydantic import BaseModel,EmailStr


app = FastAPI() 

class UserBase(BaseModel):
    username:str
    email:EmailStr
    full_name:Optional[str]=None



class UserIn(UserBase):
 
    password:str
   

class UserInDb(UserBase):
    
    hashed_password:str
    

def fake_password_hasher(raw_password:str):
    return f"supersecret{raw_password}"

def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDb(**user_in.dict(), hashed_password=hashed_password)
    print("user 'saved'")
    return user_in_db


@app.post("/user/",response_model=UserBase)
async def create_user(user_in:UserIn):
    user_saved=fake_save_user(user_in)
    return user_saved

class BaseItem(BaseModel):
    description: str
    type: str  # This field will be inherited by CarItem and PlaneItem

class CarItem(BaseItem):
    type: Literal["car"]  # Specific type for CarItem

class PlaneItem(BaseItem):
    type: Literal["plane"]  # Specific type for PlaneItem
    size: int


items={
    "item1":{"description":"all my frds drive car","type":"car"},
    "item2":{"description":"i love the plane","type":"plane","size":10}
}

@app.get("/items/{item_id}",response_model=Union[PlaneItem,CarItem])
async def read_item(item_id:Literal["item1","item2"]):
    return items[item_id]

class ListItem(BaseModel):
    name: str
    description: str

list_items = [
    {"name": "foo", "description": "this is good"},
    {"name": "Bar", "description": "this is nice"}
]

@app.get('/list_items/', response_model=List[ListItem])
async def read_item():
    return list_items

@app.get("/arbitrary", response_model=Dict[str, float])
async def get_arbitrary():
    return {"foo": 1, "bar": 2.0}