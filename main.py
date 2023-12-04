from fastapi import FastAPI, HTTPException, Path, Query

app = FastAPI()

# Kitoblar uchun xotiradagi ma'lumotlar bazasi
fake_books_db = [
    {"id": 1, "title": "Tiriklik tilsimi", "author": "Umar Xayyom"},
    {"id": 2, "title": "Sherlok Holms haqida hikoyalar", "author": "Artur Konan Doyl"},
    {"id": 3, "title": "Xazonrezgi", "author": "Rashod Nuri Guntekin"},
    {"id": 4, "title": "The Catcher in the Rye", "author": "J.D. Salinger"},
    {"id": 5, "title": "Pride and Prejudice", "author": "Jane Austen"},
    {"id": 6, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 7, "title": "The Lord of the Rings", "author": "J.R.R. Tolkien"},
    {"id": 8, "title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling"},
    {"id": 9, "title": "The Shining", "author": "Stephen King"},
    {"id": 10, "title": "The Da Vinci Code", "author": "Dan Brown"},
]

@app.get("/")
def read_root():
    return {"message": "Salom bro! Bu kitob API."}

@app.get("/books/", response_model=list[dict])
def read_books(skip: int = Query(0, title="O'tkazib yuboriladigan kitoblar soni"), limit: int = Query(10, title="Qabul qilinadigan kitoblar soni")):
    return fake_books_db[skip : skip + limit]

@app.get("/books/{book_id}", response_model=dict)
def read_book(book_id: int = Path(..., title="Olingan kitobning identifikatori")):
    book = next((book for book in fake_books_db if book["id"] == book_id), None)
    if book is None:
        raise HTTPException(status_code=404, detail="Kitob topilmadi")
    return book


# Bu funksiya hali tayyor emas
# @app.post("/books/", response_model=dict)
# def create_book(book: dict):
#     new_book_id = len(fake_books_db) + 1
#     new_book = {"id": new_book_id, **book}
#     fake_books_db.append(new_book)
#     return {"message": "Book created successfully", "book": new_book}
