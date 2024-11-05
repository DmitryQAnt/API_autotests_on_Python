import allure
from base_api.base_check import BaseChecks
from project_api.data.test_data import fields_of_created_order, HTTP_OK, order_fields_without_authorisation, \
    HTTP_SERVER_ERROR, WRONG_HASH, HTTP_BAD_REQUEST, NO_INGREDIENTS, NULL


@allure.feature('API')
@allure.story('StellarBurgers')
@allure.epic('Create new order')
@allure.parent_suite('Positive tests')
@allure.suite('POST /api/orders')
@allure.title('Check to create order with authorization')
def test_order_creation_with_right_creds(customer_api, order_api):
    with allure.step('Generating and creating a random customer'):
        customer_api.create_customer()

    with allure.step('Logging in the customer'):
        customer_api.login()

    with allure.step('Retrieving 3 ingredients from the ingredient list'):
        get_3_ingredients = order_api.get_tree_right_ingredients()

    with allure.step('Creating a valid order with 3 ingredients'):
        response_json, status_code = order_api.order_creation(ingredients=get_3_ingredients)

    with allure.step('Expected Results'):
        with allure.step('Assert status code is 200'):
            BaseChecks.check_status(status_code, HTTP_OK)

        with allure.step('Assert fields in order exist'):
            check = response_json.get("order")
            BaseChecks.check_fields_are_existing(check, fields_of_created_order)

    with allure.step('Deleting the user'):
        customer_api.delete()


@allure.feature('API')
@allure.story('StellarBurgers')
@allure.epic('Create new order')
@allure.parent_suite('Negative tests')
@allure.suite('POST /api/orders')
@allure.title('Check to create order without authorization')
def test_order_creation_no_authorisation(customer_api, order_api):
    with allure.step('Generating and creating a random customer'):
        customer_api.create_customer()

    with allure.step('Logging in the customer'):
        customer_api.login()

    with allure.step('Retrieving 3 ingredients from the ingredient list'):
        get_3_ingredients = order_api.get_tree_right_ingredients()

    with allure.step('Creating a valid order with 3 ingredients without authorization'):
        response_json, status_code = order_api.order_creation(ingredients=get_3_ingredients, auth_token=NULL)

    with allure.step('Expected Results'):
        with allure.step('Assert status code is 200'):
            BaseChecks.check_status(status_code, HTTP_OK)

        with allure.step('Assert fields in order exist without authorization'):
            check = response_json.get("order")
            BaseChecks.check_fields_are_existing(check, order_fields_without_authorisation)

    with allure.step('Deleting the user'):
        customer_api.delete()


@allure.feature('API')
@allure.story('StellarBurgers')
@allure.epic('Create new order')
@allure.parent_suite('Negative tests')
@allure.suite('POST /api/orders')
@allure.title('Check to create order without ingredients')
def test_order_creation_no_ingredients(customer_api, order_api):
    with allure.step('Generating and creating a random customer'):
        customer_api.create_customer()

    with allure.step('Logging in the customer'):
        customer_api.login()

    with allure.step('Creating an order without ingredients'):
        response_json, status_code = order_api.order_creation(ingredients=NO_INGREDIENTS)

    with allure.step('Expected Results'):
        with allure.step('Assert status code is 400'):
            BaseChecks.check_status(status_code, HTTP_BAD_REQUEST)

        with allure.step('Assert message indicates that ingredient must be provided'):
            BaseChecks.check_message(response_json, 'Ingredient ids must be provided')

    with allure.step('Deleting the user'):
        customer_api.delete()


@allure.feature('API')
@allure.story('StellarBurgers')
@allure.epic('Create new order')
@allure.parent_suite('Negative tests')
@allure.suite('POST /api/orders')
@allure.title('Check to create order with wrong ingredient hash')
def test_order_creation_wrong_ingredients(customer_api, order_api):
    with allure.step('Generating and creating a random customer'):
        customer_api.create_customer()

    with allure.step('Logging in the customer'):
        customer_api.login()

    with allure.step('Creating an order with a wrong ingredient hash'):
        response_json, status_code = order_api.order_creation(ingredients=WRONG_HASH)

    with allure.step('Expected Results'):
        with allure.step('Assert status code is 500'):
            BaseChecks.check_status(status_code, HTTP_SERVER_ERROR)

    with allure.step('Deleting the user'):
        customer_api.delete()
