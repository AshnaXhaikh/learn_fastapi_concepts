from fastapi import FastAPI

app = FastAPI()

@app.get("/required/{name}")
def read_required_param(name: str): # 👈 required
    """
    Endpoint demonstrating a required path parameter.
    
    Args:
        param (str): A required string parameter.
    
    Returns:
        dict: A response containing the received parameter.
    """
    return {"message": f"Hello, {name}!"}

@app.get("/optional")
def read_optional_param(name: str = "Guest"): # 👈 optional with default
    """
    Endpoint demonstrating an optional path parameter.

    Args:
        param (str, optional): An optional string parameter. Defaults to None.

    Returns:
        dict: A response containing the received parameter or a default message.
    """
    return {"message": f"Hello, {name}!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("req_params:app", host="127.0.0.1", port=8001, log_level="info", reload=True)