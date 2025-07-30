````markdown
# 🌐 Understanding Headers in FastAPI

Welcome! This guide explains what headers are, how to use them in FastAPI, and how to test them using Postman and cURL — all in easy, beginner-friendly language.

---

## 🧠 What Are Headers?

Think of headers like the **label on an envelope**:
- The main message is inside (body).
- Headers are instructions or extra info on the outside.

In web requests, **headers** tell the server extra details — like:
- Who is sending the request (device info)
- What kind of data is being sent (JSON, HTML)
- Whether the user is logged in (auth tokens)

---

## 📦 Common Real-World Headers

| Header Name         | Purpose                                            | Example Value                                               |
|---------------------|----------------------------------------------------|-------------------------------------------------------------|
| `User-Agent`        | Info about the browser or device                   | `"Mozilla/5.0 (Windows NT 10.0; Win64; x64)..."`            |
| `Authorization`     | Login or token info                                | `"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI..."` (JWT)             |
| `Content-Type`      | Format of the data being sent                      | `"application/json"`                                       |
| `Accept`            | Format client expects in response                  | `"application/json"`, `"text/html"`                        |
| `X-API-Key`         | Custom header for API access                       | `"my-secret-key"`                                          |
| `Accept-Language`   | Preferred language                                 | `"en-US"`, `"fr"`                                          |
| `Referer`           | Where the request came from                        | `"https://example.com"`                                    |

---

## 🧑‍💻 Using Headers in FastAPI (Code)

### ✅ Example Code:

```python
from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/greet")
def greet(user_agent: str = Header(None)):
    return {"Your device": user_agent}
````

### 🔍 What It Does:

* `user_agent`: This is a Python variable.
* `Header(None)`: Tells FastAPI to get the value from the request headers, and it's optional (default = `None`).
* FastAPI maps `user_agent` → `User-Agent` (replaces `_` with `-`).
* If the header isn't sent, the value will be `None`.

---

## 📌 Convention Notes

* Header names are **case-insensitive**.
* FastAPI converts `user_agent` → `User-Agent` automatically.
* Custom headers often use the `X-` prefix, like `X-Token`.

---

## 🧪 Testing Headers

### 🚀 Postman (Visual Tool)

* Open Postman.
* Choose the method (GET, POST).
* Enter your FastAPI URL like `http://localhost:8000/greet`.
* Go to the **Headers** tab and add:

  * Key: `User-Agent`
  * Value: `My Custom Device`
* Click **Send** to see the response.

### 💻 cURL (Command-Line Tool)

#### GET Request with Header:

```bash
curl -H "User-Agent: My Custom Device" http://localhost:8000/greet
```

#### POST with Token Header:

```bash
curl -X POST http://localhost:8000/secure \
  -H "Content-Type: application/json" \
  -H "X-Token: my-secret-token" \
  -d "{\"name\": \"Ashna\"}"
```

---

## ❓ Why Use Headers?

* ✅ Pass login tokens
* ✅ Describe the type of data
* ✅ Customize the response (language, format)
* ✅ Add security info
* ✅ Identify the source of the request

---

## 🧾 Summary

| Concept        | Meaning                                 |
| -------------- | ---------------------------------------- |
| Header         | Extra information sent in HTTP requests  |
| `Header(None)` | Optional header; returns `None` if not provided |
| `user_agent`   | Python variable name to capture the header |
| `User-Agent`   | Actual HTTP header sent by the client (e.g., browser or Postman) |
| Postman        | GUI-based tool used to test APIs         |
| cURL           | Command-line tool used to test APIs      |

---
### 📬 Postman Tool

Postman is a user-friendly tool to send HTTP requests to test APIs.

---
### 🧰 cURL Tool

cURL is a command-line tool to send HTTP requests and test APIs from the terminal.


---


