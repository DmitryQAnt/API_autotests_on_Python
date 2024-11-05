import allure

from base_api.base_check import BaseChecks
from project_api.data.test_data import HTTP_OK, fields_in_getting_order, NULL, HTTP_UNAUTHORIZED
from project_api.data.user_data import CustomerGenerator


@allure.feature('API')
@allure.story('StellarBurgers')
@allure.epic('Get order list')
@allure.parent_suite('Positive tests')
@allure.suite('GET /api/orders')
@allure.title('Check to get order of authorized client')
def test_get_orders_authorised_client(customer_api, order_api):
    with allure.step('Generating a random customer'):
        customer_api.create_customer()

    with allure.step('Customer login with credentials'):
        customer_api.login()

    with allure.step('Get 3 ingredients from the ingredient list'):
        get_3_ingredients = order_api.get_tree_right_ingredients()

    with allure.step('Create a valid order with 3 ingredients'):
        order_api.order_creation(ingredients=get_3_ingredients)

    with allure.step('Get order list with valid credentials'):
        response_json, status_code = order_api.get_user_orders()

    with allure.step('Expected Results'):
        with allure.step('Assert status code is 200'):
            BaseChecks.check_status(status_code, HTTP_OK)

        with allure.step('Assert fields in order exist'):
            check = response_json.get("orders")
            BaseChecks.check_fields_are_existing(check, fields_in_getting_order)

    with allure.step('Delete user'):
        customer_api.delete()


@allure.feature('API')
@allure.story('StellarBurgers')
@allure.epic('Get order list')
@allure.parent_suite('Negative tests')
@allure.suite('GET /api/orders')
@allure.title('Check to get order for customer without authorization')
def test_get_orders_no_authorisation(customer_api, order_api):
    with allure.step('Generating a random customer'):
        customer_api.create_customer()

    with allure.step('Customer login with credentials'):
        customer_api.login()

    with allure.step('Get 3 ingredients from the ingredient list'):
        get_3_ingredients = order_api.get_tree_right_ingredients()

    with allure.step('Create a valid order with 3 ingredients'):
        order_api.order_creation(ingredients=get_3_ingredients)

    with allure.step('Get order list without authorization'):
        response_json, status_code = order_api.get_user_orders(auth_token=NULL)

    with allure.step('Expected Results'):
        with allure.step('Assert status code is 401'):
            BaseChecks.check_status(status_code, HTTP_UNAUTHORIZED)

        with allure.step('Authorization is required'):
            BaseChecks.check_message(response_json, 'You should be authorised')

    with allure.step('Delete user'):
        customer_api.delete()
