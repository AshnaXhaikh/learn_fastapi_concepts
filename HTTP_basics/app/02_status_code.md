
# FastAPI Response Examples Documentation

## 📚 Core Concepts

### 1. HTTP Status Codes
FastAPI uses standard HTTP status codes to indicate request outcomes:
- `200 OK`: Successful request
- `201 Created`: Resource successfully created
- `204 No Content`: Successful request with empty response
- `400 Bad Request`: Invalid client input
- `404 Not Found`: Resource doesn't exist
- `500 Internal Server Error`: Server-side error

### 2. Response Types
- **Basic Dict**: Automatically converted to JSON
- **JSONResponse**: For explicit control over status codes and headers
- **Empty Response**: For 204 No Content responses

### 3. Status Code Specification
Three ways to set status codes:
1. Default status codes (200 for GET, 201 for POST)
2. `status_code` parameter in route decorators
3. Explicitly returning status codes with responses

---

## 🛣️ API Endpoints

### 1. Basic Success Response
**Endpoint:** `GET /ok`  
**Status Code:** 200 (default)  
**Purpose:** Standard successful operation

**Response:**
```json
{
  "message": "Everything is OK"
}
```

**Implementation:**
```python
@router.get("/ok")
def ok_response():
    return {"message": "Everything is OK"}
```

---

### 2. Resource Creation
**Endpoint:** `POST /created`  
**Status Code:** 201 (explicitly set)  
**Purpose:** Successful resource creation

**Response:**
```json
{
  "message": "Resource created"
}
```

**Implementation:**
```python
@router.post("/created", status_code=status.HTTP_201_CREATED)
def created_response():
    return {"message": "Resource created"}
```

---

### 3. Conditional Response
**Endpoint:** `GET /not-found/{item_id}`  
**Status Codes:**
- 200 if item exists
- 404 if item doesn't exist

**Example Requests:**
```http
GET /not-found/1  # Exists → 200
GET /not-found/99 # Doesn't exist → 404
```

**Responses:**
```json
// 200 Response
{
  "item": "Apple"
}

// 404 Response
{
  "detail": "Item not found"
}
```

**Implementation:**
```python
@router.get("/not-found/{item_id}")
def not_found(item_id: int):
    fake_db = {1: "Apple", 2: "Banana"}
    if item_id in fake_db:
        return {"item": fake_db[item_id]}
    return {"detail": "Item not found"}, status.HTTP_404_NOT_FOUND
```

---

### 4. Empty Response
**Endpoint:** `DELETE /deleted`  
**Status Code:** 204 (explicitly set)  
**Purpose:** Successful deletion with no content

**Response Body:** None

**Implementation:**
```python
@router.delete("/deleted", status_code=status.HTTP_204_NO_CONTENT)
def delete_item():
    return
```

---

### 5. Error Responses

#### Bad Request (400)
**Endpoint:** `GET /bad-request`  
**Purpose:** Simulate invalid client input

**Response:**
```json
{
  "error": "Bad request. Your input was invalid."
}
```

**Implementation:**
```python
@router.get("/bad-request")
def bad_request():
    return JSONResponse(
        content={"error": "Bad request. Your input was invalid."},
        status_code=status.HTTP_400_BAD_REQUEST
    )
```

#### Server Error (500)
**Endpoint:** `GET /error`  
**Purpose:** Simulate server failure

**Response:**
```json
{
  "error": "Something went wrong"
}
```

**Implementation:**
```python
@router.get("/error")
def error_response():
    return JSONResponse(
        content={"error": "Something went wrong"},
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    )
```

---

## 🧩 Complete Router Setup
```python
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter()

# [All endpoint implementations shown above]
```

---

## 🚀 Usage Patterns

### 1. Returning Different Status Codes
```python
# Method 1: Decorator parameter
@router.post("/items", status_code=201)

# Method 2: Return tuple
return data, status.HTTP_201_CREATED

# Method 3: JSONResponse
return JSONResponse(..., status_code=400)
```

### 2. Response Structure Best Practices
- Success: Include `message` or `data` field
- Errors: Use `detail` or `error` field
- 404: Always specify what wasn't found
- 400: Include validation details when available

### 3. Testing Recommendations
```bash
# Test happy path
curl -X GET http://localhost:8000/ok

# Test error case
curl -X GET http://localhost:8000/not-found/99 -v
```

