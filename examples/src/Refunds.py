from zarinpal_utils.Config import Config
from zarinpal import ZarinPal

def process_refund():
    try:
        config = Config(
            access_token= "Your_Token",
        )
        zarinpal = ZarinPal(config)

        refund_response = zarinpal.refunds.create({
            "session_id": "Your_Session_Id",
            "amount": 0, #Amount
            "description": "Refund for order #1234",
            "method": "PAYA",
            "reason": "CUSTOMER_REQUEST",
        })
        print("Refund Created:", refund_response)

  

    except Exception as e:
        print("Error processing refund:", str(e))


if __name__ == "__main__":
    process_refund()
