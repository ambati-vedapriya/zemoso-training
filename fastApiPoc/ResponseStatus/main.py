from fastapi import FastAPI,status

app = FastAPI()


@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}

@app.delete("/items/{pk}",status_code=204)
async def delete_item(pk:str):
    print("pk",pk)
    return pk

@app.get("/items",status_code=301)
async def read_item_redirect():
    return{"hello":"world"}



@app.post("/item/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}