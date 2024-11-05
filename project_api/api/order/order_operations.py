"""Class for order operations"""
from typing import Optional, Union


class OrderOperations:
    """
    Class for managing order operations such as creating orders and
    retrieving user orders.
    """

    def __init__(self, session):
        self.session = session

    def order_creation(self,
                       auth_token: Optional[str] = None,
                       ingredients: Optional[list] = None,
                       request: Optional[Union[str, dict]] = None) -> tuple:
        """
        Sends a request to create an order and returns the response and status code.
        :param auth_token: Authorization token.
        :param ingredients: List of ingredients for the order.
        :param request: Optional custom request.
        :return: Tuple (Server response in JSON format, status code).
        """

        ingredients = self.ingredients if ingredients is None else ingredients

        auth_token = self.session.auth_token if auth_token is None else auth_token

        try:
            response = self.session.post(url=self.session.order_url,
                                         data=request if request is not None else {
                                             "ingredients": ingredients
                                         },
                                         token=auth_token
                                         )
            response_json = response.json()
        except Exception as e:
            response_json = {"error": str(e)}
            response_code = 500
        else:
            response_code = response.status_code

        return response_json, response_code

    def get_user_orders(self,
                        auth_token: Optional[str] = None,
                        code: Optional[int] = 200) -> dict:
        """
        Sends a request to retrieve user orders and returns the response.
        :param auth_token: Authorization token.
        :param code: Expected server response code for validation, default is 200.
        :return: Server response.
        """

        auth_token = self.session.auth_token if auth_token is None else auth_token

        response = self.session.get(url=self.session.order_url,
                                    code=code,
                                    token=auth_token
                                    )

        return response.json(), response.status_code

    def get_tree_right_ingredients(self) -> list:
        """
        Retrieves the IDs of the first three ingredients from the ingredients list.
        :return: List of ingredient IDs.
        """

        ingredients = self.session.get(url='/ingredients').json()
        ids = [item['_id'] for item in ingredients['data']][0:3]
        return ids
