from zarinpal_utils.Config import Config
from zarinpal import ZarinPal

def get_transactions():
    try:
        config = Config(
            access_token= "Your_Token",
        )
        zarinpal = ZarinPal(config)

        transactions = zarinpal.transactions.list({
            "terminal_id": "Your_terminal_ID",
            "filter": "PAID",  
            "limit": 10,  
            "offset": 0,
            
        })

        print("Transactions List:", transactions)
        
    except Exception as e:
        print("Error fetching transactions:", e)

if __name__ == "__main__":
    get_transactions()