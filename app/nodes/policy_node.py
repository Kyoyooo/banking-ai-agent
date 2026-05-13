from app.core.schemas import PolicyResult
from app.data.policies import get_policy_by_intent

class PolicyNode:
    def process(self, intent: str, lang: str) -> PolicyResult:
        # Truyền ngôn ngữ vào hàm lấy chính sách
        policy_data = get_policy_by_intent(intent, lang)
        return PolicyResult(
            policy_content=policy_data["policy"],
            source_link=policy_data.get("link")
        )