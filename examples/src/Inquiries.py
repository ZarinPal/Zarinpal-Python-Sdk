from zarinpal_utils.Config import Config
from zarinpal import ZarinPal

def inquire_transaction():
    try:
        config = Config(
            merchant_id= "YOUR_MERCHANT_ID",
            
            sandbox=True,  
        )
        zarinpal = ZarinPal(config)

        response = zarinpal.inquiries.inquire({
            #Enter your authority:
            "authority": ""   
        })

        print("Inquiry Result:", response)
    except Exception as e:
        print("Error during inquiry:", e)
        if hasattr(e, "response"):
            print("Error Details:", e)
        else:
            print("No additional error details available.")

if __name__ == "__main__":
    inquire_transaction()