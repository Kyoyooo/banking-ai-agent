import json
import requests
import time

def run_tests():
    url = "http://localhost:8000/api/chat"
    
    # Đọc dữ liệu từ file JSON
    with open("./examples/sample_requests.json", "r", encoding="utf-8") as f:
        requests_data = json.load(f)
    
    for req in requests_data:
        print(f"\n[{req['id']}]")
        print(f"  Customer: {req['query']}")
        
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
            
            print(f"  Predicted Intent: {intent} (Expected: {req['expected_intent']})")
            print(f"  Priority: {priority} | Decision: {decision.upper()}")
            print("-" * 60)
            print(f"  Reponse:\n{data['final_response']}")
            
        except Exception as e:
            print(f"Lỗi khi xử lý: {e}")
            
        print("="*60)
        time.sleep(2) 

if __name__ == "__main__":
    run_tests()