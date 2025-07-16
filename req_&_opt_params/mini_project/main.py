from fastapi import FastAPI
from typing import Optional

app = FastAPI(title="Required vs. Optional Example",
              description="A mini FastAPI app to demonstrate required and optional parameters with path and query examples for easy learning.",
              version="1.1.1")

# 1. Required path parameter
@app.get("/users/{user_id}")
def get_userId(user_id: int):
    return {"user_id": user_id}

# 2. Optional query parameter with default
@app.get("/greet")
def say_hello(name: str = "Anonymous user"):
    return {"message": f"Hello, {name}!"}

# 3.  Optional query param with Optional type
@app.get("/search")
def search_items(q: Optional[str] = None):
    if q:
        return {"result": f"Searching for {q}"}
    return {"result": "Showing all items"}

# 4. Combined required path + optional query
@app.get("/products/{product_id}")
def get_product(product_id: int, details: Optional[bool] = False):
    return {"product_id": product_id, "details": details}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8001, log_level="info", reload=True)


