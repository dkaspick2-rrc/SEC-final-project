"""Description: Unit tests for the BankAccount class.
Author: Dylan Kaspick
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""

__author__ = "Dylan Kaspick"
__version__ = "1.0.0"

import unittest
from unittest import TestCase
from bank_account.bank_account import BankAccount

class TestBankAccount(TestCase):
    """Defines the unit tests for the BankAccount class."""

    def test_init_sets_attributes_to_input_values(self):
        # Arrange
        account_number = 22
        client_number = 8
        balance = 1000

        # Act
        bank_account = BankAccount(account_number, client_number, balance)

        # Assert
        expected_account_number = 22
        expected_client_number = 8
        expected_balance = 1000

        self.assertEqual(expected_account_number, bank_account._BankAccount__account_number)
        self.assertEqual(expected_client_number, bank_account._BankAccount__client_number)
        self.assertEqual(expected_balance, bank_account._BankAccount__balance)
    
    def test_init_balance_attribute_set_to_zero_when_arg_is_non_numeric(self):
        # Arrange
        account_number = 22
        client_number = 8
        balance = "number"

        # Act
        bank_account = BankAccount(account_number, client_number, balance)

        # Assert
        expected = 0
        self.assertEqual(expected, bank_account._BankAccount__balance)

    def test_init_non_numeric_acount_number_raises_value_error(self):
        # Arrange
        account_number = "number"
        client_number = 8
        balance = 1000

        # Act
        with self.assertRaises(ValueError) as context:
            bank_account = BankAccount(account_number, client_number, balance)
        
        # Assert
        expected = "Account number must be of type int."
        self.assertEqual(expected, str(context.exception))

    def test_init_non_numeric_client_number_raises_value_error(self):
        # Arrange
        account_number = 22
        client_number = "number"
        balance = 1000

        # Act
        with self.assertRaises(ValueError) as context:
            bank_account = BankAccount(account_number, client_number, balance)
        
        # Assert
        expected = "Client number must be of type int."
        self.assertEqual(expected, str(context.exception))

    def test_account_number_property_returns_account_number_attribute(self):
        # Arrange
        account_number = 22
        client_number = 8
        balance = 1000
        bank_account = BankAccount(account_number, client_number, balance)

        # Act
        actual = bank_account.account_number

        # Assert
        expected = 22
        self.assertEqual(expected, actual)

    def test_client_number_property_returns_client_number_attribute(self):
        # Arrange
        account_number = 22
        client_number = 8
        balance = 1000
        bank_account = BankAccount(account_number, client_number, balance)

        # Act
        actual = bank_account.client_number

        # Assert
        expected = 8
        self.assertEqual(expected, actual)
  
    def test_balance_property_returns_balance_attribute(self):
        # Arrange
        account_number = 22
        client_number = 8
        balance = 1000
        bank_account = BankAccount(account_number, client_number, balance)

        # Act
        actual = bank_account.balance

        # Assert
        expected = 1000
        self.assertEqual(expected, actual)   

    def test_update_balance_updates_balance_given_positive_argument(self):
        # Arrange
        account_number = 22
        client_number = 8
        balance = 1000
        bank_account = BankAccount(account_number, client_number, balance)

        # Act
        bank_account.update_balance(200)

        # Assert
        expected = 1200
        self.assertEqual(expected, bank_account.balance)

    def test_update_balance_updates_balance_given_negative_argument(self):
        # Arrange
        account_number = 22
        client_number = 8
        balance = 1000
        bank_account = BankAccount(account_number, client_number, balance)

        # Act
        bank_account.update_balance(-200)

        # Assert
        expected = 800
        self.assertEqual(expected, bank_account.balance)

    def test_update_balance_attribute_unchanged_given_non_numeric_argument(self):
        # Arrange
        account_number = 22
        client_number = 8
        balance = 1000
        bank_account = BankAccount(account_number, client_number, balance)

        # Act
        bank_account.update_balance("number")

        # Assert
        expected = 1000
        self.assertEqual(expected, bank_account.balance)

    def test_deposit_balance_updated_correctly_given_valid_input(self):
        # Arrange
        account_number = 22
        client_number = 8
        balance = 1000
        bank_account = BankAccount(account_number, client_number, balance)

        # Act
        bank_account.deposit(200)

        # Assert
        expected = 1200
        self.assertEqual(expected, bank_account.balance)

    def test_deposit_negative_amount_raises_value_error(self):
        # Arrange
        account_number = 22
        client_number = 8
        balance = 1000
        bank_account = BankAccount(account_number, client_number, balance)

        # Act
        with self.assertRaises(ValueError) as context:
            bank_account.deposit(-200)

        # Assert
        expected = "Deposit amount: $-200.00 must be positive."
        self.assertEqual(expected, str(context.exception))

    def test_withdraw_balance_updated_correctly_given_valid_input(self):
        # Arrange
        account_number = 22
        client_number = 8
        balance = 1000
        bank_account = BankAccount(account_number, client_number, balance)

        # Act
        bank_account.withdraw(200)

        # Assert
        expected = 800
        self.assertEqual(expected, bank_account.balance)

    def test_withdraw_negative_amount_raises_value_error(self):
        # Arrange
        account_number = 22
        client_number = 8
        balance = 1000
        bank_account = BankAccount(account_number, client_number, balance)

        # Act
        with self.assertRaises(ValueError) as context:
            bank_account.withdraw(-200)

        # Assert
        expected = "Withdrawal amount: $-200.00 must be positive."
        self.assertEqual(expected, str(context.exception))

    def test_withdraw_amount_exceeding_balance_raises_value_error(self):
        # Arrange
        account_number = 22
        client_number = 8
        balance = 1000
        bank_account = BankAccount(account_number, client_number, balance)

        # Act
        with self.assertRaises(ValueError) as context:
            bank_account.withdraw(2000)

        # Assert
        expected = "Withdrawal amount: $2,000.00 must not exceed the account balance: $1,000.00"
        self.assertEqual(expected, str(context.exception))

    def test_str_returns_string_in_expected_format(self):
        # Arrange
        account_number = 22
        client_number = 8
        balance = 1000
        bank_account = BankAccount(account_number, client_number, balance)

        # Act
        actual = bank_account.__str__()

        # Assert
        expected = "Account Number: 22 Balance: $1,000.00"
        self.assertEqual(expected, actual)
