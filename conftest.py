"""
File for storing all fixtures

This file includes references to the necessary pytest plugins
that provide fixtures for API tests and login tests.
"""

pytest_plugins = [
    "project_api.fixtures.api_fixtures",
    "project_api.fixtures.login_fixtures"
]
