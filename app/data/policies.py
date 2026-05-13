# Cơ sở dữ liệu Knowledge Base cho Policies
BANKING_POLICIES = {
    # SECURITY & EMERGENCY
    "card_swallowed": {
        "vi": "Nếu thẻ bị nuốt tại ATM, vui lòng ngay lập tức khóa thẻ trên ứng dụng (Mục 'Cards' > 'Freeze'). Sau đó, mang theo CMND/CCCD đến chi nhánh gần nhất để yêu cầu cấp lại thẻ miễn phí.",
        "en": "If your card is swallowed at an ATM, please immediately freeze your card on the app ('Cards' > 'Freeze'). Then, bring your ID to the nearest branch to request a free replacement.",
        "link": "https://dummybank.com/support/card-swallowed"
    },
    "lost_or_stolen_card": {
        "vi": "Để đảm bảo an toàn, bạn phải khóa thẻ khẩn cấp trên App. Thẻ thay thế sẽ được phát hành với mức phí $5 và gửi đến địa chỉ đăng ký trong vòng 3-5 ngày làm việc.",
        "en": "For your safety, you must urgently freeze the card on the App. A replacement card will be issued for a $5 fee and sent to your registered address within 3-5 business days.",
        "link": "https://dummybank.com/support/lost-card"
    },
    "compromised_card": {
        "vi": "Nếu nghi ngờ thẻ bị lộ thông tin hoặc có giao dịch lạ, hãy khóa thẻ ngay trên App và báo cáo giao dịch gian lận. Ngân hàng sẽ hủy thẻ cũ và phát hành thẻ mới hoàn toàn miễn phí.",
        "en": "If you suspect your card details are compromised, freeze the card immediately and report fraudulent transactions. We will cancel it and issue a new one for free.",
        "link": "https://dummybank.com/support/compromised"
    },
    "pin_blocked": {
        "vi": "Mã PIN/Mật khẩu sẽ bị khóa sau 3 lần nhập sai. Bạn có thể mở khóa và đặt lại mã mới trực tiếp trong mục 'Security' hoặc 'PIN Settings' trên ứng dụng.",
        "en": "Your PIN/Passcode is blocked after 3 incorrect attempts. You can unblock and reset a new one directly in the 'Security' or 'PIN Settings' section on the app.",
        "link": "https://dummybank.com/support/pin-blocked"
    },

    # TRANSFERS & TOP-UPS
    "transfer_not_received": {
        "vi": "Chuyển khoản nội địa mất tối đa 24 giờ, quốc tế mất 3-5 ngày làm việc. Nếu quá thời gian này người nhận chưa có tiền, vui lòng cung cấp biên lai để chúng tôi hỗ trợ tra soát.",
        "en": "Domestic transfers take up to 24 hours, international take 3-5 business days. If delayed further, please provide the receipt for tracing.",
        "link": "https://dummybank.com/support/transfer-delay"
    },
    "failed_transaction": {
        "vi": "Giao dịch thất bại hoặc bị từ chối thường do sai thông tin người nhận, thẻ chưa kích hoạt, hoặc số dư không đủ. Tiền sẽ được hoàn lại vào tài khoản của bạn trong vòng 24 giờ.",
        "en": "Failed or declined transactions are usually due to incorrect details, unactivated cards, or insufficient funds. The amount will bounce back to your account within 24 hours.",
        "link": "https://dummybank.com/support/failed-transaction"
    },

    # ACCOUNT & IDENTITY
    "verify_identity": {
        "vi": "Để xác minh danh tính hoặc nguồn tiền, vui lòng vào mục 'Profile' > 'Verification' và tải lên hình ảnh CMND/CCCD/Hộ chiếu, Hợp đồng hoặc Chứng từ liên quan rõ nét.",
        "en": "To verify your identity or source of funds, go to 'Profile' > 'Verification' and upload a clear picture of your ID/Passport, Contract, or related documents.",
        "link": "https://dummybank.com/support/verification"
    },
    "terminate_account": {
        "vi": "Để đóng tài khoản, bạn cần rút toàn bộ số dư và đảm bảo không có giao dịch đang chờ xử lý. Sau đó, chọn 'Close Account' trong phần cài đặt Profile.",
        "en": "To close your account, withdraw all funds and ensure no pending transactions. Then, select 'Close Account' in your Profile settings.",
        "link": "https://dummybank.com/support/close-account"
    },

    # CARD MANAGEMENT
    "activate_card": {
        "vi": "Bạn có thể kích hoạt thẻ vật lý mới bằng cách nhập mã CVV gồm 3 chữ số ở mặt sau thẻ vào mục 'Cards' > 'Activate' trên ứng dụng.",
        "en": "You can activate your new physical card by entering the 3-digit CVV from the back of the card into the 'Cards' > 'Activate' section on the app.",
        "link": "https://dummybank.com/support/activate-card"
    },
    "digital_wallet": {
        "vi": "Bạn có thể thêm thẻ vào Apple Pay hoặc Google Pay trực tiếp từ App ngân hàng tại mục 'Cards'. Đảm bảo thiết bị của bạn có hỗ trợ tính năng NFC.",
        "en": "You can add your card to Apple Pay or Google Pay directly from the banking App under the 'Cards' section. Ensure your device supports NFC.",
        "link": "https://dummybank.com/support/digital-wallets"
    },

    # REFUNDS & DISPUTES
    "refund_request": {
        "vi": "Đối với yêu cầu hoàn tiền hoặc giao dịch bị trừ đúp, khoản tiền thừa thường sẽ được hoàn lại tự động trong vòng 3-5 ngày. Nếu nhà cung cấp từ chối, bạn có thể nhấn 'Report' trên giao dịch để yêu cầu tra soát.",
        "en": "For refund requests or duplicate charges, the amount is usually auto-refunded within 3-5 days. If the merchant refuses, click 'Report' on the transaction to file a chargeback.",
        "link": "https://dummybank.com/support/refund-dispute"
    },

    # DEFAULT FALLBACK
    "default": {
        "vi": "Thời gian xử lý các yêu cầu nghiệp vụ thông thường là từ 1-2 ngày làm việc. Vui lòng đảm bảo thông tin tài khoản của bạn luôn được cập nhật chính xác.",
        "en": "Processing time for standard banking requests is 1-2 business days. Please ensure your account information is kept up to date.",
        "link": "https://dummybank.com/support/general"
    }
}

