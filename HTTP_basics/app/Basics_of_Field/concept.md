
# 📋 User API Field Specifications

## 🧑 User Model Fields

| Field    | Type   | Validation Rules                     | Example Value | Description                     |
|----------|--------|--------------------------------------|---------------|---------------------------------|
| `name`   | string | - Minimum 3 characters<br>- Maximum 20 characters | "Alex Morgan" | User's full name                |
| `age`    | integer| - Greater than 18<br>- Less than 100  | 25            | User's age in years             |
| `balance`| float  | - Zero or positive                   | 150.75        | Initial account balance ($)     |

---

## 🔧 Field Validation Examples

### ✅ Valid Input
```json
{
  "name": "Jamie Smith",
  "age": 30,
  "balance": 200.50
}
```

### ❌ Common Invalid Cases

1. **Short Name** (2 chars)
   ```json
   {"name": "Al", "age": 25, "balance": 100}
   ```
   Error: `"name: ensure this value has at least 3 characters"`

2. **Negative Balance**
   ```json
   {"name": "Taylor", "age": 40, "balance": -50}
   ```
   Error: `"balance: ensure this value is greater than or equal to 0"`

3. **Underage User**
   ```json
   {"name": "Casey", "age": 17, "balance": 0}
   ```
   Error: `"age: ensure this value is greater than 18"`

---

## 🛠️ API Endpoint

**`POST /create-user`**
- Accepts JSON with the exact field structure above
- Returns HTTP 422 for invalid data
- Successful response includes submitted data:

```json
{
  "message": "User created successfully",
  "user": {
    "name": "Jamie Smith",
    "age": 30,
    "balance": 200.50
  }
}
```

---

## 💡 Pro Tips
1. Use `Field(..., regex="^[A-Za-z ]+$")` to restrict names to letters/spaces
2. Add `email: str = Field(..., regex=email_regex)` for email validation
3. Include `timestamp: datetime = Field(default_factory=datetime.now)` for auto-timestamping

---
