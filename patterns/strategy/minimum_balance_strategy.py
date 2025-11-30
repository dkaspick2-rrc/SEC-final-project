"""A class defining the minimum balance service charge."""

__author__ = "Dylan Kaspick"
__version__ = "1.0.0"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """A class containing the behavior of a minimum balance 
    service charge.
    """

    def __init__(self, minimum_balance: float):
        """Initializes a MinimumBalanceStrategy object with a 
        minimum balance.
        
        Args:
            minimum_balance (float): The minimum balance an account must
            have to apply further service charges.
        """

        self.SERVICE_CHARGE_PREMIUM = 2.0
        self.__minimum_balance = minimum_balance

    def calculate_service_charges(self, account: BankAccount) -> float:
        """Calculates the service charge of an account based on if the
        accounts balance is above the accounts minimum balance.
        
        Returns:
            float: The calculated service charge.
        """

        service_charge = self.BASE_SERVICE_CHARGE

        if not account.balance >= self.__minimum_balance:
            service_charge = self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM

        return service_charge
    