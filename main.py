from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import JSONResponse
import uvicorn

app = FastAPI()

class Item(BaseModel):
    user_id: str
    password: str

class PatchItem(BaseModel):
    user_id: Optional[str]
    password: Optional[str]


@app.get("/")
async def root():
    return {"message": "Hello, World"}

@app.post("/register")
async def register_item(item: Item):
    global dicted_item
    dicted_item = dict(item)
    dicted_item['success'] = True

    return JSONResponse(dicted_item)

@app.put("/update")
async def update_item(item: Item):
    dicted_item = {k:v for k, v in dict(item).items()}
    dicted_item['success'] = True

    return JSONResponse(dicted_item)

@app.patch("/update")
async def update_item_sub(item: PatchItem):
    for k, v in dict(item).items():
        if v :
            dicted_item[k] = v
    dicted_item['success'] = True

    return JSONResponse(dicted_item)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
