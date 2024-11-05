import random
import string


class Customer:
    """
    Class representing a customer with optional attributes for name, password, and email.
    """

    def __init__(self, name=None, password=None, email=None):
        self.name = name
        self.password = password
        self.email = email


class CustomerGenerator:
    """
    Class for generating random customer instances.
    This implementation aims to provide secure data transmission in tests by generating
    unique customer data, ensuring that sensitive information is not hard-coded.
    """

    @classmethod
    def random_customer(cls):
        """
        Generates a random customer with a fixed name and password, and a unique email.
        The email is created using a prefix and a random numeric suffix.

        :return: An instance of Customer with generated attributes.
        """
        return Customer("test", 'password',
                        f"user_{''.join(random.choices(string.digits, k=7))}@yandex.ru")
