## 📘 README: Returning `List[dict]` in FastAPI

In FastAPI, you often need to return multiple items as a **list of dictionaries**, especially for simple data like user records, product lists, or API responses.
This README demonstrates **two ways** to do that:

---

## 🧩 1️⃣ **Basic Return of `List[dict]`** (Without Type Hinting)

📁 **File:** `07_list_of_dicts.py`

```python
from fastapi import FastAPI

app = FastAPI()

users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
]

@app.get("/users/")
async def get_users():
    return users
```

### 🔹 Pros

* Very simple and quick
* Works well for quick testing or prototyping

### 🔹 Cons

* ❌ No validation of returned structure
* ❌ No OpenAPI documentation about what the response looks like
* ❌ No IDE hints for expected data format

---

## 🧩 2️⃣ **Using FastAPI’s Built-in Type Hinting and Validation**

📁 **File:** `07_list_of_dicts_typed.py`

```python
from fastapi import FastAPI
from typing import List, Dict, Any

app = FastAPI()

users_data: List[Dict[str, Any]] = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
]

@app.get("/users/", response_model=List[Dict[str, Any]])
async def get_users():
    return users_data
```

### 🔹 Pros

* ✅ Adds **type hints** and **automatic validation**
* ✅ FastAPI generates **clean documentation** at `/docs`
* ✅ Makes it easier to maintain and scale

### 🔹 Cons

* Slightly more complex for beginners

---

## ⚖️ When to Use Which?

| Use Case                     | Recommended Approach                            |
| ---------------------------- | ----------------------------------------------- |
| Quick testing or simple demo | **Basic return** without type hint              |
| Production / robust APIs     | ✅ **Use `response_model=List[Dict[str, Any]]`** |
| Structured data              | ✅ Better to use **Pydantic models** instead     |

---

## 🚀 Run and Test

```bash
uvicorn 07_list_of_dicts:app --reload
uvicorn 07_list_of_dicts_typed:app --reload
```

Access docs at:
➡️ `http://127.0.0.1:8000/docs`

---
