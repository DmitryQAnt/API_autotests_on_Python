from base_api.base_api import BaseApi


class ApiSession(BaseApi):
    """
    Class for managing API session, handling authentication and
    providing endpoints for user operations and order management.
    """

    def __init__(self, **login_data):
        super().__init__(login_data.get('base_url'))
        self.name = login_data.get('name')
        self.password = login_data.get('password')
        self.email = login_data.get('email')
        self.auth_token = None

    @property
    def token(self):
        """
        Returns the authentication token.
        """
        return self.auth_token

    @property
    def registration_url(self):
        """
        Returns the endpoint for user registration.
        """
        return '/auth/register'

    @property
    def login_url(self):
        """
        Returns the endpoint for user login.
        """
        return '/auth/login'

    @property
    def delete_url(self):
        """
        Returns the endpoint for deleting a user.
        """
        return '/auth/user'

    @property
    def order_url(self):
        """
        Returns the endpoint for order management.
        """
        return '/orders'
