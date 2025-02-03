from fastapi import FastAPI # type: ignore

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI from Docker on Linux!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/items/")
async def add_item(name: str, location: int):
    return{"name":name, "location":location}