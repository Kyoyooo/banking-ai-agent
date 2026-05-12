from pydantic import BaseModel
from typing import List, Optional, Dict, Any

# Các Schema cho từng Node (Giữ nguyên như đã thiết kế)
class IntentResult(BaseModel):
    intent: str
    confidence: float

class PriorityResult(BaseModel):
    priority: str 
    reason: str

class PolicyResult(BaseModel):
    policy_content: str

class DraftResult(BaseModel):
    draft_reply: str

class ValidationResult(BaseModel):
    is_valid: bool
    feedback: Optional[str] = None

class RoutingResult(BaseModel):
    decision: str 
    target: str

# Schema cho toàn bộ luồng xử lý (Workflow Trace)
class WorkflowTrace(BaseModel):
    intent_output: Optional[IntentResult] = None
    priority_output: Optional[PriorityResult] = None
    policy_output: Optional[PolicyResult] = None
    draft_output: Optional[DraftResult] = None
    validation_output: Optional[ValidationResult] = None
    routing_output: Optional[RoutingResult] = None

class AgentRequest(BaseModel):
    query: str

class AgentResponse(BaseModel):
    final_response: str
    decision: str
    trace: WorkflowTrace # Hiển thị chi tiết từng bước cho thầy xem [cite: 192]