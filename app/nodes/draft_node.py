from app.core.schemas import DraftResult
from app.clients.ollama_client import OllamaClient

class DraftNode:
    def __init__(self):
        self.llm_client = OllamaClient()

    def process(self, message: str, intent: str, priority: str, policy: str, lang: str) -> DraftResult:
        # Xác định ngôn ngữ mục tiêu
        target_lang = "Vietnamese" if lang == "vi" else "English"
        
        prompt = f"""You are a professional Banking AI Customer Support Agent.
Draft a reply to the customer based on the following context:

- Customer Message: "{message}"
- System Detected Intent: {intent}
- Case Priority: {priority}
- Official Banking Policy to follow: {policy}

Guidelines:
1. Address the customer's concern immediately and politely.
2. Incorporate the instructions from the Official Banking Policy exactly. Do not invent rules or fees.
3. IMPORTANT: You MUST write the complete response in {target_lang}. Do not mix languages.
4. Keep the response concise but highly informative.

Draft Reply (in {target_lang}):"""
        
        draft_text = self.llm_client.generate(prompt=prompt, temperature=0.3)
        
        missing = []
        if "[Insert" in draft_text or "XXX" in draft_text:
            missing.append("Cần điền thông tin cá nhân cụ thể vào các trường có sẵn.")
            
        return DraftResult(draft_reply=draft_text.strip(), missing_info=missing)