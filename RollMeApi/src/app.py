# Begin by creating the actual dice roller. 
from typing import Optional, List
from fastapi import FastAPI, Query

from RollMeApi.src.roller import Roller

app = FastAPI()

@app.get("/", tags=['ROOT'])
async def root() -> dict :
    return {"status":"Ready to Roll"}

@app.get("/roll/", status_code=200)
async def dice_roll(q : Optional[List[str]] = Query(None)) -> dict:
    results_list = list()
    for v in q:
        num = int(v.split('d')[0])
        sides = int(v.split('d')[1])
        res = Roller(num, sides).roll()
        for r in res:
            results_list.append({"value":r,"type":f"d{sides}"})

    

    return {
        "dice":f"{results_list}"
    }

