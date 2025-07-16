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

## Test in Browser
- Visit `http://localhost:8000/docs` for interactive testing
- Try the "Try it out" buttons for each endpoint

## Next Steps
1. Add error handling (try invalid account IDs)
2. Expand with query parameters (`/accounts?min_balance=500`)
3. Move to router-based organization



bank_api/

├── main.py                 # HQ - coordinates everything

├── routers/                # Departments

│   ├── __init__.py

│   ├── accounts.py         # Account management

│   ├── loans.py            # Loan services

│   └── auth.py             # Authentication

├── models/                 # Data structures

│   └── schemas.py          # Request/response formats

├── dependencies.py         # Shared utilities

├── tests/                  # Quality control

│   └── test_accounts.py

└── requirements.txt        # Required packages