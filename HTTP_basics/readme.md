# FastAPI HTTP Methods Starter

Learn the 5 essential HTTP methods with this simple banking API example.

## How to Use
1. Install requirements:
```bash
pip install fastapi uvicorn
```

2. Run the server:
```bash
uvicorn http_methods:app --reload
```

## Endpoint Examples
| Method | Endpoint                | Description                  |
|--------|-------------------------|------------------------------|
| GET    | `/accounts/123`         | Check account balance        |
| POST   | `/accounts`             | Create new account           |
| PUT    | `/accounts/123`         | Update entire account        |
| PATCH  | `/accounts/123`         | Adjust balance               |
| DELETE | `/accounts/123`         | Close account                |



# 🚀 FastAPI HTTP Basics

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.7+-blue?style=for-the-badge&logo=python)

A modular FastAPI project demonstrating core HTTP concepts through practical examples.

## 📌 Features

✔ **Four Essential Modules**  
✔ **Interactive Documentation**  
✔ **Ready-to-Run Examples**  
✔ **Production-Ready Structure**

## 🌐 API Endpoints

| Module            | Base Path          | Description                     | Try It                          |
|-------------------|--------------------|---------------------------------|---------------------------------|
| Request/Response  | `/request-response`| Basic GET/POST operations       | `http://127.0.0.1:8002/docs#/Request/Response` |
| Status Codes      | `/status`          | HTTP status code examples       | `http://127.0.0.1:8002/docs#/Status%20Codes` |
| Headers           | `/headers`         | Request/response header handling| `http://127.0.0.1:8002/docs#/Headers` |
| JSON Payloads     | `/json`            | JSON request/response patterns  | `http://127.0.0.1:8002/docs#/JSON%20Payloads` |

## 🛠️ Setup & Run

```bash
# Install dependencies
pip install fastapi uvicorn

# Run the server
uvicorn main:app --host 127.0.0.1 --port 8002 --reload
```

## 📚 Learning Resources

1. Test endpoints at `http://127.0.0.1:8002/docs`
2. Check auto-generated schemas at `http://127.0.0.1:8002/redoc`
3. View raw OpenAPI spec at `http://127.0.0.1:8002/openapi.json`

## 🏗️ Project Structure

```
/app
│
├── basic_request_response.py  # Core request/response flows
├── status_examples.py         # HTTP status code demos
├── header_examples.py         # Header manipulation
└── json_examples.py           # JSON payload handling
```

## 💡 Example Request

```bash
curl -X GET "http://127.0.0.1:8002/request-response/hello" -H "accept: application/json"
```

## 📜 License

MIT License - Free for learning and modification
```

