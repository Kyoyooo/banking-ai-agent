import uvicorn
from app.core.settings import settings

if __name__ == "__main__":
    # Chạy FastAPI server với cấu hình từ settings
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=False # Tắt reload khi load model nặng để tránh lỗi bộ nhớ
    )