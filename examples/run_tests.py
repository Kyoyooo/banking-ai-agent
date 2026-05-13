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
        print("-" * 60)
        
        payload = {"query": req['query']}
        
        start_time = time.time()
        try:
            response = requests.post(url, json=payload, timeout=120)
            response.raise_for_status()
            data = response.json()
            
            # Trích xuất toàn bộ dữ liệu từ các Node
            trace = data.get("trace", {})
            intent_out = trace.get("intent_output", {})
            priority_out = trace.get("priority_output", {})
            policy_out = trace.get("policy_output", {})
            draft_out = trace.get("draft_output", {})
            val_out = trace.get("validation_output", {})
            route_out = trace.get("routing_output", {})
            
            # 1. Intent Node
            print(f"   1. INTENT NODE")
            print(f"   - Predicted Intent: {intent_out.get('intent', 'N/A')} (Expected: {req.get('expected_intent', 'N/A')})")
            print(f"   - Confidence: {intent_out.get('confidence', 'N/A')}")
            
            # 2. Priority Node
            print(f"   2. PRIORITY NODE")
            print(f"   - Priority Level: {priority_out.get('priority', 'N/A')}")
            print(f"   - Reason: {priority_out.get('reason', 'N/A')}")
            
            # 3. Policy Node
            print(f"   3. POLICY NODE")
            print(f"   - Extracted Policy: {policy_out.get('policy_content', 'N/A')}")
            
            # 4. Draft Node
            print(f"   4. DRAFT NODE")
            print(f"   - Draft Reply: {draft_out.get('draft_reply', 'N/A')}")
            
            # 5. Validation Node
            print(f"   5. VALIDATION NODE")
            print(f"   - Is Valid: {val_out.get('is_valid', 'N/A')}")
            print(f"   - Feedback: {val_out.get('feedback', 'N/A')}")
            
            # 6. Routing Node
            print(f"   6. ROUTING NODE")
            print(f"   - Decision: {route_out.get('decision', 'N/A')}")
            print(f"   - Target: {route_out.get('target', 'N/A')}")
            
            print("-" * 60)
            print(f"   FINAL RESPONSE:\n{data.get('final_response', 'N/A')}")
            
        except Exception as e:
            print(f"Lỗi khi xử lý: {e}")
            
        print("="*60)
        time.sleep(2) 

if __name__ == "__main__":
    run_tests()