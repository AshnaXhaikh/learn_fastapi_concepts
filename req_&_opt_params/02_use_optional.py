from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/hello")
def say_hello(name: Optional[str] = None):
    """
    Endpoint demonstrating an optional query parameter.
    
    Args:
        name (Optional[str]): An optional string parameter. Defaults to None.
    
    Returns:
        dict: A response containing a greeting message.
    """
    if name: 
        return {"message": f"Hello, {name}!"}
    return {"message": "Hello, Anonymous user!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("02_use_optional:app", host="127.0.0.1", port=8001,  reload=True)