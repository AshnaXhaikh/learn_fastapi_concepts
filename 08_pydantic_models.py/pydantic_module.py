from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    description: str | None = None
    in_stock: bool = True

@app.post("/items/")
async def create_item(item: Item):
    return {"message": "Item created successfully", "item": item}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("pydantic_module:app", host="127.0.0.1", port=8001, reload=True)