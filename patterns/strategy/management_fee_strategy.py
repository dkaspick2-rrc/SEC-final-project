"""A class defining the management fee service charge."""

__author__ = "Dylan Kaspick"
__version__ = "1.0.0"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount
from datetime import date, timedelta

class ManagementFeeStrategy(ServiceChargeStrategy):
    """A class containing the behavior of a management fee 
    service charge.
    """

    def __init__(self, date_created: date, management_fee: float):
        """Initializes a ManagementFeeStrategy object with a date 
        created and a management fee.

        Args:
            date_created (date): Date the account was created.
            management_fee (float): The management fee applied to the 
            account.
        """

        self.TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)
        
        self.__date_created = date_created
        self.__management_fee = management_fee

    def calculate_service_charges(self, account: BankAccount) -> float:
        """Calculates the service charge of an account based on the
         accounts age.
          
        Returns:
            float: The calculated service charge.
        """

        service_charge = self.BASE_SERVICE_CHARGE

        if not self.TEN_YEARS_AGO.year > self.__date_created.year:
            service_charge = self.BASE_SERVICE_CHARGE + self.__management_fee

        return service_charge
