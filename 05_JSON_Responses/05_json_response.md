# 📝 FastAPI JSON Responses Guide
`05_json_response.py` – Learn how to return JSON responses in FastAPI

## 🎯 Learning Objectives
1. Understand automatic JSON conversion
2. Learn explicit `JSONResponse` usage
3. Handle error responses in JSON format

## 🛠️ Code Breakdown

### 1. Automatic JSON Conversion
```python
@app.get("/simple-json")
def simple_json():
    return {"message": "This is a simple JSON response", "status": "success"}
```
🔹 **Key Points**:
- FastAPI **automatically converts** dictionaries to JSON
- Default status code: `200 OK`
- Sets `Content-Type: application/json` header automatically

**Test it:**
```bash
curl http://localhost:8000/simple-json
```

### 2. Explicit JSONResponse
```python
@app.get("/custom-json")
def custom_json():
    data = {
        "user": "Ashna",
        "role": "Data Scientist",
        "active": True
    }
    return JSONResponse(content=data, status_code=200)
```
🔹 **When to Use**:
- Need custom headers
- Require explicit status codes
- Want to modify JSON serialization behavior

**Try adding headers:**
```python
return JSONResponse(
    content=data,
    headers={"X-Custom-Header": "value"}
)
```

### 3. Error Responses
```python
@app.get("/error-json")
def error_json():
    error_detail = {
        "error": "Resource not found",
        "code": 404
    }
    return JSONResponse(content=error_detail, status_code=404)
```
🔹 **Best Practices**:
- Always include `error` and `code` fields
- Use standard HTTP status codes
- Keep error messages consistent

**Example Error Output:**
```json
{
  "error": "Resource not found",
  "code": 404
}
```

## 📚 Comparison Table

| Approach               | Pros                          | Cons                     |
|------------------------|-------------------------------|--------------------------|
| **Automatic**          | Simple, less code             | Less control             |
| **JSONResponse**       | Full control over response    | More verbose             |
| **Error JSON**         | Standardized error handling   | Manual status codes      |

---
