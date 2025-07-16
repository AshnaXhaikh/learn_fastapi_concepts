# 03_req_opt_path_param.py
"""FASTAPI REQUIRED AND OPTIONAL PATH PARAMETERS DEMO"""
from fastapi import FastAPI 
from typing import Optional

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int): # 👈 required path param
    """Read an item by its ID.
    Args:
        item_id (int): The ID of the item to retrieve.
    """
    return {"item_id": item_id, "message": "Item retrieved successfully"}

@app.get("/items")
def read_items(item_id: Optional[int] = None): # 👈 optional query param
    """Read items with an optional query parameter.

    Args:
        item_id (Optional[int]): An optional integer parameter to filter items.
    
    Returns:
        dict: A response containing the item ID if provided.
    """
    return {"item_id": item_id} if item_id is not None else {"message": "No item ID provided"}

@app.get("/items/")
def read_item(item_id: int, q: Optional[str] = None): # 👈 required path param with optional query param

    """
    Read an item by its ID.

    Args:
        item_id (int): The ID of the item to retrieve.
        q (Optional[str]): An optional query parameter.

    Returns:
        dict: The item details.
    """
    return {"item_id": item_id, "query": q} if q else {"item_id": item_id}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("03_req_opt_path_param:app", host="127.0.0.1", port=8001, log_level="info", reload=True)
