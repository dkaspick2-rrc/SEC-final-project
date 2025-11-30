"""Unit tests for the ChequingAccount class.
Author: Dylan Kaspick
Usage: To execute all tests in the terminal use the following command:
    python -m unittest tests/test_chequing_account.py
"""

__author__ = "Dylan Kaspick"
__version__ = "1.0.0"

import unittest
from bank_account.chequing_account import ChequingAccount
from datetime import date

class TestChequingAccount(unittest.TestCase):
    """Defines the unit tests for the ChequingAccount class."""

    def test_init_sets_attributes_to_input_values(self):
        # Arrange
        account_number = 42
        client_number = 21
        balance = 500
        date_created = date(2025, 5, 1)
        overdraft_limit = -150
        overdraft_rate = 0.08

        # Act
        chequing_account = ChequingAccount(account_number, client_number, balance, date_created,
                                           overdraft_limit, overdraft_rate)

        # Assert
        expected_account_number = 42
        expected_client_number = 21
        expected_balance = 500
        expected_date_created = date(2025, 5, 1)
        expected_overdraft_limit = -150
        expected_overdraft_rate = 0.08

        self.assertEqual(expected_account_number, chequing_account._BankAccount__account_number)
        self.assertEqual(expected_client_number, chequing_account._BankAccount__client_number)
        self.assertEqual(expected_balance, chequing_account._BankAccount__balance)
        self.assertEqual(expected_date_created, chequing_account._date_created)
        self.assertEqual(expected_overdraft_limit,
                         chequing_account._ChequingAccount__overdraft_limit)
        self.assertEqual(expected_overdraft_rate, chequing_account._ChequingAccount__overdraft_rate)

    def test_init_invalid_overdraft_limit_sets_default_value(self):
        # Arrange
        account_number = 42
        client_number = 21
        balance = 500
        date_created = date(2025, 5, 1)
        overdraft_limit = "five"
        overdraft_rate = 0.08

        # Act
        chequing_account = ChequingAccount(account_number, client_number, balance, date_created,
                                           overdraft_limit, overdraft_rate)
        
        # Assert
        expected = -100
        self.assertEqual(expected, chequing_account._ChequingAccount__overdraft_limit)

    def test_init_invalid_overdraft_rate_sets_default_value(self):
        # Arrange
        account_number = 42
        client_number = 21
        balance = 500
        date_created = date(2025, 5, 1)
        overdraft_limit = -150
        overdraft_rate = "five"

        # Act
        chequing_account = ChequingAccount(account_number, client_number, balance, date_created,
                                           overdraft_limit, overdraft_rate)
        
        # Assert
        expected = 0.05
        self.assertEqual(expected, chequing_account._ChequingAccount__overdraft_rate)

    def test_init_invalid_date_created_sets_default_value(self):
        # Arrange
        account_number = 42
        client_number = 21
        balance = 500
        date_created = "May 05"
        overdraft_limit = -150
        overdraft_rate = 0.08

        # Act
        chequing_account = ChequingAccount(account_number, client_number, balance, date_created,
                                           overdraft_limit, overdraft_rate)
        
        # Assert
        expected = date.today()
        self.assertEqual(expected, chequing_account._date_created)

    def test_get_service_charge_balance_greater_than_overdraft_limit(self):
        # Arrange
        account_number = 42
        client_number = 21
        balance = 500
        date_created = date(2025, 5, 1)
        overdraft_limit = -150
        overdraft_rate = 0.08
        chequing_account = ChequingAccount(account_number, client_number, balance, date_created,
                                           overdraft_limit, overdraft_rate)
        # Act
        actual = chequing_account.get_service_charges()

        # Assert
        expected = 0.5
        self.assertEqual(expected, actual)

    def test_get_service_charge_balance_less_than_overdraft_limit(self):
        # Arrange
        account_number = 42
        client_number = 21
        balance = -200
        date_created = date(2025, 5, 1)
        overdraft_limit = -150
        overdraft_rate = 0.08
        chequing_account = ChequingAccount(account_number, client_number, balance, date_created,
                                           overdraft_limit, overdraft_rate)
        # Act
        actual = chequing_account.get_service_charges()

        # Assert
        expected = 4.5
        self.assertEqual(expected, actual)
    
    def test_get_service_charge_balance_equal_to_overdraft_limit(self):
        # Arrange
        account_number = 42
        client_number = 21
        balance = -150
        date_created = date(2025, 5, 1)
        overdraft_limit = -150
        overdraft_rate = 0.08
        chequing_account = ChequingAccount(account_number, client_number, balance, date_created,
                                           overdraft_limit, overdraft_rate)
        # Act
        actual = chequing_account.get_service_charges()

        # Assert
        expected = 0.5
        self.assertEqual(expected, actual)

    def test_str_returns_string_in_expected_format(self):
        # Arrange
        account_number = 42
        client_number = 21
        balance = 500
        date_created = date(2025, 5, 1)
        overdraft_limit = -150
        overdraft_rate = 0.08
        chequing_account = ChequingAccount(account_number, client_number, balance, date_created,
                                           overdraft_limit, overdraft_rate)
        
        # Act
        actual = chequing_account.__str__()

        # Assert
        expected = "Account Number: 42 Balance: $500.00\n" \
                    "Overdraft Limit: $-150.00 Overdraft Rate: 8.00% Account Type: Chequing"
        self.assertEqual(expected, actual)
        