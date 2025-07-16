# app/basic_request_response.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def basic_get():
    return {"message": "This is a basic GET request response example."}
