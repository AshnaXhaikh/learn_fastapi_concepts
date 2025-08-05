from fastapi import FastAPI

app = FastAPI()

# Sample data - list of dictionaries
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
]

# Endpoint that returns the list of dicts
@app.get("/users/")
async def get_users():
    return users
