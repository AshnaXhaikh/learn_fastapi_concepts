from fastapi import FastAPI, Header, HTTPException
from typing import Optional

app = FastAPI()

# 1. Read a standard header (like User-Agent)
@app.get("/read-user-agent/")
async def read_user_agent(user_agent: Optional[str] = Header(default=None)):
    return {"User-Agent": user_agent}

# 2. Read custom headers (e.g., X-Token, X-Client-ID)
@app.get("/custom-headers/")
async def read_custom_headers(
    x_token: Optional[str] = Header(default=None),
    x_client_id: Optional[str] = Header(default=None)
):
    return {
        "X-Token": x_token,
        "X-Client-ID": x_client_id
    }

# 3. Handle Authorization header for protected endpoint
@app.get("/secure/")
async def secure_endpoint(authorization: Optional[str] = Header(default=None)):
    if authorization != "Bearer mysecrettoken":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"message": "Access granted - Token Verified"}

# 4. Optional: Read multiple headers at once (combined)
@app.get("/all-headers/")
async def read_all_headers(
    user_agent: Optional[str] = Header(default=None),
    x_token: Optional[str] = Header(default=None),
    authorization: Optional[str] = Header(default=None)
):
    return {
        "User-Agent": user_agent,
        "X-Token": x_token,
        "Authorization": authorization
    }
