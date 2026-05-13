from app.core.schemas import ValidationResult

class ValidationNode:
    def process(self, draft: str, policy: str, lang: str = "vi") -> ValidationResult:
        draft_lower = draft.lower()
        
        # 1. Quá ngắn? (Bị lỗi sinh text)
        if len(draft.split()) < 10:
            feedback = "Câu trả lời quá ngắn, có thể chưa giải quyết đủ vấn đề." if lang == "vi" else "The response is too short and may not adequately resolve the issue."
            return ValidationResult(is_valid=False, feedback=feedback)
        
        # 2. Bị lỗi văn phong của AI? (AI Hallucination/Refusal)
        ai_error_phrases = [
            "as an ai", "system error", "i cannot assist", "i'm just a language model",
            "với tư cách là một ai", "tôi không thể hỗ trợ", "tôi chỉ là một mô hình", "lỗi hệ thống"
        ]
        if any(phrase in draft_lower for phrase in ai_error_phrases):
            feedback = "Phát hiện văn phong từ chối của AI model." if lang == "vi" else "Detected AI model refusal or hallucination language."
            return ValidationResult(is_valid=False, feedback=feedback)
            
        # 3. Quên điền thông tin (Unfilled placeholders)
        placeholders = ["[", "]", "xxx", "insert"]
        if any(p in draft_lower for p in placeholders):
            feedback = "Câu trả lời chứa thông tin mẫu chưa được điền (placeholder)." if lang == "vi" else "The response contains unfilled placeholders or brackets."
            return ValidationResult(is_valid=False, feedback=feedback)
        
        # 4. Hợp lệ
        feedback = "Câu trả lời đạt chuẩn chất lượng." if lang == "vi" else "The response meets quality standards."
        return ValidationResult(is_valid=True, feedback=feedback)