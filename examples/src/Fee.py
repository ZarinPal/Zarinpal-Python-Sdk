from zarinpal_utils.Config import Config
from zarinpal import ZarinPal

def calculate_fee():
    try:
        config = Config(
            merchant_id = "YOUR_MERCHANT_ID"
        )
        zarinpal = ZarinPal(config)

        fee = zarinpal.fee.calculate({
            "amount": 90000,
            "currency": "IRR"
        })

        print("Fee Calculation Result:", fee)

    except Exception as e:
        print("Error calculating fee:", e)

if __name__ == "__main__":
    calculate_fee()