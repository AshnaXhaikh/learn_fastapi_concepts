from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse

router = APIRouter()

# 📥 Reading headers 
# (like checking customer ID / extracting what client sent)
"""
`Inbound`: client-to-server instructions
- Security checks ID card    | Validate `Authorization`      | `auth: str = Header()`
"""
@router.get("/check-client")
def check_client(user_agent: str = Header()):
    """
    Technical: Extracts User-Agent header
    analogy: Bank teller verifying customer ID card
    """
    return {"client": user_agent}

# 📤 Setting custom header (like adding transaction stamps)
"""
`Outbound`: Headers are **server-to-client** metadata  
"""
@router.get("/secure-route")
def secure_route():
    """
    Technical: Addds custom security headers
    Analogy: Bank adding notary seal to documents
    """
    return JSONResponse(
        content={"status": "secure"},
        headers={"X-Aproval": "manager42"}
    )

@router.get("/auth-check")
def auth_check(auth: str = Header()):
    """
    Technical: Extracts Authorization header
    Analogy: Security checks customer's ID card
    """
    return {"authorization": auth}

