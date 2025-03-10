import pytest
import random
import string
from project_api.data.test_data import notvalid_login_data, URL
from project_api.data.user_data import CustomerGenerator, Customer


@pytest.fixture(scope="function")
def get_random_creds() -> dict:
    """
    Retrieves data for a new user with a random email.

    :return: A dictionary containing random user data generated by the CustomerGenerator.
    """
    return CustomerGenerator.random_customer()


@pytest.fixture(scope="function")
def login_data(get_random_creds: Customer) -> dict:
    """
    Fixture that returns unique data for testing.

    :param get_random_creds: An instance of Customer containing random user data.
    :return: A dictionary with base URL, name, password, and email for the user.
    """
    return {
        'base_url': URL.API_URL,
        'name': get_random_creds.name,
        'password': get_random_creds.password,
        'email': get_random_creds.email
    }


@pytest.fixture(scope="function")
def login_pass_dict(login_data, request):
    """
    Fixture for creating a dictionary of data for testing user creation.

    This fixture provides different sets of login data to test various scenarios.

    :param login_data: A dictionary containing user data for login.
    :param request: The request object that provides the parameter for selecting a specific login data variant.
    :return: A dictionary of login data options based on the specified request parameter.
    """
    # Creating a dictionary of possible data variants
    loginpass_options = {
        'all_valid': {
            'name': login_data['name'],
            'password': login_data['password'],
            'email': login_data['email']
        },
        'no_password_field': {
            'name': login_data['name'],
            'password': notvalid_login_data['password'],
            'email': login_data['email']
        },
        'no_name_field': {
            'name': notvalid_login_data['name'],
            'password': login_data['password'],
            'email': login_data['email']
        },
        'no_email_field': {
            'name': login_data['name'],
            'password': login_data['password'],
            'email': notvalid_login_data['email']
        }
    }
    # Returning the specified dictionary indicated by the request.param
    return loginpass_options[request.param]
