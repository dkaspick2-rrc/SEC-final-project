"""A class to manage investment account data."""

__author__ = "Dylan Kaspick"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount
from datetime import date, timedelta
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy

class InvestmentAccount(BankAccount):
    """A class representing an investment account."""

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date,
                 management_fee: float):
        """Initializes an InvestmentAccount object with account number,
        client number, balance, date created, and management fee.
        
        Args:
            account_number (int): An int representing
            the account number.
            client_number (int): An int representing the client number.
            balance (float): A float representing the account balance.
            date_created (date): Date the account was created.
            management_fee (float): The management fee applied to the 
            investment account.

        Raises:
            ValueError: When the account number or client number are not
            an integer value.
        """

        super().__init__(account_number, client_number, balance, date_created)

        self.TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

        try:
            management_fee = float(management_fee)
        except:
            management_fee = 2.55

        self.__management_fee = management_fee
        self.__strategy = ManagementFeeStrategy(date_created, management_fee)

    def __str__(self) -> str:
        """Formats a string using the objects attributes.
        
        Returns:
            str: A formatted string that includes the objects
            attributes.
        """

        if self.TEN_YEARS_AGO.year > self._date_created.year:
           account_fee = "Waived"
        else:
            account_fee = f"${self.__management_fee:,.2f}" 

        return super().__str__() + (f"\nDate Created: {self._date_created} "
                                    f"Management Fee: {account_fee} " 
                                    f"Account Type: Investment")

    def get_service_charges(self) -> float:
        """Calculates the service charge of an account based on the
         accounts age.
          
        Returns:
            float: The calculated service charge.
        """

        return self.__strategy.calculate_service_charges(self)
    