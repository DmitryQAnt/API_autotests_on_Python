"""Class for Basic Checks"""

import allure
from typing import Optional, Union


class BaseChecks:

    @classmethod
    def check_success(cls, response: dict):
        """
        Checks if the response contains a 'success' field and if its value is True.
        :param response: The response to be checked.
        """
        assert response.get('success', None) is not None, 'Response is missing the success message'
        assert response.get('success') == True, 'The response is not positive'

    @classmethod
    def check_message(cls, response: dict, message: str, strict: bool = True):
        """
        Verifies the response message.
        :param response: The response to be checked.
        :param message: Message to verify.
        :param strict: Strict comparison.
        """
        assert response.get('message', None) is not None, 'Response is missing the message'
        if strict:
            assert response.get('message') == message, (
                f'The message does not contain the required information. '
                f'Found: {response.get("message")} - Expected: {message}'
            )
        else:
            assert message in response.get('message'), (
                f'The message does not contain the required information. '
                f'Found: {response.get("message")} - Expected: {message}'
            )

    @classmethod
    def check_status(cls, response, expected_status: int):
        """
        Checks if the response status matches the expected value.
        :param response: The response to be checked.
        :param expected_status: Expected status code.
        """
        assert response == expected_status, f'Incorrect server response status, code = {response}'

    @classmethod
    def check_fields_are_existing(cls, response: Union[dict, list], fields: dict):
        """
        Verifies the presence of custom keys in the response and that their values are not None.
        :param response: The response to be checked.
        :param fields: Fields to verify.
        """

        # If the response is a list, take the first element
        if isinstance(response, list):
            response = response[0]

        for field, expected_value in fields.items():
            # Checks if the field exists in the response
            if field not in response:
                raise AssertionError(f"The field '{field}' is missing from the response.")

            # If a value is provided, verify its presence
            assert response[field] is not None, f"The field '{field}' should not be None."
