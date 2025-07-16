# 04_using_pydantic.py
"""FASTAPI USING PYDANTIC FOR DATA VALIDATION AND SERIALIZATION"""
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str # required field
    description: Optional[str] = None # optional field with default value
    price: float # required fields
    tax: Optional[float] = None # optional field with default value
    is_available: bool = True # optional field with default value
    tags: list[str] = [] # optional field with default value


@app.post("/items/")
def create_item(item: Item):
    """
    Create an item with the provided details.

    Args:
        item (Item): An instance of Item containing the item details.

    Returns:
        dict: The created item details.
    """
    return item.dict()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("04_using_pydantic:app", host="127.0.0.1", port=8001, reload=True)