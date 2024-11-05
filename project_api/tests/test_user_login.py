import allure
from base_api.base_check import BaseChecks
from project_api.data.test_data import HTTP_OK, HTTP_ACCEPTED, HTTP_UNAUTHORIZED


@allure.feature('API')
@allure.story('StellarBurgers')
@allure.epic('Customer login')
@allure.parent_suite('Positive tests')
@allure.suite('POST /auth/login')
@allure.title('Check login for new customer with valid credentials')
def test_login_user_with_right_creds(customer_api):
    with allure.step('Generating and creating a random customer'):
        customer_api.create_customer()

    with allure.step('Customer login'):
        response_json, status_code = customer_api.login()

    with allure.step('Expected Results'):
        with allure.step('Assert status code is 200'):
            BaseChecks.check_status(status_code, HTTP_OK)

        with allure.step('Assert field "success" is True'):
            BaseChecks.check_success(response_json)

    with allure.step('Deleting the user'):
        response_json, status_code = customer_api.delete()

    with allure.step('Expected Results'):
        with allure.step('Assert status code is 202'):
            BaseChecks.check_status(status_code, HTTP_ACCEPTED)

        with allure.step('Assert field "success" is True'):
            BaseChecks.check_message(response_json, 'User successfully removed')


@allure.feature('API')
@allure.story('StellarBurgers')
@allure.epic('Customer login')
@allure.parent_suite('Negative tests')
@allure.suite('POST /auth/login')
@allure.title('Check login for customer with invalid credentials')
def test_login_with_wrong_creds(customer_api):
    with allure.step('Generating and creating a random customer'):
        response_json, status_code = customer_api.create_customer()

    with allure.step('Retrieving credentials from the customer'):
        email = response_json.get("user", {}).get("email")
        password = response_json.get("user", {}).get("password")

    with allure.step('Deleting the user'):
        customer_api.delete()

    with allure.step('Customer login with deleted credentials'):
        response_json, status_code = customer_api.login(email=email, password=password)

    with allure.step('Expected Results'):
        with allure.step('Assert response code is 401'):
            BaseChecks.check_status(status_code, HTTP_UNAUTHORIZED)

        with allure.step('Assert message indicates incorrect email or password'):
            BaseChecks.check_message(response_json, 'email or password are incorrect')
