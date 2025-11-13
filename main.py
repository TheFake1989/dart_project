#lib imports
from fastapi import FastAPI

#function imports
from models.player import *
from models.rules import *
from models.throw_logic import *




def main ():
    players = []
    jonas = Player("Jonas")
    players.append(jonas)
    print(jonas.score)

    shoot_down(players, 40)
    print(jonas.score)
    print(jonas.game)
    jonas.record_round((10, 1), (16, 2), (0, 3))


main()

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

