from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()

class Account(BaseModel):
    name: str
    balance: float
    age: int

# Define the POST route to create an account
@router.post("/create-account")
def create_account(account: Account):
    """
    Accepts an Account object in JSON with name, balance, and email.
    Returns confirmation with the validated data.
    """
    return {"message": "Account created", "account": account}
