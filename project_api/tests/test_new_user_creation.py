import allure
import pytest
from base_api.base_check import BaseChecks
from project_api.data.test_data import HTTP_ACCEPTED, HTTP_OK, HTTP_FORBIDDEN


@allure.feature('API')
@allure.story('StellarBurgers')
@allure.epic('User Creation')
@allure.parent_suite('Positive tests')
@allure.suite('POST /api/auth/register')
@allure.title('Check to create new customer with valid data')
def test_create_user_with_right_creds(customer_api):
    with allure.step('Generating a random customer'):
        response_json, status_code = customer_api.create_customer()

    with allure.step('Expected Results'):
        with allure.step('Assert status code is 200'):
            BaseChecks.check_status(status_code, HTTP_OK)

        with allure.step('Assert field "success" is True'):
            BaseChecks.check_success(response_json)

    with allure.step('Delete user'):
        response_json, status_code = customer_api.delete()

    with allure.step('Expected Results'):
        with allure.step('Assert status code is 202'):
            BaseChecks.check_status(status_code, HTTP_ACCEPTED)

        with allure.step('Assert field "success" is True'):
            BaseChecks.check_message(response_json, 'User successfully removed')


@allure.feature('API')
@allure.story('StellarBurgers')
@allure.epic('User Creation')
@allure.parent_suite('Negative tests')
@allure.suite('POST /api/auth/register')
@allure.title('Check to create new customer without fields')
@pytest.mark.parametrize(
    'login_pass_dict',
    [('no_password_field'),
     ('no_name_field'),
     ('no_email_field')],
    indirect=['login_pass_dict']
)
def test_create_user(customer_api, login_pass_dict):
    with allure.step(f'Generating new customer with missing field: {login_pass_dict}'):
        response_json, status_code = customer_api.create_customer(
            login_pass_dict['name'],
            login_pass_dict['password'],
            login_pass_dict['email'])

    with allure.step('Expected Results'):
        with allure.step('User is not created, code 403'):
            BaseChecks.check_status(status_code, HTTP_FORBIDDEN)

        with allure.step('Assert field "message" indicates required fields'):
            BaseChecks.check_message(response_json, 'Email, password and name are required fields')


@allure.feature('API')
@allure.story('StellarBurgers')
@allure.epic('User Creation')
@allure.parent_suite('Positive tests')
@allure.suite('POST /api/auth/register')
@allure.title('Check to create a duplicate customer')
def test_create_double_user(customer_api):
    with allure.step('Generating a random customer login'):
        response_json, status_code = customer_api.create_customer()

    with allure.step('Getting credentials from the created customer'):
        email = response_json.get("user", {}).get("email")
        password = response_json.get("user", {}).get("password")

    with allure.step('Attempting to create a customer with the same credentials'):
        response_json, status_code = customer_api.create_customer(password=password, email=email)

    with allure.step('Expected Results'):
        with allure.step('User is not created, code 403'):
            BaseChecks.check_status(status_code, HTTP_FORBIDDEN)

        with allure.step('Assert field "message" indicates user already exists'):
            BaseChecks.check_message(response_json, 'User already exists')

    with allure.step('Delete user'):
        customer_api.delete()
