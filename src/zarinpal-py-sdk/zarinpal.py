import requests
from typing import Optional
from utils.Config import Config
import logging



class ZarinPal:
    def __init__(self, config: Config):
        """
        Initializes the ZarinPal SDK.
        :param config: An instance of Config class containing merchant ID, access token, and sandbox mode.
        """
        self.config = config
        self.base_url = "https://sandbox.zarinpal.com" if self.config.sandbox else "https://payment.zarinpal.com"
        self.graphql_url = "https://next.zarinpal.com/api/v4/graphql/"

        self.http_client = requests.Session()
        self.http_client.headers.update({
            'User-Agent': 'ZarinPalSdk/v1 (Python)',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        })

        self.graphql_client = requests.Session()
        self.graphql_client.headers.update({
            'User-Agent': 'ZarinPalSdk/v1 (Python)',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.config.access_token}',
        })
        self._payments = None
        self._inquiries = None
        self._refunds = None
        self._transactions = None
        self._reversals = None
        self._unverified = None
        self._verifications = None
        self._fee = None

    @property
    def payments(self):
        if self._payments is None:
            from resources.Payments import Payments
            self._payments = Payments(self)
        return self._payments

    @property
    def inquiries(self):
        if self._inquiries is None:
            from resources.Inquiries import Inquiries
            self._inquiries = Inquiries(self)
        return self._inquiries

    @property
    def refunds(self):
        if self._refunds is None:
            from resources.Refunds import Refunds
            self._refunds = Refunds(self)
        return self._refunds

    @property
    def transactions(self):
        if self._transactions is None:
            from resources.Transactions import Transactions
            self._transactions = Transactions(self)
        return self._transactions

    @property
    def reversals(self):
        if self._reversals is None:
            from resources.Reverses import Reversals
            self._reversals = Reversals(self)
        return self._reversals

    @property
    def unverified(self):
        if self._unverified is None:
            from resources.Unverified import Unverified
            self._unverified = Unverified(self)
        return self._unverified

    @property
    def verifications(self):
        if self._verifications is None:
            from resources.Verifications import Verifications
            self._verifications = Verifications(self)
        return self._verifications
    
    @property
    def fee(self):
        if self._fee is None:
            from resources.Fee import Fee
            self._fee = Fee(self)
        return self._fee

    def request(self, method: str, endpoint: str, data: Optional[dict] = None) -> dict:
        """
        General method for making REST API requests to ZarinPal.
        :param method: HTTP method (e.g., 'GET', 'POST').
        :param endpoint: API endpoint relative to the base URL.
        :param data: Request payload as a dictionary.
        :return: Response data as a dictionary.
        """
        url = f"{self.base_url}{endpoint}"
        payload = {'merchant_id': self.config.merchant_id, **(data or {})}

        try:
            response = self.http_client.request(method=method, url=url, json=payload)
            response.raise_for_status()
            return response.json()
        
        except requests.HTTPError as http_err:
            if http_err.response is not None:
                try:
                    error_content = http_err.response.json()
                except ValueError:
                    error_content = http_err.response.text
                logging.error(f"SandBox API HTTP error: {http_err} - Response Content: {error_content}")
            else:
                logging.error(f"SandBox API HTTP error without response: {http_err}")
            raise RuntimeError(f"SandBox API request error: {http_err}") from http_err
        except requests.RequestException as req_err:
            logging.exception(f"SandBox API Request exception: {req_err}")
            raise RuntimeError(f"SandBox API request error: {req_err}") from req_err
        except Exception as e:
            logging.exception(f"Unexpected error during SandBox API request: {e}")
            raise RuntimeError(f"Unexpected error: {e}") from e

    def graphql(self, query: str, variables: Optional[dict] = None) -> dict:
        """
        General method for making GraphQL API requests to ZarinPal.
        :param query: GraphQL query string.
        :param variables: Variables for the GraphQL query as a dictionary.
        :return: Response data as a dictionary.
        """
        payload = {"query": query, "variables": variables or {}}

        try:
            response = self.graphql_client.post(self.graphql_url, json=payload)
            response.raise_for_status()
            return response.json()

        except requests.HTTPError as http_err:
            if http_err.response is not None:
                try:
                    error_content = http_err.response.json()
                except ValueError:
                    error_content = http_err.response.text
                logging.error(f"GraphQL API HTTP error: {http_err} - Response Content: {error_content}")
            else:
                logging.error(f"GraphQL API HTTP error without response: {http_err}")
            raise RuntimeError(f"GraphQL API request error: {http_err}") from http_err
        except requests.RequestException as req_err:
            logging.exception(f"GraphQL API Request exception: {req_err}")
            raise RuntimeError(f"GraphQL API request error: {req_err}") from req_err
        except Exception as e:
            logging.exception(f"Unexpected error during GraphQL API request: {e}")
            raise RuntimeError(f"Unexpected error: {e}") from e
        
        

    def get_base_url(self) -> str:
        """
        Getter for the base URL.
        :return: Base URL as a string.
        """
        return self.base_url