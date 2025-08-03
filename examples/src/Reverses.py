from zarinpal_utils.Config import Config
from zarinpal import ZarinPal

def reverse_transaction():
    try:
        config = Config(
            merchant_id= "YOUR_MERCHANT_ID",
            sandbox=True, 
        )
        zarinpal = ZarinPal(config)

        response = zarinpal.reversals.reverse({
            #Enter authority:
            "authority": "",  
        })

        print("Transaction Reversed Successfully:", response)
    except Exception as e:
        print("Error during transaction reversal:", e)

if __name__ == "__main__":
    reverse_transaction()