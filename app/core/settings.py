"""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Banking AI-Agent"
    
    # Cấu hình Ollama (Dùng để sinh câu trả lời nháp - Response Generation)
    OLLAMA_BASE_URL: str = "http://localhost:11434" 
    RESPONSE_MODEL: str = "gpt-oss-20b"
    
    # Cấu hình Hugging Face Model (Dùng cho Intent Detection - Đồ án 2)
    # Sau này Node Intent sẽ dùng ID này để tự động tải về
    INTENT_MODEL_ID: str = "tazuneru/llama-3-8b-banking-intent"
    
    # API Config
    HOST: str = "0.0.0.0"
    PORT: int = 8000

settings = Settings()
"""

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Banking AI-Agent"
    
    # URL 1: Dùng cho Ollama (Sinh câu trả lời)
    OLLAMA_BASE_URL: str = "http://xcmcw-8-228-13-113.run.pinggy-free.link" 
    RESPONSE_MODEL: str = "gpt-oss:20b"
    
    # URL 2: Dùng cho Llama-3 Intent (Đoán ý định)
    INTENT_API_URL: str = "http://ywwqs-8-228-13-113.run.pinggy-free.link/predict_intent"
    
    HOST: str = "0.0.0.0"
    PORT: int = 8000

settings = Settings()