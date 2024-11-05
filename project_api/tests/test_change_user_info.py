import allure

from base_api.base_check import BaseChecks
from project_api.data.test_data import HTTP_OK, HTTP_UNAUTHORIZED
from project_api.data.user_data import CustomerGenerator

@allure.feature('API')
@allure.story('StellarBurgers')
@allure.epic('Change user info')
@allure.parent_suite('Positive tests')
@allure.suite('PATCH /auth/user')
@allure.title('Check to change customer with valid data')
def test_change_user_with_right_creds(customer_api, get_random_creds):
    with allure.step('Generating a random customer'):
        customer_api.create_customer()

    with allure.step('Generating the next random customer'):
        new_user_data = CustomerGenerator.random_customer()

    with allure.step('Updating information for the customer'):
        response_json, status_code = customer_api.change_user_data(email=new_user_data.email,
                                                                   name=new_user_data.name)

    with allure.step('Expected Results'):
        with allure.step('Assert status code is 200'):
            BaseChecks.check_status(status_code, HTTP_OK)

        with allure.step('Assert field "success" is True'):
            BaseChecks.check_success(response_json)

    with allure.step('Delete user'):
        customer_api.delete()


@allure.feature('API')
@allure.story('StellarBurgers')
@allure.epic('Change user info')
@allure.parent_suite('Negative tests')
@allure.suite('PATCH /auth/user')
@allure.title('Check to change customer without authorization')
def test_change_user_no_authorisation(customer_api):
    with allure.step('Generating a random customer'):
        customer_api.create_customer()

    with allure.step('Generating the next random customer'):
        new_user_data = CustomerGenerator.random_customer()

    with allure.step('Updating information for the customer without Bearer token'):
        response_json, status_code = customer_api.change_user_data(email=new_user_data.email,
                                                                   name=new_user_data.name, auth_token='')

    with allure.step('Expected Results'):
        with allure.step('User update should fail, expected code 401'):
            BaseChecks.check_status(status_code, HTTP_UNAUTHORIZED)

        with allure.step('Check authorization is required'):
            BaseChecks.check_message(response_json, 'You should be authorised')

    with allure.step('Delete user'):
        customer_api.delete()
