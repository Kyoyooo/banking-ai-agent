from fastapi import FastAPI
from app.core.schemas import AgentRequest, AgentResponse
from app.agent.orchestrator import BankingOrchestrator
from app.core.settings import settings

app = FastAPI(title=settings.APP_NAME)

# Khởi tạo Orchestrator một lần duy nhất khi server bắt đầu
orchestrator = BankingOrchestrator()

@app.get("/health")
def health():
    return {"status": "Agent is online"}

@app.post("/api/chat", response_model=AgentResponse)
async def chat(request: AgentRequest):
    """
    Điểm tiếp nhận câu hỏi của khách hàng và trả về quy trình xử lý của Agent.
    """
    return orchestrator.process_request(request)