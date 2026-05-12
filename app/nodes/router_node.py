from app.core.schemas import RoutingResult

class RouterNode:
    def process(self, priority: str, is_valid: bool) -> RoutingResult:
        if not is_valid:
            # Nếu draft bị lỗi, đẩy ngay cho người thật xử lý
            return RoutingResult(decision="escalate", target="human_agent")
        
        if priority == "High":
            # Giao dịch mức ưu tiên cao (mất tiền, mất thẻ) -> Vẫn gửi reply hướng dẫn khẩn cấp nhưng báo con người theo dõi
            return RoutingResult(decision="send_reply_and_escalate", target="customer_and_human")
        
        # Trường hợp bình thường (Low/Medium) -> Tự động hóa hoàn toàn
        return RoutingResult(decision="send_reply", target="customer")