def get_policy_by_intent(intent: str, lang: str = "vi") -> dict:
    """
    Truy xuất chính sách dựa vào ý định (intent) và ngôn ngữ (lang).
    Sử dụng dictionary mapping để gom nhóm các intent tương đồng.
    """
    intent = intent.strip().lower()
    
    intent_mapping = {
        # Giao dịch thất bại
        "declined_transfer": "failed_transaction",
        "failed_transfer": "failed_transaction",
        "declined_card_payment": "failed_transaction",
        "card_not_working": "failed_transaction",
        "contactless_not_working": "failed_transaction",
        "virtual_card_not_working": "failed_transaction",
        "top_up_failed": "failed_transaction",
        
        # Chậm trễ / Chưa nhận được tiền
        "transfer_not_received_by_recipient": "transfer_not_received",
        "balance_not_updated_after_bank_transfer": "transfer_not_received",
        "balance_not_updated_after_cheque_or_cash_deposit": "transfer_not_received",
        "pending_transfer": "transfer_not_received",
        "pending_top_up": "transfer_not_received",
        
        # Mất mát / Rủi ro
        "lost_or_stolen_phone": "lost_or_stolen_card",
        "card_payment_not_recognised": "compromised_card",
        "cash_withdrawal_not_recognised": "compromised_card",
        
        # Xác minh
        "verify_my_identity": "verify_identity",
        "verify_source_of_funds": "verify_identity",
        "unable_to_verify_identity": "verify_identity",
        
        # Hoàn tiền & Lỗi đúp
        "request_refund": "refund_request",
        "refund_not_showing_up": "refund_request",
        "transaction_charged_twice": "refund_request",
        "reverted_card_payment?": "refund_request",
        
        # Khác
        "passcode_forgotten": "pin_blocked",
        "apple_pay_or_google_pay": "digital_wallet",
        "activate_my_card": "activate_card"
    }
    
    # Đối chiếu ý định được truyền vào với bộ mapping, nếu không có thì giữ nguyên tên
    mapped_intent = intent_mapping.get(intent, intent)
    
    # Lấy dữ liệu chính sách, nếu không tồn tại thì lấy mặc định
    policy_data = BANKING_POLICIES.get(mapped_intent, BANKING_POLICIES["default"])
    
    return {
        "policy": policy_data[lang],
        "link": policy_data["link"]
    }