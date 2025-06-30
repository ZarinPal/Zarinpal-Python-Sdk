from zarinpal import ZarinPal
from utils.Validator import Validator

class Fee:
    def __init__(self, zarinpal: ZarinPal):
 
        self.zarinpal = zarinpal
        self.endpoint = '/pg/v4/payment/feeCalculation.json'

    def calculate(self, data: dict) -> dict:
        """
        Calculate the transaction fee.

        :param data: Fee calculation parameters. Example:
                     {
                         "merchant_id": "merchant-guid",
                         "amount": 5050543,
                         "currency": "IRR"
                     }
        :return: A dictionary containing the fee details.
        :raises: ValueError if validation fails.
                 RuntimeError if the API call encounters an error.
        """
        if "amount" not in data:
            raise ValueError("The 'amount' field is required.")
        Validator.validate_amount(data["amount"])

        if "currency" in data:
            Validator.validate_currency(data["currency"])

     # Make the API request
        return self.zarinpal.request('POST', self.endpoint, data)