import uuid
import re
from typing import Dict, Any
from app.core.schemas import AgentRequest, AgentResponse, WorkflowTrace
from app.nodes.intent_node import IntentNode
from app.nodes.priority_node import PriorityNode
from app.nodes.policy_node import PolicyNode
from app.nodes.draft_node import DraftNode
from app.nodes.validation_node import ValidationNode
from app.nodes.router_node import RouterNode

def detect_language(text: str) -> str:
    vn_chars = re.compile(r'[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ]')
    return "vi" if vn_chars.search(text.lower()) else "en"

class BankingOrchestrator:
    def __init__(self):
        print("[*] Đang khởi tạo bộ não Agent...")
        self.intent_node = IntentNode()
        self.priority_node = PriorityNode()
        self.policy_node = PolicyNode()
        self.draft_node = DraftNode()
        self.validation_node = ValidationNode()
        self.router_node = RouterNode()

    def process_request(self, request: AgentRequest) -> AgentResponse:
        request_id = str(uuid.uuid4())
        trace = WorkflowTrace()

        # 0. Nhận diện ngôn ngữ đầu vào
        lang = detect_language(request.query)

        # 1. Intent Node
        intent_res = self.intent_node.process(request.query)
        trace.intent_output = intent_res

        # 2. Priority Node
        priority_res = self.priority_node.process(request.query, intent_res.intent)
        trace.priority_output = priority_res

        # 3. Policy Node 
        policy_res = self.policy_node.process(intent_res.intent, lang)
        trace.policy_output = policy_res

        # 4. Draft Node 
        draft_res = self.draft_node.process(
            message=request.query,
            intent=intent_res.intent,
            priority=priority_res.priority,
            policy=policy_res.policy_content,
            lang=lang
        )
        trace.draft_output = draft_res

        # 5. Validation Node
        validation_res = self.validation_node.process(draft_res.draft_reply, policy_res.policy_content)
        trace.validation_output = validation_res

        # 6. Router Node
        routing_res = self.router_node.process(priority_res.priority, validation_res.is_valid)
        trace.routing_output = routing_res

        # Dịch draft reponse dựa theo ngôn ngữ
        final_text = draft_res.draft_reply
        if routing_res.decision == "escalate":
            if lang == "vi":
                final_text = "Tôi xin lỗi, yêu cầu của bạn cần được chuyên viên hỗ trợ trực tiếp xử lý. Tôi đang chuyển kết nối..."
            else:
                final_text = "I apologize, but your request requires direct assistance from our support specialists. Transferring your connection now..."

        return AgentResponse(
            request_id=request_id,
            final_response=final_text,
            decision=routing_res.decision,
            trace=trace
        )