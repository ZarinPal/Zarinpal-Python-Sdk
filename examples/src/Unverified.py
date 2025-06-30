from zarinpal import ZarinPal
from zarinpal.utils.Config import Config

def get_unverified_payments():
    try:
        config = Config(
            merchant_id="Your merchant code", 
            sandbox=True,
        )
        zarinpal = ZarinPal(config)

        unverified_payments = zarinpal.unverified.list()
        print("Unverified Payments:", unverified_payments)

    except Exception as e:
        print("Error fetching unverified payments:", e)

if __name__ == "__main__":
    get_unverified_payments()