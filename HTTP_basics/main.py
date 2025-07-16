from fastapi import FastAPI
from app import basic_request_response
from app import status_examples
from app import header_examples
from app import json_examples

app = FastAPI(title="FastAPI HTTP Basics",
              description="This project teaches the **basics of HTTP in FastAPI** with modular, easy-to-follow examples.")


# Include routers from modules
app.include_router(basic_request_response.router, prefix="/request-response", tags=["Request/Response"])
app.include_router(status_examples.router, prefix="/status", tags=["Status Codes"])
app.include_router(header_examples.router, prefix="/headers", tags=["Headers"])
app.include_router(json_examples.router, prefix="/json", tags=["JSON Payloads"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8002, reload=True)