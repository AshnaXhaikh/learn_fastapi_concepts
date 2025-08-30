# 📘 Pydantic Models 

## 🔹 What is Pydantic?

* **Pydantic** is a Python library that helps you define and validate data.
* It makes sure the data you receive or send has the correct **type** (like string, integer, etc.).
* Mostly used with **FastAPI** but can also be used alone.

---

## 🔹 Why Use It?

* You don’t need to write manual checks (like `if not isinstance(name, str): ...`).
* It **automatically validates** data for you.
* It gives you **clean error messages** if the input is wrong.

---

## 🔹 Basic Example

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
```

✅ Correct data:

```python
user = User(name="Ashna", age=22)
print(user)
# name='Ashna' age=22
```

❌ Wrong data:

```python
user = User(name="Ashna", age="twenty two")
```

Output:

```
ValidationError: value is not a valid integer
```

---

## 🔹 With FastAPI

FastAPI automatically uses Pydantic models for request/response validation.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Login(BaseModel):
    username: str
    password: str

@app.post("/login")
async def login(user: Login):
    return {"message": f"Welcome, {user.username}!"}
```

👉 Send this JSON:

```json
{
  "username": "ashna123",
  "password": "mypassword"
}
```

👉 Response:

```json
{
  "message": "Welcome, ashna123!"
}
```
---
           ┌────────────┐
           │   User     │
           │ (raw data) │
           └─────┬──────┘
                 │
                 ▼
         ┌───────────────┐
         │ Pydantic Model │
         │ (define schema │
         │   + rules)     │
         └─────┬─────────┘
               │
               ▼
      ┌────────────────────┐
      │  Validation Step   │
      │ (checks types,     │
      │  constraints, etc.)│
      └───────┬────────────┘
              │
     ┌────────▼─────────┐
     │  Cleaned Output  │
     │ (validated data) │
     └──────────────────┘
     
This shows:

- User provides messy or raw data.
- Pydantic Model defines what valid data looks like.
- Validation automatically checks types & rules.
- Output is guaranteed clean and usable data.


## 🔹 Features of Pydantic Models

1. **Type checking** → Ensures `int`, `str`, `float` etc. are correct.
2. **Validation** → Throws error if data doesn’t match.
3. **Default values** → You can set defaults.

   ```python
   class User(BaseModel):
       name: str
       age: int = 18  # default age
   ```
4. **Nested models** → Models inside models.

   ```python
   class Address(BaseModel):
       city: str
       country: str

   class User(BaseModel):
       name: str
       address: Address
   ```

---

## 🔹 Best Practices

* Always inherit from `BaseModel`.
* Use **types** to make code clean.
* Add **default values** where possible.
* For beginners: stick to simple `str`, `int`, `float`, `bool`.

---

## 🚀 Summary

* **Pydantic = Data validation made easy** ✅
* Works great with **FastAPI** 🚀
* Reduces bugs and invalid data in your app 🔒

---
