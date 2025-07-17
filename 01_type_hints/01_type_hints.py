# Basic example of type hints in a function
def add(a: int, b: int) -> int:
    return a + b

# Example with string inputs
def greet(name: str) -> str:
    return f"Hello, {name}!"

# float input and return type
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

# Using Optional values
from typing import Optional

def get_user_email(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "user@example.com"
    return None

# Example calls
if __name__ == "__main__":
    print(add(3, 4))                   # 7
    print(greet("Ashna"))             # Hello, Ashna!
    print(apply_discount(100.0, 0.2))  # 80.0
    print(get_user_email(1))          # user@example.com
    print(get_user_email(99))

"""# practical uses

## 1. FastAPI / Pydantic Auto-validation & Docs

FastAPI heavily uses type hints for:

    Request validation (e.g., check query params, headers, JSON body)

    Automatic error responses

    Auto-generating Swagger UI and ReDoc
"""

from fastapi  import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
def create_item(item: Item):
    return item

"""If the request payload doesn’t match the Item structure, FastAPI auto-generates a 422 error response.

# **2. Runtime Type Checking (with help)**
With packages like:

    pydantic

    enforce

    typeguard

You can enforce type hints at runtime:
"""

from typeguard import typechecked

@typechecked
def add(a: int, b: int) -> float:
    return a + b

print(add(3, 2))      # ✅ Works
print(add("3", "2"))  # ❌ Raises TypeError
