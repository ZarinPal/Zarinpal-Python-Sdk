from typing import Dict, Any
from zarinpal import ZarinPal


class Payments:
    """
    Class representing the Payments resource for creating and managing payment requests.
    """

    def __init__(self, zarinpal: ZarinPal):
        """
        Initializes the Payments class.
        :param zarinpal: An instance of the ZarinPal class.
        """
        self.zarinpal = zarinpal
        self.endpoint = '/pg/v4/payment/request.json'

    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        from zarinpal_utils.Validator import Validator

        """
        Create a new payment request.
        :param data: A dictionary containing payment details:
            - amount (int): Amount in IRR (minimum is 1,000 IRR).
            - callback_url (str): URL to redirect after payment.
            - description (str): A description of the payment.
        :return: The response from the API as a dictionary.
        :raises ValueError: If validation fails.
        :raises RuntimeError: If the API call fails.
        """
        # Validate input data
        if "amount" not in data or "callback_url" not in data:
            raise ValueError("Missing required parameters: 'amount' or 'callback_url'")
        Validator.validate_amount(data["amount"])
        Validator.validate_callback_url(data["callback_url"])

        # Make the API request
        return self.zarinpal.request("POST", self.endpoint, data)

      
    def generate_payment_url(self, authority: str) -> str:
        """
        Generate the payment URL using the authority code.
        :param authority: The authority code for the transaction.
        :return: The complete payment URL.
        """
        start_pay_url = "/pg/StartPay/"
        return f"{self.zarinpal.base_url}{start_pay_url}{authority}"