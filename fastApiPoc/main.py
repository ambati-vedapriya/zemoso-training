from fastapi import FastAPI,Path,Query
from enum import Enum
from typing import Optional,List


world = FastAPI() 
@world.get("/",description="this is our first route", deprecated=True)
async def root():
    return {"message":"hello world"}

@world.post("/")
async def post():
    return {"message":"hello from the post route"}

@world.put("/")
async def put():
    return {"message":"hello from the put route"}

@world.get("/items")
async def list_item():
    return {"message":"list item route"}

@world.get("/items/{item_id}")
async def get_item(item_id:str):
    return {"item_id":item_id}

@world.get("/items/me")
async def get_curruent_user():
    return {"message":"tis is current user"}


class FoodEnum(str,Enum):
    fruits="fruits"
    vegetables="vegtables"
    dairy="dairy"

@world.get("/foods/{food_name}")
async def get_food(food_name:FoodEnum):
    if  food_name == FoodEnum.vegetables:
        return {"food_name":food_name,"message":"you are healthy"}

    if food_name==FoodEnum.fruits:
        return {"food_name":food_name,"message":"you are still healthy"}
    return {"food_name":food_name,"message":"you become fat"}

#after the start every argument is kwargs we keep this beacuse q:str will get eror if we keep it after the item_id 
@world.get("/items_validations/{item_id}")
async def read_items_validation(*,q:str,item_id:int=Path(...,title="the path variable")):
    resulr={"item_id":item_id}
    if q:
        resulr.update({"q":q})
    return resulr


@world.get("/items_validation/{item_id}")
async def read_items_validation(item_id:int=Path(...,title="the path variable",gt=10,le=100),q:Optional[str]=Query(None,alias="hai_everyone"),size:float=Query(...,gt=0,lt=7.75)):
    resulr={"item_id":item_id,"size":size}
    if q:
        resulr.update({"q":q})
    return resulr
