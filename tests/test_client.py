"""Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

__author__ = "Dylan Kaspick"
__version__ = "1.0.0"

import unittest
from unittest import TestCase
from client.client import Client

class TestClient(TestCase):
    """Defines the unit tests for the Client class."""

    def test_init_sets_attributes_to_input_values(self):
        # Arrange
        client_number = 8
        first_name = "John"
        last_name = "Doe"
        email_address = "test@email.com"

        # Act
        client = Client(client_number, first_name, last_name, email_address)

        # Assert
        expected_client_number = 8
        expected_first_name = "John"
        expected_last_name = "Doe"
        expected_email_address = "test@email.com"

        self.assertEqual(expected_client_number, client._Client__client_number)
        self.assertEqual(expected_first_name, client._Client__first_name)
        self.assertEqual(expected_last_name, client._Client__last_name)
        self.assertEqual(expected_email_address, client._Client__email_address)

    def test_init_invalid_client_number_raises_value_error(self):
        # Arrange
        client_number = "NaN"
        first_name = "John"
        last_name = "Doe"
        email_address = "test@email.com"

        # Act
        with self.assertRaises(ValueError) as context:
            client = Client(client_number, first_name, last_name, email_address)
        
        # Assert
        expected = "Client ID must be of type int."
        self.assertEqual(expected, str(context.exception))

    def test_init_blank_first_name_raises_value_error(self):
        # Arrange
        client_number = 8
        first_name = "  "
        last_name = "Doe"
        email_address = "test@email.com"

        # Act
        with self.assertRaises(ValueError) as context:
            client = Client(client_number, first_name, last_name, email_address)
        
        # Assert
        expected = "First name cannot be blank."
        self.assertEqual(expected, str(context.exception))

    def test_init_blank_last_name_raises_value_error(self):
        # Arrange
        client_number = 8
        first_name = "John"
        last_name = "   "
        email_address = "test@email.com"

        # Act
        with self.assertRaises(ValueError) as context:
            client = Client(client_number, first_name, last_name, email_address)
        
        # Assert
        expected = "Last name cannot be blank."
        self.assertEqual(expected, str(context.exception))

    def test_init_invalid_email_sets_to_default_value(self):
        # Arrange
        client_number = 8
        first_name = "John"
        last_name = "Doe"
        email_address = "wrong@@email.com"

        # Act
        client = Client(client_number, first_name, last_name, email_address)
        
        # Assert
        expected_email_address = "email@pixell-river.com"
        self.assertEqual(expected_email_address, client._Client__email_address )

    def test_client_number_property_returns_client_number_attribute(self):
        # Arrange
        client_number = 8
        first_name = "John"
        last_name = "Doe"
        email_address = "test@email.com"
        client = Client(client_number, first_name, last_name, email_address)

        # Act
        actual = client.client_number

        # Assert
        expected = 8
        self.assertEqual(expected, actual)

    def test_first_name_property_returns_first_name_attribute(self):
        # Arrange
        client_number = 8
        first_name = "John"
        last_name = "Doe"
        email_address = "test@email.com"
        client = Client(client_number, first_name, last_name, email_address)

        # Act
        actual = client.first_name

        # Assert
        expected = "John"
        self.assertEqual(expected, actual)

    def test_last_name_property_returns_last_name_attribute(self):
        # Arrange
        client_number = 8
        first_name = "John"
        last_name = "Doe"
        email_address = "test@email.com"
        client = Client(client_number, first_name, last_name, email_address)

        # Act
        actual = client.last_name

        # Assert
        expected = "Doe"
        self.assertEqual(expected, actual)

    def test_email_address_property_returns_email_address_attribute(self):
        # Arrange
        client_number = 8
        first_name = "John"
        last_name = "Doe"
        email_address = "test@email.com"
        client = Client(client_number, first_name, last_name, email_address)

        # Act
        actual = client.email_address

        # Assert
        expected = "test@email.com"
        self.assertEqual(expected, actual)

    def test_str_returns_expected_format(self):
        # Arrange
        client_number = 8
        first_name = "John"
        last_name = "Doe"
        email_address = "test@email.com"
        client = Client(client_number, first_name, last_name, email_address)

        # Act
        actual = client.__str__()

        # Assert
        expected = "Doe, John [8] - test@email.com"
        self.assertEqual(expected, actual)
