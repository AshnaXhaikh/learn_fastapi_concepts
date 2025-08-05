## 📘 README: Understanding HTTP Request Headers

### 🔹 What are Request Headers?

**Request headers** are key-value pairs sent by the **client (your code/browser)** to the **server** when making an HTTP request.
They provide metadata about the request such as:

* What kind of content is acceptable (`Accept`)
* Who is making the request (`User-Agent`)
* Authorization credentials (`Authorization`)
* Language preferences, cache settings, and more

---

### 🔹 Why are Headers Important?

They help the server:

* Understand how to **respond properly**
* **Authenticate** the client
* Deliver **customized responses** (e.g. language, format)
* Enforce **security and caching** rules

---

### 🔹 Commonly Used Headers

| Header          | Purpose                                              |
| --------------- | ---------------------------------------------------- |
| `User-Agent`    | Identifies the client (browser/app/tool)             |
| `Accept`        | Specifies accepted response format (e.g. JSON, HTML) |
| `Authorization` | Sends login/auth token                               |
| `Content-Type`  | Specifies the type of data being sent (e.g. JSON)    |
| `Host`          | Specifies the domain name of the server              |
| `Referer`       | Indicates the origin of the request                  |

---

### 🔹 Example in Python using `requests`

```python
import requests

url = "https://httpbin.org/headers"

headers = {
    "User-Agent": "MyApp/1.0",
    "Accept": "application/json",
    "X-Custom-Header": "TestValue"
}

response = requests.get(url, headers=headers)

print(response.json())
```

🧪 `https://httpbin.org/headers` simply returns the headers you sent — great for testing.

---

### 🔹 Custom Headers

You can define your own headers using the `"X-"` prefix:

```python
headers = {
    "X-App-Mode": "dark",
    "X-User-ID": "12345"
}
```

---

### 📌 Notes

* Some headers (like `Host` or `Content-Length`) are automatically added by libraries like `requests`.
* Improper headers can lead to **403 Forbidden** or **401 Unauthorized** errors.

---

### ✅ Use Cases

* API access with tokens
* Mimicking browser behavior
* Sending JSON/XML data
* Managing session and authentication

---