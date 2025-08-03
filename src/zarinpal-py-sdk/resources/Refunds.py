from zarinpal import ZarinPal
from zarinpal_utils.Validator import Validator

class Refunds:
    def __init__(self, zarinpal: ZarinPal):

        self.zarinpal = zarinpal

    def create(self, data: dict) -> dict:

        Validator.validate_session_id(data["session_id"])
        Validator.validate_amount(data["amount"])
        if "method" in data:
            Validator.validate_method(data["method"])
        if "reason" in data:
            Validator.validate_reason(data["reason"])

        query = """
            mutation AddRefund($session_id: ID!, $amount: BigInteger!, $description: String, $method: InstantPayoutActionTypeEnum, $reason: RefundReasonEnum){
                resource: AddRefund(
                    session_id: $session_id,
                    amount: $amount,
                    description: $description,
                    method: $method,
                    reason: $reason
                ) {
                    terminal_id,
                    id,
                    amount,
                    timeline {
                        refund_amount,
                        refund_time,
                        refund_status
                    }
                }
            }
        """
        variables = {
            "session_id": data["session_id"],
            "amount": data["amount"],
            "description": data.get("description"),
            "method": data.get("method"),
            "reason": data.get("reason"),
        }

        return self.zarinpal.graphql(query, variables)

