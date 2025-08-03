from zarinpal_utils.Config import Config
from zarinpal import ZarinPal



def initiate_payment():
    try:
        config = Config(
            merchant_id= "YOUR_MERCHANT_ID",  
            sandbox=True,  
        )
        zarinpal = ZarinPal(config)
        response = zarinpal.payments.create({
            "amount": 20000, 
            "callback_url": "https://zarinpal.com/", 
            "description": "Payment creat", 
            "mobile": "09123456789",  
            "email": "customer@example.com",  
            "cardPan": "6219861034529007", 
            "referrer_id": "affiliate123", 
        })

        print("Payment created successfully:", response)
        
        if "data" in response and "authority" in response["data"]:
            authority = response["data"]["authority"]
            payment_url = zarinpal.payments.generate_payment_url(authority)
            print("Payment URL:", payment_url)
        else:
            print("Authority not found in response.")


    except Exception as e:
        print("Error during payment creation:", e)

if __name__ == "__main__":
    initiate_payment()