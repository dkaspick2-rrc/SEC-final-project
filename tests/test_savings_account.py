"""Unit tests for the SavingsAccount class.
Author: Dylan Kaspick
Usage: To execute all tests in the terminal use the following command:
    python -m unittest tests/test_savings_account.py
"""

__author__ = "Dylan Kaspick"
__version__ = "1.0.0"

import unittest
from bank_account.savings_account import SavingsAccount
from datetime import date, timedelta

class TestSavingsAccount(unittest.TestCase):
    """Defines the unit tests for the SavingsAccount class."""

    def test_init_sets_attributes_to_input_values(self):
        # Arrange
        account_number = 42
        client_number = 21
        balance = 500
        date_created = date.today()
        minimum_balance = 100

        # Act
        savings_account = SavingsAccount(account_number, client_number, balance, date_created,
                                         minimum_balance)

        # Assert
        self.assertEqual(account_number, savings_account._BankAccount__account_number)
        self.assertEqual(client_number, savings_account._BankAccount__client_number)
        self.assertEqual(balance, savings_account._BankAccount__balance)
        self.assertEqual(date_created, savings_account._date_created)
        self.assertEqual(minimum_balance, savings_account._SavingsAccount__minimum_balance)
    
    def test_init_invalid_minimum_balance_sets_default_value(self):
        # Arrange
        account_number = 42
        client_number = 21
        balance = 500
        date_created = date.today()
        minimum_balance = "five"

        # Act
        savings_account = SavingsAccount(account_number, client_number, balance, date_created,
                                         minimum_balance)

        # Assert
        expected = 50
        self.assertEqual(expected, savings_account._SavingsAccount__minimum_balance)

    def test_get_service_charges_balance_greater_than_minimum(self):
        # Arrange
        account_number = 42
        client_number = 21
        balance = 500
        date_created = date.today()
        minimum_balance = 100

        savings_account = SavingsAccount(account_number, client_number, balance, date_created,
                                         minimum_balance)
        
        # Act

        actual = savings_account.get_service_charges()

        # Assert
        expected = 0.5
        self.assertEqual(expected, actual)

    def test_get_service_charges_balance_equal_to_minimum(self):
        # Arrange
        account_number = 42
        client_number = 21
        balance = 100
        date_created = date.today()
        minimum_balance = 100

        savings_account = SavingsAccount(account_number, client_number, balance, date_created,
                                         minimum_balance)
        
        # Act

        actual = savings_account.get_service_charges()

        # Assert
        expected = 0.5
        self.assertEqual(expected, actual)

    def test_get_service_charges_balance_less_than_minimum(self):
        # Arrange
        account_number = 42
        client_number = 21
        balance = 25
        date_created = date.today()
        minimum_balance = 100

        savings_account = SavingsAccount(account_number, client_number, balance, date_created,
                                         minimum_balance)
        
        # Act

        actual = savings_account.get_service_charges()

        # Assert
        expected = 1
        self.assertEqual(expected, actual)

    def test_str_returns_string_in_expected_format(self):
        # Arrange
        account_number = 42
        client_number = 21
        balance = 500
        date_created = date.today()
        minimum_balance = 100

        savings_account = SavingsAccount(account_number, client_number, balance, date_created,
                                         minimum_balance)
        
        # Act
        actual = savings_account.__str__()

        # Assert
        expected = "Account Number: 42 Balance: $500.00\n" \
                    "Minimum Balance: $100.00 Account Type: Savings"
        self.assertEqual(expected, actual)
                    