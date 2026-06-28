from fastapi import FastAPI

app = FastAPI()

# 1. Dữ liệu mẫu đã cập nhật thêm trường is_available theo bối cảnh bài toán
books = [
    {
        "id": 1,
        "title": "Python Basic",
        "author": "Nguyen Van A",
        "category": "programming",
        "year": 2022,
        "is_available": True  # Có sẵn
    },
    {
        "id": 2,
        "title": "Web API Design",
        "author": "Tran Van B",
        "category": "web",
        "year": 2021,
        "is_available": False  # Đang được mượn
    },
    {
        "id": 3,
        "title": "Database System",
        "author": "Lê Minh Huyền",
        "category": "database",
        "year": 2020,
        "is_available": True  # Có sẵn
    },
    {
        "id": 4,
        "title": "Clean Code",
        "author": "Lê Ánh Linh",
        "category": "programming",
        "year": 2008,
        "is_available": False  # Đang được mượn
    },
    {
        "id": 5,
        "title": "Computer Network",
        "author": "Vũ Hồng Vân",
        "category": "network",
        "year": 2019,
        "is_available": True  # Có sẵn
    }
]

# --- Các API từ bài trước ---
@app.get("/health")
def check_health():
    return {"message": "Library API is running"}

@app.get("/books")
def get_all_books():
    return books


# --- BÀI THỰC HÀNH 2: XỬ LÝ THEO TRẠNG THÁI ---

# API 1: Lấy danh sách sách còn có thể mượn (is_available == True)
@app.get("/books/available")
def get_available_books():
    # Sử dụng Vòng lặp (Cách 1) hoặc List Comprehension (Cách 2) để lọc dữ liệu
    result = []
    for book in books:
        if book["is_available"] is True:
            result.append(book)
    return result


# API 2: Lấy danh sách sách đang được mượn (is_available == False)
@app.get("/books/borrowed")
def get_borrowed_books():
    # Sử dụng List Comprehension (Cách 2) cho code ngắn gọn, rõ ràng
    result = [book for book in books if book["is_available"] is False]
    return result