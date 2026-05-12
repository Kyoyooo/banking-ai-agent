import json
import requests
import time

def run_tests():
    url = "http://localhost:8000/api/chat"
    
    # Đọc dữ liệu từ file JSON
    with open("./examples/sample_requests.json", "r", encoding="utf-8") as f:
        requests_data = json.load(f)
        
    print("="*60)
    print("🚀 BẮT ĐẦU CHẠY KIỂM THỬ BANKING AI-AGENT")
    print("="*60)
    
    for req in requests_data:
        print(f"\n[{req['id']}] Kịch bản: {req['scenario']}")
        print(f"👤 Khách hàng: {req['query']}")
        
        payload = {"query": req['query']}
        
        start_time = time.time()
        try:
            response = requests.post(url, json=payload, timeout=120)
            response.raise_for_status()
            data = response.json()
            
            trace = data.get("trace", {})
            intent = trace.get("intent_output", {}).get("intent", "N/A")
            priority = trace.get("priority_output", {}).get("priority", "N/A")
            decision = data.get("decision", "N/A")
            
            print(f"🤖 Intent đoán được: {intent} (Kỳ vọng: {req['expected_intent']})")
            print(f"🚦 Mức ưu tiên: {priority} | 🔀 Quyết định: {decision.upper()}")
            print("-" * 60)
            print(f"📝 Trả lời:\n{data['final_response']}")
            
        except Exception as e:
            print(f"❌ Lỗi khi xử lý: {e}")
            
        print("="*60)
        time.sleep(2) # Nghỉ một chút giữa các request cho mượt mà

if __name__ == "__main__":
    run_tests()