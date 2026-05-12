from app.core.schemas import PriorityResult

class PriorityNode:
    def process(self, message: str, intent: str) -> PriorityResult:
        message_lower = message.lower()
        
        # Các từ khóa báo động đỏ [cite: 153]
        high_keywords = ['stolen', 'lost', 'fraud', 'unauthorized', 'hacked', 'swallowed', 'urgent', 'scam']
        medium_keywords = ['fail', 'error', 'wrong', 'overcharged', 'delay', 'not received']
        
        if any(kw in message_lower for kw in high_keywords) or intent in ['lost_or_stolen_card', 'card_swallowed', 'compromised_card']:
            return PriorityResult(priority="High", reason="Phát hiện từ khóa khẩn cấp hoặc ý định liên quan đến rủi ro bảo mật.")
            
        elif any(kw in message_lower for kw in medium_keywords) or 'error' in intent or 'failed' in intent:
            return PriorityResult(priority="Medium", reason="Vấn đề giao dịch cần tra soát.")
            
        return PriorityResult(priority="Low", reason="Câu hỏi tra cứu thông tin thông thường.")