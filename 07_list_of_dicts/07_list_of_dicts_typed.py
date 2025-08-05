from fastapi import FastAPI
from typing import List, Dict, Any

app = FastAPI()

# Sample data as a list of dictionaries
users_data: List[Dict[str, Any]] = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
]

# Return type is explicitly List[Dict[str, Any]]
@app.get("/users/", response_model=List[Dict[str, Any]])
async def get_users():
    return users_data
