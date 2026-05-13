# Build a Banking AI-Agent

## Thông tin sinh viên
- **Họ và tên:** Võ Trần Duy Hoàng
- **MSSV:** 23120266
- **Môn học:** Ứng dụng xử lý ngôn ngữ tự nhiên trong doanh nghiệp - CSC15012
- **Giảng viên hướng dẫn:** TS. Nguyễn Hồng Bửu Long, CN. Lê Đức Khoan

## Giới thiệu đồ án
- Đồ án này tập trung vào việc xây dựng một Banking AI-Agent sử dụng kiến trúc Agentic Workflow để tự động hóa quy trình chăm sóc khách hàng trong lĩnh vực ngân hàng. Hệ thống không chỉ đơn thuần là một chatbot trả lời câu hỏi, mà hoạt động như một thực thể có khả năng suy luận, phân loại mức độ ưu tiên, tra cứu chính sách nghiệp vụ và tự động điều hướng xử lý dựa trên bối cảnh thực tế.
- Hệ thống hỗ trợ song ngữ hoàn chỉnh (Tiếng Việt và Tiếng Anh) và sử dụng kết hợp các mô hình ngôn ngữ lớn (LLM).

## Kiến trúc hệ thống
Đồ án được thiết kế theo mô hình Microservices phân tán giữa Local và Cloud (Google Colab) để tối ưu hóa tài nguyên GPU:
### 1. Luồng xử lý (6 Nodes Orchestrator)
Hệ thống vận hành thông qua bộ điều phối (Orchestrator) đi qua 6 bước xử lý chuyên biệt:
- **Intent Detection Node**: Sử dụng mô hình `Llama-3-8B` đã fine-tune trên tập dữ liệu **[BANKING77](https://huggingface.co/datasets/PolyAI/banking77)** để nhận diện chính xác 77 ý định của khách hàng.
- **Priority Assessment Node**: Phân loại yêu cầu theo 3 mức (Low, Medium, High) dựa trên ý định và từ khóa.
- **Policy Retrieval Node**: Tra cứu chính sách nghiệp vụ tương ứng từ cơ sở dữ liệu giả lập (Knowledge Base).
- **Response Drafting Node**: Gọi mô hình `gpt-oss:20b` thông qua `Ollama` để soạn thảo phản hồi chuyên nghiệp.
- **Validation Node**: Kiểm duyệt câu trả lời nháp để đảm bảo không có lỗi AI (hallucination), không quá ngắn và không bỏ sót thông tin placeholder.
- **Routing Node**: Ra quyết định cuối cùng hoặc là tự động trả lời luôn với khách hàng hoặc là chuyển tiếp cho nhân viên hỗ trợ (Human Agent) trong các trường hợp khẩn cấp hoặc câu trả lời không đạt chuẩn.
### 2. Mô hình AI & Hạ tầng
- **Mô hình nhận diện ý định**:  [`tazuneru/llama-3-8b-banking-intent`](https://huggingface.co/tazuneru/llama-3-8b-banking-intent) (Fine-tuned Llama-3-8B), chi tiết về mô hình: https://github.com/Kyoyooo/fine-tuning-intent-detection-model-with-banking-dataset
- **Mô hình sinh văn bản**: `gpt-oss:20b` chạy trên nền tảng `Ollama`.
- **Backend**: FastAPI (Python).
- **Kết nối**: Sử dụng `Pinggy` để tạo Tunnel kết nối máy Local với GPU trên Google Colab.

## Cấu trúc thư mục
```text
banking-ai-agent/
├── app/
│   ├── agent/           # Bộ điều phối (Orchestrator)
│   ├── clients/         # Các Client kết nối LLM (Base, Ollama)
│   ├── core/            # Cấu hình hệ thống (Settings, Schemas)
│   ├── data/            # Knowledge Base (Policies)
│   ├── nodes/           # 6 Nodes xử lý chính của Agent
│   └── main.py          # Khởi tạo FastAPI Server
├── examples/
│   ├── sample_requests.json  # Một vài câu hỏi kiểm thử
│   └── run_test.py           # Script chạy kiểm thử tự động
├── requirements.txt     # Danh sách thư viện cần thiết
└── run.py               # File khởi chạy ứng dụng chính
```

## Hướng dẫn cài đặt
### Bước 1: Thiết lập trên Google Colab
Vì hệ thống yêu cầu GPU để chạy LLM, bạn cần chạy 2 phiên làm việc Colab độc lập (hoặc gộp chung nếu đủ VRAM):
- **Intent API**: Chạy notebook khởi tạo Llama-3 API trên cổng `8001`.
- **Ollama API**: Chạy notebook khởi tạo Ollama trên cổng `11434`.
- Sử dụng lệnh `pinggy` trong notebook để lấy 2 đường link public (URL).
- 
### Bước 2: Cài dặt tại máy Local
**1. Clone repository:**
```bash
git clone https://github.com/Kyoyooo/banking-ai-agent.git
cd banking-ai-agent
```

**2. Cài đặt thư viện:**
```bash
pip install -r requirements.txt
```

**3. Cấu hình API:** Mở file `app/core/settings.py` và cập nhật 2 URL Pinggy thu được từ Colab vào:
- `OLLAMA_BASE_URL`
- `INTENT_API_URL`

### Bước 3: Khởi chạy và Kiểm thử
**1. Chạy Server:**
```bash
python run.py
```

**2. Chạy các test tự động:**
Mở thêm 1 terminal khác và chạy 
```bash
python examples/run_test.py
```

*Kết quả sẽ hiển thị chi tiết luồng xử lý cho từng Node từ lúc nhận câu hỏi cho đến khi ra quyết định cuối cùng.*

## Video Demonstration   
Xem video hướng dẫn thực hiện và kết quả chạy script tại: https://drive.google.com/file/d/1nkCMTnh1gJyKRUSy-IhQYfQKEBEflATO/view?usp=sharing
