"""A class to manage savings account data."""

__author__ = "Dylan Kaspick"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount
from datetime import date, timedelta
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy

class SavingsAccount(BankAccount):
    """A class representing a SavingsAccount."""

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date,
                 minimum_balance: float):
        """Initializes a SavingsAccount object with account number,
        client number, balance, date created, and minimum balance
        
        Args:
            account_number (int): An int representing
            the account number.
            client_number (int): An int representing the client number.
            balance (float): A float representing the account balance.
            date_created (date): Date the account was created.
            minimum_balance (float): The minimum balance a savings
            account must have to apply further service charges.

        Raises:
            ValueError: When the account number or client number are not
            an integer value.
        """

        super().__init__(account_number, client_number, balance, date_created)

        try:
            minimum_balance = float(minimum_balance)
        except:
            minimum_balance = 50

        self.__minimum_balance = minimum_balance
        self.__strategy = MinimumBalanceStrategy(minimum_balance)

    def __str__(self) -> str:
        """Formats a string using the objects attributes.
        
        Returns:
            str: A formatted string that includes the objects
            attributes.
        """

        return super().__str__() + (f"\nMinimum Balance: ${self.__minimum_balance:,.2f} "
                                    f"Account Type: Savings")
    
    def get_service_charges(self) -> float:
        """Calculates the service charge of an account based on if the
        accounts balance is above the accounts minimum balance.
        
        Returns:
            float: The calculated service charge.
        """

        return self.__strategy.calculate_service_charges(self)
    