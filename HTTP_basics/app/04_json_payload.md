
# FastAPI Account Creation API Documentation

## 📚 Core Concepts

### 1. **Pydantic Data Modeling**
```python
class Account(BaseModel):
    name: str
    balance: float 
    age: int
```
- **Type Validation**: Enforces data types (string, float, integer)
- **Required Fields**: All fields are mandatory by default
- **Automatic Docs**: Generates OpenAPI schema automatically

### 2. **APIRouter**
```python
router = APIRouter()
```
- **Modular Design**: Organize endpoints logically
- **Prefixes/Tags**: Can group related endpoints
- **Multiple Routers**: Combine in main `FastAPI()` app

### 3. **POST Request Handling**
```python
@router.post("/create-account")
def create_account(account: Account):
```
- **HTTP POST**: Used for resource creation
- **Request Body**: Automatically parses JSON → Pydantic model
- **Validation**: Returns 422 for invalid data

---

## 🛠️ Implementation Details

### Endpoint Specification

**`POST /create-account`**  
Creates a new bank account with validated data

**Request:**
```json
{
  "name": "string",
  "balance": number,
  "age": integer
}
```

**Successful Response (200 OK):**
```json
{
  "message": "Account created successfully",
  "account_details": {
    "name": "string",
    "balance": number,
    "age": integer
  }
}
```

**Validation Error (422 Unprocessable Entity):**
```json
{
  "detail": [
    {
      "loc": ["body", "field_name"],
      "msg": "error description",
      "type": "error_type"
    }
  ]
}
```

---

## 🚀 Runnable Code (Colab Version)

```python
# Install dependencies
!pip install fastapi uvicorn nest-asyncio pyngrok

# Imports
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
import nest_asyncio
from pyngrok import ngrok
import uvicorn

# Initialize app
app = FastAPI()
router = APIRouter()

# Data model
class Account(BaseModel):
    name: str
    balance: float
    age: int

# Endpoint
@router.post("/create-account")
def create_account(account: Account):
    return {
        "message": "Account created successfully",
        "account_details": account.dict()
    }

# Mount router
app.include_router(router)

# Colab setup
nest_asyncio.apply()
public_url = ngrok.connect(8000)
print("Public URL:", public_url)

# Start server
uvicorn.run(app, host="0.0.0.0", port=8000)
```

---

## 🔍 Testing Guide

### 1. Using cURL
```bash
# Success case
curl -X POST {URL}/create-account \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","balance":500.75,"age":28}'

# Error case (missing field)
curl -X POST {URL}/create-account \
  -H "Content-Type: application/json" \
  -d '{"name":"Bob","balance":1000}'
```

### 2. Using Python Requests
```python
import requests

response = requests.post(
    "{URL}/create-account",
    json={"name": "Carol", "balance": 750.50, "age": 32}
)
print(response.json())
```

### 3. Interactive Docs
Access `{URL}/docs` in browser to try the endpoint with UI

---

## 📊 Common Status Codes

| Code | Status               | Trigger Condition               |
|------|----------------------|---------------------------------|
| 200  | OK                   | Successful account creation     |
| 422  | Unprocessable Entity | Invalid/missing fields          |
| 500  | Server Error         | Unexpected server-side failure  |

---

## 💡 Best Practices

1. **Field Validation**: Add constraints using `Field()`
   ```python
   age: int = Field(..., gt=18, lt=100)
   ```
2. **Error Handling**: Customize error responses
3. **Logging**: Add request logging middleware
4. **Security**: Add authentication for production

---
