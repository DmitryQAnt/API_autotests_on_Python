"""Class for customer operations"""
from typing import Optional, Union


class UserOperations:
    """
    Class for managing user operations such as creating, deleting,
    logging in, and updating user information.
    """

    def __init__(self, session, login_data):
        self.session = session
        self.name = login_data['name']
        self.password = login_data['password']
        self.email = login_data['email']

    def create_customer(self,
                        name: Optional[str] = None,
                        password: Optional[str] = None,
                        email: Optional[str] = None,
                        request: Optional[Union[str, dict]] = None,
                        code: Optional[int] = 200) -> dict:
        """
        Sends a request to create a customer and returns the response.
        :param name: Name for registration.
        :param password: Password for registration.
        :param email: Email for registration.
        :param request: Optional custom request.
        :param code: Expected server response code for validation, default is 200.
        :return: Server response.
        """
        name = self.name if name is None else name
        password = self.password if password is None else password
        email = self.email if email is None else email

        response = self.session.post(url=self.session.registration_url,
                                     data=request if request is not None else {
                                         "name": name,
                                         "password": password,
                                         "email": email
                                     },
                                     code=code,
                                     headers={'Authorization': None})

        if response.status_code == 200:
            self.session.auth_token = response.json().get('accessToken')

        return response.json(), response.status_code

    def delete(self,
               auth_token: Optional[str] = None,
               request: Optional[Union[str, dict]] = None,
               code: Optional[int] = 202) -> dict:
        """
        Sends a request to delete a user and returns the response.
        :param auth_token: Auth token of the authorized user.
        :param request: Optional custom request.
        :param code: Expected server response code for validation, default is 202.
        :return: Server response.
        """
        if not auth_token:
            auth_token = self.session.auth_token

        response = self.session.delete(url=self.session.delete_url,
                                       data=request if request is not None else {
                                           "token": auth_token},
                                       code=code,
                                       token=auth_token)

        return response.json(), response.status_code

    def login(self,
              email: Optional[str] = None,
              password: Optional[str] = None,
              request: Optional[Union[str, dict]] = None,
              code: Optional[int] = 200) -> dict:
        """
        Sends a request to log in and returns the response.
        :param email: Email for login.
        :param password: Password for login.
        :param request: Optional custom request.
        :param code: Expected server response code for validation, default is 200.
        :return: Server response.
        """
        if not email:
            email = self.session.email

        if not password:
            password = self.session.password

        response = self.session.post(url=self.session.login_url,
                                     data=request if request is not None else {
                                         "email": email,
                                         "password": password
                                     },
                                     code=code,
                                     headers={'Authorization': None})

        return response.json(), response.status_code

    def change_user_data(self,
                         auth_token: Optional[str] = None,
                         name: Optional[str] = None,
                         email: Optional[str] = None,
                         request: Optional[Union[str, dict]] = None,
                         code: Optional[int] = 200) -> dict:
        """
        Sends a request to update user data and returns the response.
        :param auth_token: Auth token of the authorized user.
        :param name: New name for the user.
        :param email: New email for the user.
        :param request: Optional custom request.
        :param code: Expected server response code for validation, default is 200.
        :return: Server response.
        """
        auth_token = self.session.auth_token if auth_token is None else auth_token
        email = self.email if email is None else email
        name = self.name if name is None else name

        response = self.session.patch(url=self.session.delete_url,
                                      data=request if request is not None else {
                                          "email": email,
                                          "name": name},
                                      code=code,
                                      token=auth_token
                                      )
        return response.json(), response.status_code
