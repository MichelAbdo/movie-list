import requests
from requests.exceptions import HTTPError
from requests.models import Response


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
        @return: Response
        @rtype: Response
        """
        try:
            response: Response = requests.request(
                method,
                url,
                params=query_params,
                json=body)
            response.raise_for_status()
            return response
        except HTTPError as http_err:
            return http_err.response
        except Exception as err:
            return err.response
