from zarinpal import ZarinPal
from zarinpal_utils.Validator import Validator

class Reversals:
    def __init__(self, zarinpal: ZarinPal):
        """
        Initializes the Reversals instance.
        :param zarinpal: An instance of the ZarinPal class.
        """
        self.zarinpal = zarinpal
        self.endpoint = '/pg/v4/payment/reverse.json'

    def reverse(self, data: dict) -> dict:
        """
        Reverse a transaction.

        :param data: The reversal request data. Example:
                     {
                         "authority": "A12345678901234567890123456789012345"
                     }
        :return: The response from the API.
        :raises: ValueError if validation fails.
                 RuntimeError if the API call encounters an error.
        """
        # Validate input data
        if "authority" not in data:
            raise ValueError("The 'authority' field is required.")
        
        Validator.validate_authority(data["authority"])

        # Make the API request
        return self.zarinpal.request("POST", self.endpoint, data)