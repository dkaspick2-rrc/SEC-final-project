"""Unit tests for the InvestmentAccount class.
Author: Dylan Kaspick
Usage: To execute all tests in the terminal use the following command:
    python -m unittest tests/test_investment_account.py
"""

__author__ = "Dylan Kaspick"
__version__ = "1.0.0"

import unittest
from bank_account.investment_account import InvestmentAccount
from datetime import date, timedelta

class TestInvestmentAccount(unittest.TestCase):
    """Defines the unit tests for the InvestmentAccount class."""

    def test_init_sets_attributes_to_input_values(self):
        # Arrange
        account_number = 22
        client_number = 42
        balance = 500
        date_created = date.today()
        management_fee = 10

        # Act
        investment_account = InvestmentAccount(account_number, client_number, balance, date_created,
                                               management_fee)
        # Assert
        self.assertEqual(account_number, investment_account._BankAccount__account_number)
        self.assertEqual(client_number, investment_account._BankAccount__client_number)
        self.assertEqual(balance, investment_account._BankAccount__balance)
        self.assertEqual(date_created, investment_account._date_created)
        self.assertEqual(management_fee, investment_account._InvestmentAccount__management_fee)
    
    def test_init_invalid_management_fee_sets_default_value(self):
        # Arrange
        account_number = 22
        client_number = 42
        balance = 500
        date_created = date.today()
        management_fee = "five"

        # Act
        investment_account = InvestmentAccount(account_number, client_number, balance, date_created,
                                               management_fee)
        
        # Assert
        expected = 2.55
        self.assertEqual(expected, investment_account._InvestmentAccount__management_fee)

    def test_get_service_charges_more_than_ten_years(self):
        # Arrange
        account_number = 22
        client_number = 42
        balance = 500
        date_created = date(1990, 5, 7)
        management_fee = 10

        investment_account = InvestmentAccount(account_number, client_number, balance, date_created,
                                               management_fee)
        # Act
        actual = investment_account.get_service_charges()

        # Assert
        expected = 0.5
        self.assertEqual(expected, actual)
    
    def test_get_service_charges_exactly_ten_years(self):
        # Arrange
        account_number = 22
        client_number = 42
        balance = 500
        date_created = date.today() - timedelta(days=10 * 365.25)
        management_fee = 10

        investment_account = InvestmentAccount(account_number, client_number, balance, date_created,
                                               management_fee)
        # Act
        actual = investment_account.get_service_charges()

        # Assert
        expected = 10.5
        self.assertEqual(expected, actual)

    def test_get_service_charges_less_than_ten_years(self):
        # Arrange
        account_number = 22
        client_number = 42
        balance = 500
        date_created = date.today() - timedelta(days=5 * 365.25)
        management_fee = 10

        investment_account = InvestmentAccount(account_number, client_number, balance, date_created,
                                               management_fee)
        # Act
        actual = investment_account.get_service_charges()

        # Assert
        expected = 10.5
        self.assertEqual(expected, actual)

    def test_str_returns_string_in_expected_format_when_age_more_than_ten_years(self):
        # Arrange
        account_number = 22
        client_number = 42
        balance = 500
        date_created = date(1990, 5, 7)
        management_fee = 10

        investment_account = InvestmentAccount(account_number, client_number, balance, date_created,
                                               management_fee)
        
        # Act
        actual = investment_account.__str__()

        # Assert
        expected = "Account Number: 22 Balance: $500.00\n" \
                    "Date Created: 1990-05-07 Management Fee: Waived Account Type: Investment"
        self.assertEqual(expected, actual)

    def test_str_returns_string_in_expected_format_when_age_less_than_ten_years(self):
        # Arrange
        account_number = 22
        client_number = 42
        balance = 500
        date_created = date.today()
        management_fee = 10

        investment_account = InvestmentAccount(account_number, client_number, balance, date_created,
                                               management_fee)
        
        # Act
        actual = investment_account.__str__()

        # Assert
        expected = "Account Number: 22 Balance: $500.00\n" \
                    f"Date Created: {date.today()} Management Fee: $10.00 Account Type: Investment"
        self.assertEqual(expected, actual)
        