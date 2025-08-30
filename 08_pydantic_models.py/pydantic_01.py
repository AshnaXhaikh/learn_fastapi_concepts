from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define request body schema
class User(BaseModel):
    username: str
    password: str

@app.post("/login")
async def login(user: User):
    return {"message": f"Welcome, {user.username}!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("pydantic_01:app", host="127.0.0.1", port=8001, reload=True)

# Extra Info:
#   - Pydantic automatically validates input data
#   - If invalid, FastAPI returns a clear error response
#   - Docs are generated automatically, no extra code needed