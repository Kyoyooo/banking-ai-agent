from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Banking AI-Agent"
    
    # URL 1: Dùng cho Ollama (Sinh câu trả lời)
    OLLAMA_BASE_URL: str = "http://qfilf-35-252-238-54.run.pinggy-free.link"  
    RESPONSE_MODEL: str = "gpt-oss:20b"
    
    # URL 2: Dùng cho Llama-3 Intent (Đoán ý định)
    INTENT_API_URL: str = "http://lswyi-34-142-218-230.run.pinggy-free.link/predict_intent"
    
    HOST: str = "0.0.0.0"
    PORT: int = 8000

settings = Settings()