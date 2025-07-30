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


