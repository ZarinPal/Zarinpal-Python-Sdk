from zarinpal import ZarinPal
from zarinpal.utils.Config import Config

def get_transactions():
    try:
        config = Config(
            access_token= "Your Token",
        )
        zarinpal = ZarinPal(config)

        transactions = zarinpal.transactions.list({
            "terminal_id": "Your terminal ID",
            "filter": "PAID",  
            "limit": 10,  
            "offset": 0,
            
        })

        print("Transactions List:", transactions)
        
    except Exception as e:
        print("Error fetching transactions:", e)

if __name__ == "__main__":
    get_transactions()