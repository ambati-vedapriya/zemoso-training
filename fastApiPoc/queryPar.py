from fastapi import FastAPI,Query
from enum import Enum
from typing import Optional,List

app = FastAPI() 
@app.get("/",description="this is our first route")
async def root():
    return {"message":"hello world"}



fake_items_db=[{"item_name":"foo"},{"item_name":"fez"},{"item_name":"bar"}]

@app.get("/items")
async def list_item(skip: int =0,limit:int=10):
    return fake_items_db[skip:skip+limit]
#http://localhost:8000/items?skip=1

"""@app.get("/items/{items_id}")
async def get_item(items_id:str ,q:Optional[str]=None ): #q:str | None=None
    
    if q:
        return{"item_id":items_id,"q":q}
    return{"item_id":items_id}"""



@app.get("/items/{items_id}")
async def get_item(items_id: str, q: Optional[str] = None, short: bool = False):
    item = {"items_id": items_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "hai hello everyone dears"})
        
    return item

#http://localhost:8000/items/hello?q=world&short=1

@app.get("/users/{user_id}/items/{items_id}")
async def get_user_item(user_id:int,items_id:str, q: Optional[str] = None, short: bool = False):
    item = {"items_id": items_id,"user_id":user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "hai hello users have great items"})
        
    return item
    
@app.get("/item")
async def read_items(q:Optional[str]=Query(None,min_length=3,max_length=10,regex="^fixedquery$") ):
    result={"items":[{"item_id":"zip"},{"item_id":"zip1"}]}
    if q:
        result.update({"q":q})
    return result

#fixing the query here
@app.get("/itemFix")
async def read_items(q:str=Query("fixedquery",min_length=3,max_length=10) ):
    result={"items":[{"item_id":"once"},{"item_id":"upon"}]}
    if q:
        result.update({"q":q})
    return result


#Adding Valdation 

@app.get("/itemVali")
async def read_items(q:str=Query(...,min_length=3,max_length=10) ):
    result={"items":[{"item_id":"once"},{"item_id":"upon"}]}
    if q:
        result.update({"q":q})
    return result


@app.get("/itemMulti")
async def read_items(q:Optional[str]=Query(None) ):
    result={"items":[{"item_id":"once"},{"item_id":"upon"}]}
    if q:
        result.update({"q":q})
    return result

#http://localhost:8000/itemMulti?q=a&q=b --{"items":[{"item_id":"once"},{"item_id":"upon"}],"q":"b"}

@app.get("/itemListQ")
async def read_items(q:Optional[List[str]] =Query(None) ): # Query(["Foo","Bar"]) -default query will be foo and bar
    result={"items":[{"item_id":"once"},{"item_id":"upon"}]}
    if q:
        result.update({"q":q})
    return result

@app.get("/itemTitle")
async def read_items(q:Optional[str]=Query(None,max_length=10,title="samplequery string",description="sample ones",alias="item-query") ):
    result={"items":[{"item_id":"once"},{"item_id":"upon"}]}
    if q:
        result.update({"q":q})
    return result

@app.get("/hidden")
async def hidden_query_route(hidden_query:Optional[str]=Query(None,include_in_schema=False) ):
    result={"items":[{"item_id":"once"},{"item_id":"upon"}]}
    if hidden_query:
        return {"hidden":hidden_query}
    return {"hidden":"Not Found"}