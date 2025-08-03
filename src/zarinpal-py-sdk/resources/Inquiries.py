from typing import Dict, Any
from zarinpal import ZarinPal

class Inquiries:
    """
    Class representing the Inquiries resource for checking transaction status.
    """

    def __init__(self, zarinpal : ZarinPal):
        """
        Initializes the Inquiries class.
        :param zarinpal: An instance of the ZarinPal class.
        """
        self.zarinpal = zarinpal
        self.endpoint = '/pg/v4/payment/inquiry.json'

    def inquire(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Inquire about the status of a transaction.
        :param data: A dictionary containing inquiry data.
            - authority (str): The authority code of the transaction.
        :return: The response from the API as a dictionary.
        :raises ValueError: If validation fails.
        :raises RuntimeError: If the API call fails.
        """
        # Avoid circular import by importing Validator here
        from zarinpal_utils.Validator import Validator

        # Validate input data
        if "authority" not in data:
            raise ValueError("Missing required parameter: 'authority'")
        Validator.validate_authority(data["authority"])

        # Make the API request
        return self.zarinpal.request("POST", self.endpoint, data)