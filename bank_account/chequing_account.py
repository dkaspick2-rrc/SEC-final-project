"""A class to manage chequing account data."""

__author__ = "Dylan Kaspick"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount
from datetime import date
from patterns.strategy.overdraft_strategy import OverdraftStrategy

class ChequingAccount(BankAccount):
    """A class representing a chequing account."""
    
    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, 
                 overdraft_limit : float, overdraft_rate: float): 
        """Initializes a ChequingAccount object with account number,
        client number, balance, date created, overdraft limit,
        and overdraft rate.

        Args:
            account_number (int): An int representing
            the account number.
            client_number (int): An int representing the client number.
            balance (float): A float representing the account balance.
            date_created (date): Date the account was created.
            overdraft_limit (float): The amount that the account is
            allowed to overdraft.
            overdraft_rate (float): The rate applied to an account that 
            is in overdraft.

        Raises:
            ValueError: When the account number or client number are not
            an integer value.
        """

        super().__init__(account_number, client_number, balance, date_created)

        try:
            overdraft_limit = float(overdraft_limit)
        except:
            overdraft_limit = -100

        try:
            overdraft_rate = float(overdraft_rate)
        except:
            overdraft_rate = 0.05
        
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate
        self.__strategy = OverdraftStrategy(overdraft_limit, overdraft_rate)

    def __str__(self) -> str:
        """Formats a string using the objects attributes.
        
        Returns:
            str: A formatted string that includes the objects 
            attributes.
        """

        return super().__str__() + (f"\nOverdraft Limit: ${self.__overdraft_limit:,.2f} "
                                  f"Overdraft Rate: {self.__overdraft_rate * 100:.2f}% "
                                  f"Account Type: Chequing")
    
    def get_service_charges(self) -> float:
        """Calculates the service charge of an account based on it's
        overdraft status.
        
        Returns:
            float: The calculated service of the account.
        """
    
        return self.__strategy.calculate_service_charges(self)
    