from fastapi import FastAPI

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Python Basic",
        "author": "Nguyen Van A",
        "category": "programming",
        "year": 2022,
        "is_available": True
    },
    {
        "id": 2,
        "title": "Web API Design",
        "author": "Tran Van B",
        "category": "web",
        "year": 2021,
        "is_available": False
    },
    {
        "id": 3,
        "title": "Database System",
        "author": "Lê Minh Huyền",
        "category": "database",
        "year": 2020,
        "is_available": True
    },
    {
        "id": 4,
        "title": "Clean Code",
        "author": "Lê Ánh Linh",
        "category": "programming",
        "year": 2008,
        "is_available": False
    },
    {
        "id": 5,
        "title": "Computer Network",
        "author": "Vũ Hồng Vân",
        "category": "network",
        "year": 2019,
        "is_available": True
    }
]

@app.get("/health")
def check_health():
    return {"message": "Library API is running"}

@app.get("/books")
def get_all_books():
    return books

@app.get("/books/available")
def get_available_books():
    return [book for book in books if book["is_available"] is True]

@app.get("/books/borrowed")
def get_borrowed_books():
    return [book for book in books if book["is_available"] is False]

@app.get("/books/statistics")
def get_books_statistics():
    total_books = len(books)
    available_books = sum(1 for book in books if book["is_available"] is True)
    borrowed_books = sum(1 for book in books if book["is_available"] is False)
    
    return {
        "total_books": total_books,
        "available_books": available_books,
        "borrowed_books": borrowed_books
    }

@app.get("/books/categories")
def get_books_categories():
    unique_categories = list(set(book["category"] for book in books))
    return {
        "categories": unique_categories
    }


@app.get("/books/latest")
def get_latest_book():
    if not books:
        return {"message": "No books available"}
    
    latest_book = max(books, key=lambda book: book["year"])
    return latest_book  
