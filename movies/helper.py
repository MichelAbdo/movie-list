import requests
from requests.exceptions import HTTPError


class Helper:

    def make_request(self, url,
                     method='GET', query_params=None,
                     body=None) -> list:
        """
        @todo document all methods
        @type body: object
        """
        try:
            response = requests.request(
                method,
                url,
                params=query_params,
                json=body)
            response.raise_for_status()
            return response.json()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            return "An HTTP error occurred"
        except Exception as err:
            print(f'Other error occurred: {err}')
            return "An Error occurred"
