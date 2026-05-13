from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Banking AI-Agent"
    
    # URL 1: Dùng cho Ollama (Sinh câu trả lời)
    OLLAMA_BASE_URL: str = "http://ysjgz-35-196-153-48.run.pinggy-free.link"  
    RESPONSE_MODEL: str = "gpt-oss:20b"
    
    # URL 2: Dùng cho Llama-3 Intent (Đoán ý định)
    INTENT_API_URL: str = "http://dosfr-136-118-33-117.run.pinggy-free.link/predict_intent"
    
    HOST: str = "0.0.0.0"
    PORT: int = 8000

settings = Settings()