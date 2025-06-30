# Zarinpal Python SDK Documentation

## **Introduction**

The **Zarinpal Python SDK** provides an easy and flexible way to interact with Zarinpal’s payment gateway APIs. With features like payment initiation, transaction management, refunds, and reversals, it helps streamline integration with Zarinpal’s platform in both live and sandbox environments.

---

## **Installation**

### **Requirements**:  
- Python >= 3.12

### **Install**:

**From PyPI**:
```bash
pip install zarinpal-py-sdk
```

**From TestPyPI (for testing purposes)**:
```bash
pip install -i https://test.pypi.org/simple/ zarinpal-py-sdk
```

### **Features**:

1. **Manage Payments**:

    Easily initiate and verify payments using secure APIs.

    Example:
    ```python
    payment = zarinpal.payment_gateway.create({  
        "amount": 10000,  
        "description": "Order #1234",  
        "callback_url": "https://example.com/callback",  
    })
    ```
2. **Calculate Fee**:

    Calculate the transaction fee

    Example:
    ```python
        fee = zarinpal.fee.calculate({
            "amount": 90000,
            "currency": "IRR"
        })
        print("Fee Calculation Result:", fee)

    ```

3. **Transaction Management**:

    Fetch transaction details with filters, limits, and pagination using GraphQL.

    Example:
    ```python
    transactions = zarinpal.transactions.list({  
        "terminal_id": "YourTerminalID",  
        "filter": "PAID",  
        "limit": 10,  
        "offset": 0,  
    })
    ```

4. **Refunds & Reversals**:

    Easily process refunds or reverse a transaction with a single API call.

    Example - Refund:
    ```python
    refund = zarinpal.refunds.create({  
        "session_id": "Session1234",  
        "amount": 5000,  
        "description": "Refund for Order #1234",  
        "reason": "CUSTOMER_REQUEST",  
    })

    Example - Reversal:

    response = zarinpal.reversals.reverse({  
        "authority": "AUTHORITY_CODE",  
    })
    ```

5. **Sandbox Support**:

    Easily switch between sandbox and live environments for development and production.

## **How to Use**:

6. **Initialize SDK**:

```bash
from zarinpal import ZarinPal  
from utils.Config import Config  

config = Config(  
    access_token="YourAccessToken",  
    merchant_id="YourMerchantId"
    sandbox=True,  # Use sandbox environment  
)  
zarinpal = ZarinPal(config)  

Full Example: Fetching Transactions

from zarinpal import ZarinPal  
from utils.Config import Config  

def get_transactions():  
    try:  
        config = Config(  
            access_token="YourAccessToken",  
        )  
        zarinpal = ZarinPal(config)  

        transactions = zarinpal.transactions.list({  
            "terminal_id": "YourTerminalID",  
            "filter": "PAID",  
            "limit": 10,  
            "offset": 0,  
        })  

        print("Transactions List:", transactions)  
    except Exception as e:  
        print("Error fetching transactions:", e)  

if __name__ == "__main__":  
    get_transactions()
```
### **Contribute**:

Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

GitHub Repository: [Zarinpal Python SDK](https://github.com/ImanAttary/zarinpal_py_sdk)

By simplifying integration, this SDK ensures smooth payment workflows, enabling developers to focus on building excellent user experiences.
