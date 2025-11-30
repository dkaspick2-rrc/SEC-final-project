"""A class defining the overdraft service charge."""

__author__ = "Dylan Kaspick"
__version__ = "1.0.0"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class OverdraftStrategy(ServiceChargeStrategy):
    """A class containing the behavior of an overdraft 
    service charge.
    """

    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """Initializes a OverdraftStrategy object with an overdraft 
        limit and overdraft rate.
        
        Args:
            overdraft_limit (float): The amount that the account is
            allowed to overdraft.
            overdraft_rate (float): The rate applied to an account that 
            is in overdraft.
        """

        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate
        
    def calculate_service_charges(self, account: BankAccount) -> float:
        """Calculates the service charge of an account based on it's
        overdraft status.
        
        Returns:
            float: The calculated service of the account.
        """

        service_charge = self.BASE_SERVICE_CHARGE

        if not account.balance >= self.__overdraft_limit:
            service_charge = (self.BASE_SERVICE_CHARGE + (self.__overdraft_limit - account.balance)
                              * self.__overdraft_rate)
             
        return service_charge
