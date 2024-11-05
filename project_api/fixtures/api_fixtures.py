import pytest

from project_api.api.order.order_operations import OrderOperations
from project_api.data.test_data import URL
from project_api.api.api_session import ApiSession
from project_api.api.customer.customer_operations import UserOperations


@pytest.fixture()
def customer_api(api_session, login_data):
    """
    Fixture that creates an instance of the UserOperations class
    for working with user creation methods.

    :param api_session: The API session to be used for requests.
    :param login_data: The login data for the user.
    :return: An instance of UserOperations.
    """
    yield UserOperations(api_session, login_data)


@pytest.fixture()
def order_api(api_session):
    """
    Fixture that creates an instance of the OrderOperations class
    for working with order creation methods.

    :param api_session: The API session to be used for requests.
    :return: An instance of OrderOperations.
    """
    yield OrderOperations(api_session)


@pytest.fixture(scope="function")
def api_session(login_data):
    """
    Fixture that creates an instance of the ApiSession class
    for managing the API session during tests.

    :param login_data: The login data used to initialize the session.
    :return: An instance of ApiSession.
    """
    session = ApiSession(**login_data)

    yield session
