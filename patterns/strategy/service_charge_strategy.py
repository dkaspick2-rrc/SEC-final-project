"""A class defining a service charge strategy interface."""

__author__ = "Dylan Kaspick"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from bank_account.bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    """An abstract class defining the behavior of a service charge 
    strategy.
    """

    BASE_SERVICE_CHARGE = 0.5
    """The base service charge applied to bank accounts."""

    @abstractmethod
    def calculate_service_charges(self, account: BankAccount) -> float:
        """Calculates the service charges that will be applied to this
        bank account.

        Returns:
            float: The calculated service charge.
        """

        pass
