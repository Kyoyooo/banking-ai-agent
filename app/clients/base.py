from abc import ABC, abstractmethod

class BaseClient(ABC):
    """
    Interface cơ sở cho mọi LLM Client.
    Đảm bảo tính nhất quán khi gọi mô hình trong toàn bộ hệ thống.
    """
    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        pass