# json_responses_api.py
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

# Basic JSON response
@app.get("/simple-json")
def simple_json():
    return {"message": "This is a simple JSON response", "status": "success"}

# JSON response using JSONResponse explicitly
@app.get("/custom-json")
def custom_json():
    data = {
        "user": "Ashna",
        "role": "Data Scientist",
        "active": True
    }
    return JSONResponse(content=data, status_code=200)

# Error response as JSON
@app.get("/error-json")
def error_json():
    error_detail = {
        "error": "Resource not found",
        "code": 404
    }
    return JSONResponse(content=error_detail, status_code=404)

if __name__ == "__main__":
    # Run on localhost with auto-reload
    uvicorn.run(
        "json_responses_api:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
