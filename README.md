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
- **Intent Detection Node**: Sử dụng mô hình **Llama-3-8B** đã fine-tune trên tập dữ liệu **[BANKING77](https://huggingface.co/datasets/PolyAI/banking77)** để nhận diện chính xác 77 ý định của khách hàng.
- **Priority Assessment Node**: Phân loại yêu cầu theo 3 mức (Low, Medium, High) dựa trên ý định và từ khóa.
- **Policy Retrieval Node**: Tra cứu chính sách nghiệp vụ tương ứng từ cơ sở dữ liệu giả lập (Knowledge Base).
- **Response Drafting Node**: Gọi mô hình **gpt-oss:20b** thông qua **Ollama** để soạn thảo phản hồi chuyên nghiệp.
- **Validation Node**: Kiểm duyệt câu trả lời nháp để đảm bảo không có lỗi AI (hallucination), không quá ngắn và không bỏ sót thông tin placeholder.
- **Routing Node**: Ra quyết định cuối cùng hoặc là tự động trả lời luôn với khách hàng hoặc là chuyển tiếp cho nhân viên hỗ trợ (Human Agent) trong các trường hợp khẩn cấp hoặc câu trả lời không đạt chuẩn.
### 2. Mô hình AI & Hạ tầng
- **Mô hình nhận diện ý định**:  `tazuneru/llama-3-8b-banking-intent`(https://huggingface.co/tazuneru/llama-3-8b-banking-intent) (Fine-tuned Llama-3-8B)
- **Mô hình sinh văn bản**: **gpt-oss:20b** chạy trên nền tảng **Ollama**.
- **Backend**: FastAPI (Python).
- **Kết nối: Sử dụng Pinggy để tạo đường hầm (Tunnel) kết nối máy Local với GPU trên Google Colab.

## Cấu trúc thư mục
```text
banking-intent-unsloth
|-- scripts
|   |-- train.py            # Huấn luyện với thuật toán Masked Loss
|   |-- inference.py        # Suy luận với bộ lọc Regex và chuẩn hóa đầu ra
|   |-- preprocess_data.py  # Stratified Sampling đảm bảo cân bằng 77 nhãn
|   |-- evaluate.py         # Đánh giá Accuracy và xuất báo cáo chi tiết
|-- configs
|   |-- train.yaml          # Cấu hình LoRA (r=16, alpha=32) và Hyperparameters
|   |-- inference.yaml      # Cấu hình đường dẫn model checkpoint
|-- sample_data
|   |-- train.csv           # 1540 mẫu huấn luyện (20 mẫu/nhãn)
|   |-- test.csv            # 385 mẫu kiểm thử (5 mẫu/nhãn)
|-- train.sh                # Bash script thực thi quy trình train
|-- inference.sh            # Bash script thực thi quy trình test mẫu
|-- requirements.txt        # Danh sách thư viện tương thích
|-- README.md               # Hướng dẫn chi tiết
```

## Thông số mô hình & Huấn luyện 
| Tham số | Giá trị |
|:------:|:--------:|
| Base Model | Unsloth Llama-3-8B-Instruct (4-bit) | 
| LoRA Rank (r) | 16 | 
| LoRA Alpha | 32 | 
| Learning Rate | 2e-4 | 
| Epochs | 5 | 
| Optimizer | AdamW 8-bit | 
| Batch Size | 4 (Gradient Accumulation: 4) | 

## Hướng dẫn cài đặt
**1. Clone repository:**
```bash
git clone [https://github.com/Kyoyooo/fine-tuning-intent-detection-model-with-banking-dataset.git](https://github.com/Kyoyooo/fine-tuning-intent-detection-model-with-banking-dataset.git)
cd fine-tuning-intent-detection-model-with-banking-dataset
```

**2. Cài đặt thư viện:**
```bash
pip install -r requirements.txt
```

## Hướng dẫn sử dụng
**1. Tiền xử lý dữ liệu**

Sử dụng kỹ thuật **Stratified Sampling** để trích xuất dữ liệu cân bằng từ **BANKING77**:
```bash
python scripts/preprocess_data.py
```
**2. Huấn luyện mô hình**

Chạy fine-tuning với **Unsloth**:
```bash
bash train.sh
```
**3. Suy luận (Inference)**

Kiểm tra mô hình với các message đầu vào:
```bash
bash inference.sh
```

**4. Đánh giá**
   
Chạy đánh giá trên toàn bộ tập test để xem Accuracy:
```bash
python scripts/evaluate.py
``` 

## Kết quả thử nghiệm
- **Độ chính xác (Accuracy): 88.05%**
- Nhận xét: Mô hình nhận diện chính xác các ý định khó và có sự tương đồng cao (như các vấn đề về thẻ hoặc phí giao dịch) nhờ vào việc ép định dạng đầu ra nghiêm ngặt.

## Video Demonstration   
Xem video hướng dẫn thực hiện và kết quả chạy script tại: https://drive.google.com/file/d/1nkCMTnh1gJyKRUSy-IhQYfQKEBEflATO/view?usp=sharing
