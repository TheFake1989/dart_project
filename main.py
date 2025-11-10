#lib imports
from fastapi import FastAPI

#function imports
from models.player import *
from models.rules import *


app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

