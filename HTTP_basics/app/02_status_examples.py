from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/ok")
def ok_response():
    return {"message": "Everything is OK"}

@router.post("/created", status_code=status.HTTP_201_CREATED)
def created_response():
    return {"message": "Resource created"}

@router.get("/not-found/{item_id}")
def not_found(item_id: int):
    fake_db = {1: "Apple", 2: "Banana"}
    if item_id in fake_db:
        return {"item": fake_db[item_id]}
    return {"detail": "Item not found"}, status.HTTP_404_NOT_FOUND

@router.delete("/deleted", status_code=status.HTTP_204_NO_CONTENT)
def delete_item():
    return

@router.get("/bad-request")
def bad_request():
    """
    Returns 400 Bad Request.
    Analogy: Customer gave invalid form details at the counter.
    """
    return JSONResponse(
        content={"error": "Bad request. Your input was invalid."},
        status_code=status.HTTP_400_BAD_REQUEST
    )
@router.get("/error")
def error_response():
    return JSONResponse(
        content={"error": "Something went wrong"},
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    )
