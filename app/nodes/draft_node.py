from app.core.schemas import DraftResult
from app.clients.ollama_client import OllamaClient

class DraftNode:
    def __init__(self):
        self.llm_client = OllamaClient()

    def process(self, message: str, intent: str, priority: str, policy: str) -> DraftResult:
        prompt = f"""You are a professional and empathetic Banking AI Customer Support Agent.
Draft a reply to the customer based on the following context:

- Customer Message: "{message}"
- System Detected Intent: {intent}
- Case Priority: {priority}
- Official Banking Policy to follow: {policy}

Guidelines:
1. Be polite and address the customer's concern immediately.
2. Incorporate the instructions from the Official Banking Policy exactly. Do not invent rules or fees.
3. If the priority is High, express empathy and urgency.
4. Keep the response concise but highly informative.
5. Answer in the same language as the customer message.

Draft Reply:"""
        
        # Gọi Ollama sinh text
        draft_text = self.llm_client.generate(prompt=prompt, temperature=0.3)
        
        # Kiểm tra xem có chỗ nào bị trống thông tin cần điền tay không
        missing = []
        if "[Insert" in draft_text or "XXX" in draft_text:
            missing.append("Cần điền thông tin cá nhân cụ thể vào các trường có sẵn.")
            
        return DraftResult(draft_reply=draft_text.strip(), missing_info=missing)