from typing import Union

from fastapi import Depends, FastAPI

app = FastAPI()

async def hello():
    return "world"
async def common_parameters(
    q: Union[str, None] = None, skip: int = 0, limit: int = 100,blah:str=Depends(hello)
):
    return {"q": q, "skip": skip, "limit": limit,"hello":blah}


@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons