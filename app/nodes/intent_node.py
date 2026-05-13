"""
import re
import torch
from unsloth import FastLanguageModel
from app.core.settings import settings
from app.core.schemas import IntentResult

class IntentNode:
    def __init__(self):
        print(f"[*] Đang tải mô hình Intent từ Hugging Face: {settings.INTENT_MODEL_ID}")
        self.model, self.tokenizer = FastLanguageModel.from_pretrained(
            model_name=settings.INTENT_MODEL_ID,
            max_seq_length=512,
            load_in_4bit=True,
            device_map="auto" # Tự động đưa vào GPU
        )
        FastLanguageModel.for_inference(self.model)
        
        self.prompt_template = (
            "### Instruction:\n"
            "Classify the intent of the following banking customer message. Output ONLY the exact intent label in snake_case format.\n\n"
            "### Input:\n"
            "{message}\n\n"
            "### Response:\n"
        )

    def process(self, message: str) -> IntentResult:
        prompt = self.prompt_template.format(message=message)
        # Sử dụng GPU nếu có
        device = "cuda" if torch.cuda.is_available() else "cpu"
        inputs = self.tokenizer([prompt], return_tensors="pt").to(device)
        
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs, 
                max_new_tokens=32, 
                use_cache=True, 
                pad_token_id=self.tokenizer.eos_token_id
            )
        
        decoded = self.tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
        prediction = decoded.split("### Response:")[-1].strip()
        
        # Bộ lọc Regex bọc thép (Tương tự đồ án 2)
        label = prediction.split('\n')[0].strip().lower()
        label = re.sub(r'[^a-z0-9]', '_', label)
        label = re.sub(r'_+', '_', label).strip('_')
        
        # Vì dùng text generation, ta giả định confidence cao nếu sinh ra đúng label
        return IntentResult(intent=label, confidence=0.95)
""" 

import requests
from app.core.settings import settings
from app.core.schemas import IntentResult

class IntentNode:
    def __init__(self):
        self.api_url = settings.INTENT_API_URL
        print(f"[*] Đã kết nối Intent Node tới: {self.api_url}")

    def process(self, message: str) -> IntentResult:
        try:
            response = requests.get(self.api_url, params={"message": message}, timeout=60)
            response.raise_for_status()
            
            data = response.json()
            intent_label = data.get("intent", "unknown_intent")
            
            return IntentResult(intent=intent_label, confidence=0.95)
            
        except requests.exceptions.RequestException as e:
            print(f"[Intent Error] Lỗi kết nối đến GPU Colab: {e}")
            return IntentResult(intent="error_connection", confidence=0.0)