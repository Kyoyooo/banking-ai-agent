from app.core.schemas import PriorityResult

class PriorityNode:
    def __init__(self):
        self.high_intents = {
            'card_swallowed', 'compromised_card', 'lost_or_stolen_card', 
            'lost_or_stolen_phone', 'passcode_forgotten', 'pin_blocked',
            'card_payment_not_recognised', 'cash_withdrawal_not_recognised',
            'direct_debit_payment_not_recognised', 'transaction_charged_twice'
        }
        
        self.medium_intents = {
            'balance_not_updated_after_bank_transfer', 'balance_not_updated_after_cheque_or_cash_deposit',
            'cancel_transfer', 'card_not_working', 'contactless_not_working', 'declined_card_payment',
            'declined_cash_withdrawal', 'declined_transfer', 'failed_transfer', 'pending_card_payment',
            'pending_cash_withdrawal', 'pending_top_up', 'pending_transfer', 'refund_not_showing_up',
            'request_refund', 'reverted_card_payment?', 'reverted_card_payment', 'top_up_failed', 
            'top_up_reverted', 'transfer_not_received_by_recipient', 'unable_to_verify_identity',
            'verify_my_identity', 'verify_source_of_funds', 'verify_top_up', 'virtual_card_not_working',
            'wrong_amount_of_cash_received', 'wrong_exchange_rate_for_cash_withdrawal', 'card_payment_fee_charged',
            'card_payment_wrong_exchange_rate', 'cash_withdrawal_charge', 'exchange_charge',
            'extra_charge_on_statement', 'top_up_by_bank_transfer_charge', 'top_up_by_card_charge',
            'transfer_fee_charged', 'terminate_account'
        }

        self.high_keywords = [
            'stolen', 'lost', 'fraud', 'unauthorized', 'hacked', 'swallowed', 'urgent', 'scam', 'compromised', 'blocked',
            'mất', 'nuốt', 'hack', 'lừa đảo', 'khẩn cấp', 'đánh cắp', 'chiếm đoạt'
        ]
        self.medium_keywords = [
            'fail', 'error', 'wrong', 'overcharged', 'delay', 'not received', 'declined', 'pending', 'missing', 'charge',
            'lỗi', 'sai', 'chưa nhận', 'thất bại', 'chậm', 'phí', 'không thành công', 'bị trừ'
        ]

    def process(self, message: str, intent: str) -> PriorityResult:
        message_lower = message.lower()
        intent_clean = intent.strip().lower()

        if intent_clean in self.high_intents or any(kw in message_lower for kw in self.high_keywords):
            return PriorityResult(
                priority="High", 
                reason="Phát hiện ý định hoặc từ khóa liên quan đến rủi ro bảo mật, mất mát hoặc khẩn cấp."
            )
            
        elif intent_clean in self.medium_intents or any(kw in message_lower for kw in self.medium_keywords):
            return PriorityResult(
                priority="Medium", 
                reason="Phát hiện ý định hoặc từ khóa liên quan đến lỗi giao dịch, sai sót số tiền hoặc cần tra soát."
            )
            
        return PriorityResult(
            priority="Low", 
            reason="Câu hỏi tra cứu thông tin thông thường hoặc yêu cầu hướng dẫn sử dụng."
        )