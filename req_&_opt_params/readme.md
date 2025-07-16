# 🚀 FastAPI Mini App – Required and Optional Parameters

At the end I created a simple FastAPI app to demonstrate **required** and **optional** parameters using path and query examples.

---

## 📌 Features

✅ Required path parameters  
✅ Optional query parameters with defaults  
✅ Use of Optional from typing  
✅ Combined required and optional inputs

---

## 📁 Endpoints

- `/users/{user_id}` – Required path parameter
- `/greet` – Optional query with default
- `/search` – Optional query using Optional type
- `/products/{product_id}` – Path + optional query

---

## 🚀 Quick Start

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```
