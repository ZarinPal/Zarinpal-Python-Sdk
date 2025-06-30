from zarinpal import ZarinPal
from utils.Config import Config

def calculate_fee():
    try:
        config = Config(
            merchant_id = ""
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