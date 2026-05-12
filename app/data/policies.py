# Dummy database lưu trữ các chính sách và FAQ của ngân hàng
BANKING_POLICIES = {
    "card_swallowed": {
        "policy": "Nếu thẻ của bạn bị nuốt tại ATM, vui lòng ngay lập tức khóa thẻ trên ứng dụng (Mục 'Cards' > 'Freeze'). Sau đó, mang theo CMND/CCCD đến chi nhánh gần nhất để yêu cầu cấp lại thẻ miễn phí. Không bao giờ cung cấp mã PIN cho bất kỳ ai.",
        "link": "https://dummybank.com/support/card-swallowed"
    },
    "lost_or_stolen_card": {
        "policy": "Đối với thẻ bị mất hoặc bị đánh cắp, khách hàng phải khóa thẻ khẩn cấp trên App. Thẻ thay thế sẽ được phát hành với mức phí $5 và gửi đến địa chỉ đăng ký trong vòng 3-5 ngày làm việc.",
        "link": "https://dummybank.com/support/lost-card"
    },
    "transfer_not_received_by_recipient": {
        "policy": "Giao dịch chuyển khoản nội địa có thể mất tối đa 24 giờ. Chuyển khoản quốc tế mất 3-5 ngày làm việc. Nếu quá thời gian này, vui lòng kiểm tra lại thông tin người nhận. Ngân hàng hỗ trợ tra soát giao dịch với mức phí $15.",
        "link": "https://dummybank.com/support/transfer-delay"
    },
    "apple_pay_or_google_pay": {
        "policy": "Bạn có thể thêm thẻ vật lý hoặc thẻ ảo vào Apple Pay / Google Pay trực tiếp từ App ngân hàng. Vào mục 'Cards', chọn thẻ và nhấn 'Add to Apple Wallet' hoặc 'Add to GPay'. Đảm bảo thiết bị của bạn có hỗ trợ NFC.",
        "link": "https://dummybank.com/support/digital-wallets"
    },
    "verify_source_of_funds": {
        "policy": "Theo quy định phòng chống rửa tiền, ngân hàng có thể yêu cầu chứng minh nguồn gốc đối với các giao dịch lớn bất thường. Khách hàng cần chuẩn bị Hợp đồng, Bảng lương hoặc Chứng từ liên quan và tải lên qua App.",
        "link": "https://dummybank.com/support/compliance"
    },
    "default": {
        "policy": "Thời gian xử lý các yêu cầu thông thường là 1-2 ngày làm việc. Vui lòng đảm bảo thông tin tài khoản của bạn luôn được cập nhật chính xác.",
        "link": "https://dummybank.com/support/general"
    }
}

def get_policy_by_intent(intent: str) -> dict:
    """
    Hàm truy xuất Policy dựa vào intent lấy được từ Llama-3.
    Nếu intent không có trong dữ liệu, trả về chính sách mặc định.
    """
    intent = intent.strip().lower()
    return BANKING_POLICIES.get(intent, BANKING_POLICIES["default"])