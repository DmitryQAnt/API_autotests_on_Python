from requests import Session, Response
from base_api.snippets.logger import log_request_response


def get_headers(**kwargs) -> dict:
    """
    Возвращает заголовки для запроса
    """

    headers = kwargs.get('headers', {})
    if (token := kwargs.get('token')) is not None:
        headers.update({'Authorization': f'{token}'})

    return headers


class BaseApi(Session):
    """
    Base API class for handling HTTP requests.

    This class provides methods to make HTTP requests (GET, POST, PUT, DELETE) 
    to a specified base URL. Each method allows for optional parameters, headers, 
    and verification settings.
    """

    def __init__(self, base_url: str):
        """
        Initialize the BaseApi instance with a base URL.

        :param base_url: The base URL for the API.
        """
        super().__init__()
        self.base_url = base_url

    def post(self, **kwargs) -> Response:
        """
        Make a POST request to the specified URL.

        :param kwargs: Optional parameters for the request, including:
                       - url: The endpoint to append to the base URL.
                       - data: The JSON data to send in the request body.
                       - params: URL parameters to include in the request.
                       - headers: Custom headers for the request.
                       - verify: Whether to verify SSL certificates.
        :return: The Response object from the request.
        """
        url = self.base_url + kwargs.get('url')
        response = super().post(url=url, json=kwargs.get('data'),
                            params=kwargs.get('params'), headers=get_headers(**kwargs),
                            verify=kwargs.get('verify'))
        log_request_response(response)
        return response

    def get(self, **kwargs) -> Response:
        """
        Make a GET request to the specified URL.

        :param kwargs: Optional parameters for the request, including:
                       - url: The endpoint to append to the base URL.
                       - params: URL parameters to include in the request.
                       - headers: Custom headers for the request.
                       - verify: Whether to verify SSL certificates.
        :return: The Response object from the request.
        """
        url = self.base_url + kwargs.get('url')
        response = super().get(url=url, headers=get_headers(**kwargs),
                           params=kwargs.get('params'), verify=kwargs.get('verify'))
        log_request_response(response)
        return response


    def patch(self, **kwargs) -> Response:
        """
        Make a PATCH request to the specified URL.

        :param kwargs: Optional parameters for the request, including:
                       - url: The endpoint to append to the base URL.
                       - data: The JSON data to send in the request body.
                       - headers: Custom headers for the request.
                       - verify: Whether to verify SSL certificates.
        :return: The Response object from the request.
        """
        url = self.base_url + kwargs.get('url')
        response = super().patch(url=url, json=kwargs.get('data'),
                           headers=get_headers(**kwargs), verify=kwargs.get('verify'))
        log_request_response(response)
        return response


    def delete(self, **kwargs) -> Response:
        """
        Make a DELETE request to the specified URL.

        :param kwargs: Optional parameters for the request, including:
                       - url: The endpoint to append to the base URL.
                       - headers: Custom headers for the request.
                       - verify: Whether to verify SSL certificates.
        :return: The Response object from the request.
        """
        url = self.base_url + kwargs.get('url')
        response = super().delete(url=url, headers=get_headers(**kwargs), verify=kwargs.get('verify'))
        log_request_response(response)
        return response

