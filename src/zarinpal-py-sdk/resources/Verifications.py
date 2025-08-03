from zarinpal import ZarinPal
from zarinpal_utils.Validator import Validator

class Verifications:
    def __init__(self, zarinpal: ZarinPal):
        """
        Initializes the Verifications instance.
        :param zarinpal: An instance of the ZarinPal class.
        """
        self.zarinpal = zarinpal
        self.endpoint = '/pg/v4/payment/verify.json'

    def verify(self, data: dict) -> dict:
        """
        Verify a payment transaction.
        
        :param data: A dictionary containing the amount and authority of the transaction.
        :return: The response from the ZarinPal API.
        :raises: ValueError if validation fails or if the API call encounters an error.
        """
        # Validate input data
        Validator.validate_amount(data['amount'])
        Validator.validate_authority(data['authority'])

        # Make the API request
        return self.zarinpal.request('POST', self.endpoint, data)