import requests
from app.clients.base import BaseClient
from app.core.settings import settings

class OllamaClient(BaseClient):
    """
    Client kết nối trực tiếp với Ollama server để gọi LLM sinh response.
    """
    def __init__(self):
        self.base_url = settings.OLLAMA_BASE_URL
        self.model = settings.RESPONSE_MODEL

    def generate(self, prompt: str, **kwargs) -> str:
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,  # Nhận toàn bộ kết quả 1 lần thay vì stream từng từ
        }
        
        # Cho phép ghi đè/thêm các tham số nâng cao như temperature, max_tokens...
        payload.update(kwargs)
        
        try:
            response = requests.post(url, json=payload, timeout=120)
            response.raise_for_status()
            return response.json().get("response", "")
        except requests.exceptions.RequestException as e:
            print(f"[Ollama Error] Lỗi kết nối đến Ollama: {e}")
            return "System Error: Cannot reach the Response Generation Model."