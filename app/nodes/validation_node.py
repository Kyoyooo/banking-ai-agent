from app.core.schemas import ValidationResult

class ValidationNode:
    def process(self, draft: str, policy: str) -> ValidationResult:
        # 1. Quá ngắn?
        if len(draft.split()) < 10:
            return ValidationResult(is_valid=False, feedback="Câu trả lời quá ngắn, có thể chưa giải quyết đủ vấn đề.")
        
        # 2. Bị lỗi của AI?
        ai_error_phrases = ["as an ai", "system error", "i cannot assist", "i'm just a language model"]
        if any(phrase in draft.lower() for phrase in ai_error_phrases):
            return ValidationResult(is_valid=False, feedback="Phát hiện văn phong từ chối của AI model.")
        
        return ValidationResult(is_valid=True, feedback="Câu trả lời đạt chuẩn chất lượng.")