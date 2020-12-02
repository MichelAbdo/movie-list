import requests
from requests.exceptions import HTTPError


class Helper:
    """
    Class containing helper functions
    """

    @staticmethod
    def make_request(url, method='GET',
                     query_params=None, body=None) -> list:
        """
        Make an api call to the provided URL with the sent params
        :param url: API Endpoint
        :param method: Method, default value is GET
        :param query_params: Query Params, default is None
        :param body: Request body, default is None
        :return: list
        @rtype: list
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
