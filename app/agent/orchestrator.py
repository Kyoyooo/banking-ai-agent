import uuid
from typing import Dict, Any
from app.core.schemas import AgentRequest, AgentResponse, WorkflowTrace
from app.nodes.intent_node import IntentNode
from app.nodes.priority_node import PriorityNode
from app.nodes.policy_node import PolicyNode
from app.nodes.draft_node import DraftNode
from app.nodes.validation_node import ValidationNode
from app.nodes.router_node import RouterNode

class BankingOrchestrator:
    def __init__(self):
        # Khởi tạo tất cả các Node xử lý
        print("[*] Đang khởi tạo bộ não Agent...")
        self.intent_node = IntentNode()
        self.priority_node = PriorityNode()
        self.policy_node = PolicyNode()
        self.draft_node = DraftNode()
        self.validation_node = ValidationNode()
        self.router_node = RouterNode()

    def process_request(self, request: AgentRequest) -> AgentResponse:
        """
        Thực thi quy trình Agentic Workflow tuần tự.
        """
        request_id = str(uuid.uuid4())
        trace = WorkflowTrace()

        # Bước 1: Nhận diện ý định (Intent Detection) [cite: 182]
        intent_res = self.intent_node.process(request.query)
        trace.intent_output = intent_res

        # Bước 2: Đánh giá mức độ ưu tiên (Priority Assessment) [cite: 183]
        priority_res = self.priority_node.process(request.query, intent_res.intent)
        trace.priority_output = priority_res

        # Bước 3: Tra cứu chính sách (Policy Retrieval) [cite: 188]
        policy_res = self.policy_node.process(intent_res.intent)
        trace.policy_output = policy_res

        # Bước 4: Soạn thảo câu trả lời nháp (Response Drafting) [cite: 189]
        draft_res = self.draft_node.process(
            message=request.query,
            intent=intent_res.intent,
            priority=priority_res.priority,
            policy=policy_res.policy_content
        )
        trace.draft_output = draft_res

        # Bước 5: Kiểm duyệt (Validation) [cite: 190]
        validation_res = self.validation_node.process(draft_res.draft_reply, policy_res.policy_content)
        trace.validation_output = validation_res

        # Bước 6: Điều hướng quyết định (Routing) [cite: 191]
        routing_res = self.router_node.process(priority_res.priority, validation_res.is_valid)
        trace.routing_output = routing_res

        # Xác định phản hồi cuối cùng dựa trên quyết định điều hướng
        final_text = draft_res.draft_reply
        if routing_res.decision == "escalate":
            final_text = "Tôi xin lỗi, yêu cầu của bạn cần được chuyên viên hỗ trợ trực tiếp xử lý. Tôi đang chuyển kết nối..."

        return AgentResponse(
            request_id=request_id,
            final_response=final_text,
            decision=routing_res.decision,
            trace=trace
        )