class URL:
    """
    Class that holds the API URL for the application.
    """
    API_URL = 'https://stellarburgers.nomoreparties.site/api'

# List of HTTP response codes for verification
HTTP_OK = 200
HTTP_ACCEPTED = 202
HTTP_BAD_REQUEST = 400
HTTP_UNAUTHORIZED = 401
HTTP_FORBIDDEN = 403
HTTP_NOT_FOUND = 404
HTTP_SERVER_ERROR = 500

# Data with empty fields
notvalid_login_data = {
    'name': '',
    'password': '',
    'email': ''
}

# Required data for order creation by an authorized user
fields_of_created_order = {
    "ingredients": '',
    "_id": "",
    "owner": '',
    "status": "",
    "name": "",
    "createdAt": "",
    "updatedAt": "",
    "number": '',
    "price": ''
}

# Fields expected when retrieving an order
fields_in_getting_order = {
    "ingredients": '',
    "_id": "",
    "status": "",
    "name": "",
    "createdAt": "",
    "updatedAt": "",
    "number": ''
}

# The only field present if the user is not authorized
order_fields_without_authorisation = {
    'number': ''
}

# Define constants for ingredients
WRONG_HASH = ['1234567890123243']
NO_INGREDIENTS = []
NULL = ''
