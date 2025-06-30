from zarinpal import ZarinPal
from zarinpal.utils.Config import Config



authority = "Your Authority"    
status = "OK"


def get_amount_from_database(authority):
    return 20000

def verify_payment(authority, status):
    if status == "OK":
        amount = get_amount_from_database(authority)

        if amount:
            try:
                config = Config(
                    merchant_id= "Your merchant code", 
                    sandbox=True, 
                )
                zarinpal = ZarinPal(config)    
                response = zarinpal.verifications.verify({
                    "amount": amount,
                    "authority": authority,
                })

                if response["data"]["code"] == 100:
                    print("Payment Verified:")
                    print("Reference ID:", response["data"]["ref_id"])
                    print("Card PAN:", response["data"]["card_pan"])
                    print("Fee:", response["data"]["fee"])
                elif response["data"]["code"] == 101:
                    print("Payment already verified.")
                else:
                    print("Transaction failed with code:", response["data"]["code"])

            except Exception as e:
                print("Payment Verification Failed:", e)
        else:
            print("No Matching Transaction Found For This Authority Code.")
    else:
        print("Transaction was cancelled or failed.")

if __name__ == "__main__":
    verify_payment(authority, status)