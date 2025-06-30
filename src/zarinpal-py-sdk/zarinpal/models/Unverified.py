from zarinpal.service import ZarinPal

class Unverified:
    def __init__(self, zarinpal: ZarinPal):
        """
        Initializes the Unverified instance.
        :param zarinpal: An instance of the ZarinPal class.
        """
        self.zarinpal = zarinpal
        self.endpoint = '/pg/v4/payment/unVerified.json'

    def list(self) -> dict:
        """
        Retrieve a list of unverified payments.

        :return: A dictionary containing the list of unverified payments.
        :raises: RuntimeError if the API call encounters an error.
        """
        # Make the API request
        return self.zarinpal.request('POST', self.endpoint, {})