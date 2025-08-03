from zarinpal import ZarinPal
from zarinpal_utils.Validator import Validator

class Transactions:
    def __init__(self, zarinpal: ZarinPal):
        """
        Initializes the Transactions instance.
        :param zarinpal: An instance of the ZarinPal class.
        """
        self.zarinpal = zarinpal

    def list(self, data: dict) -> dict:
        """
        Retrieve a list of transactions via GraphQL.

        :param data: The transaction query parameters. Example:
                     {
                         "terminal_id": "terminal_id",
                         "filter": "some-filter",
                         "limit": 10,
                         "offset": 0
                     }
        :return: A dictionary containing the list of transactions.
        :raises: ValueError if validation fails.
                 RuntimeError if the API call encounters an error.
        """
        # Validate input data
        if "terminal_id" not in data:
            raise ValueError("The 'terminal_id' field is required.")

        Validator.validate_terminal_id(data["terminal_id"])
        
        if "filter" in data:
            Validator.validate_filter(data["filter"])
        if "limit" in data:
            Validator.validate_limit(data["limit"])
        if "offset" in data:
            Validator.validate_offset(data["offset"])

        # GraphQL query and variables
        query = """
        query GetTransactions($terminal_id: ID!, $filter: FilterEnum, $limit: Int, $offset: Int) {
            Session: Session(
                terminal_id: $terminal_id,
                filter: $filter,
                limit: $limit,
                offset: $offset
            ) {
                id,
                status,
                amount,
                description,
                created_at
            }
        }
        """
        variables = {
            "terminal_id": data["terminal_id"],
            "filter": data.get("filter"),
            "limit": data.get("limit"),
            "offset": data.get("offset"),
        }

        # Make the GraphQL request
        return self.zarinpal.graphql(query, variables)