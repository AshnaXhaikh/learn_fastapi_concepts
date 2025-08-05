from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Pydantic model for a Book
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

# In-memory storage (acts like a fake DB)
books_db: List[Book] = []

# 1️⃣ GET all books
@app.get("/books/", response_model=List[Book])
async def get_books():
    return books_db

# 2️⃣ GET a single book by ID
@app.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# 3️⃣ POST a new book
@app.post("/books/", response_model=Book, status_code=201)
async def create_book(book: Book):
    # Check if book with same ID already exists
    for b in books_db:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail="Book ID already exists")
    books_db.append(book)
    return book

# 4️⃣ PUT to update an existing book
@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(books_db):
        if book.id == book_id:
            books_db[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

# 5️⃣ DELETE a book
@app.delete("/books/{book_id}", status_code=204)
async def delete_book(book_id: int):
    for index, book in enumerate(books_db):
        if book.id == book_id:
            books_db.pop(index)
            return
    raise HTTPException(status_code=404, detail="Book not found")
