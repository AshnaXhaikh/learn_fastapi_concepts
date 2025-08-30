# 🚀 FastAPI Learning Plan and Notes

This repository documents my learning plan and notes for starting with **FastAPI** as a Python developer.

---

## ✅ 1️⃣ What is FastAPI?
FastAPI is a modern, high-performance Python framework for building APIs quickly and with automatic validation and documentation.  
- Built on Starlette (web) and Pydantic (validation).  
- Supports async and sync routes.  
- Generates interactive docs automatically.

---

# 🚀 FastAPI Basics Walkthrough

This repo is a step-by-step guide to learning **FastAPI fundamentals**, one concept at a time.

Each Python file in the `app/` folder covers a single topic, like:

- ✅ Type hints in route functions
- ✅ HTTP methods (GET, POST, etc.)
- ✅ Returning status codes
- ✅ Handling headers
- ✅ Working with JSON
- ✅ REST API structure
- ✅ Pydantic models for validation

## 📁 File Guide

| File                          | Concept                         |
|-------------------------------|----------------------------------|
| 01_type_hints.py              | Function annotations             |
| 02_http_methods.py            | GET, POST, PUT, DELETE routes    |
| 03_status_codes.py            | Custom status responses          |
| 04_headers.py                 | Request headers                  |
| 05_json_response.py           | Returning JSON                   |
| 06_rest_api_example.py        | RESTful endpoint design          |
| 07_list_of_dicts.py           | Return `List[dict]`              |
| 08_pydantic_model.py          | Request body with BaseModel      |


# FastAPI Basics – Step by Step 🚀

This repo contains small, easy examples to understand **FastAPI fundamentals**. Each Python file introduces one concept in a simple way.

---

## 1️⃣ Type Hints – `01_type_hints.py`

Python **type hints** help us tell FastAPI (and ourselves) what type of data a function expects/returns.

```python
def add(a: int, b: int) -> int:
    return a + b
```

* `a: int` means `a` should be an integer
* `-> int` means the function returns an integer

---

## 2️⃣ HTTP Methods – `02_http_methods.py`

FastAPI supports common **HTTP methods**:

* `GET` → fetch data
* `POST` → create data
* `PUT` → update data
* `DELETE` → remove data

---

## 3️⃣ Status Codes – `03_status_codes.py`

We can send **custom responses** with status codes:

* `200` → OK
* `201` → Created
* `404` → Not Found
* `500` → Server Error

---

## 4️⃣ Headers – `04_headers.py`

You can access **request headers** (like `User-Agent`, `Authorization`) from clients.

---

## 5️⃣ JSON Response – `05_json_response.py`

FastAPI automatically returns **JSON**. Example:

```python
@app.get("/items")
def get_items():
    return {"id": 1, "name": "Book"}
```

---

## 6️⃣ REST API Example – `06_rest_api_example.py`

Shows how to design a **RESTful endpoint**:

* `/users` → list all users (GET)
* `/users/{id}` → get one user (GET)
* `/users` → create a user (POST)
* `/users/{id}` → update a user (PUT)
* `/users/{id}` → delete a user (DELETE)

---

## 7️⃣ List of Dicts – `07_list_of_dicts.py`

We can return a **list of dictionaries** in JSON:

```python
@app.get("/users")
def get_users():
    return [
        {"id": 1, "name": "Ayan"},
        {"id": 2, "name": "Ali"}
    ]
```

---

## 8️⃣ Pydantic Models – `08_pydantic_model.py`

Pydantic’s `BaseModel` validates request bodies automatically.

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
```

* If the request has wrong data (e.g. `id` as text), FastAPI returns an error.
* You get **clean, validated data** without extra code.

---

## 🚀 How to Run

1. Install FastAPI & Uvicorn (only once):

   ```bash
   pip install fastapi uvicorn
   ```
2. Run any file:

   ```bash
   uvicorn 01_type_hints:app --reload
   ```
3. Open docs: 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

✅ With these 8 examples, you’ll understand the **core of FastAPI**: type hints, routes, responses, REST design, and validation.

---
