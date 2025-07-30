# this is for colab env
from fastapi import FastAPI
from pydantic import BaseModel, Field
from pyngrok import ngrok
import nest_asyncio
import uvicorn
import threading

# Enable nested event loop (important for Colab)
nest_asyncio.apply()

# Define app
app = FastAPI()

# Define the model with field validation
class User(BaseModel):
    name: str = Field(..., min_length=3, max_length=20, description="Full name of the user")
    age: int = Field(..., gt=18, lt=100, description="Age must be between 19 and 99")
    balance: float = Field(..., ge=0, description="Initial balance must be zero or positive")

@app.post("/create-user")
def create_user(user: User):
    return {"message": "User created successfully", "user": user}

# Start ngrok tunnel
public_url = ngrok.connect(8000)
print("🚀 Public URL:", public_url)

# Run the app in a background thread
def run():
    uvicorn.run(app, port=8000)

thread = threading.Thread(target=run)
thread.start()
