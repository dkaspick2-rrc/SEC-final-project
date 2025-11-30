"""Description: A class to manage bank account data."""

__author__ = "Dylan Kaspick"
__version__ = "1.2.1"

from datetime import date
from abc import ABC, abstractmethod
from patterns.observer.subject import Subject
from patterns.observer.observer import Observer

class BankAccount(Subject, ABC):
    """A class representing a bank account."""

    
    LARGE_TRANSACTION_THRESHOLD = 9999.99
    """The threshold for a single transaction to trigger a warning."""

    LOW_BALANCE_LEVEL = 50.0
    """That value at which an account balance warning will trigger."""


    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date):
        """Initializes a BankAccount object with account number,
        client number, and and account balance.

        Args:
            account_number (int): An int representing
            the account number.
            client_number (int): An int representing the client number.
            balance (float): A float representing the account balance.
            date_created (date): Date the account was created.
        
        Raises:
            ValueError: When the account number or client number are not
            an integer value.
        """

        super().__init__()

        if not isinstance(account_number, int):
            raise ValueError("Account number must be of type int.")
        
        if not isinstance(client_number, int):
            raise ValueError("Client number must be of type int.")
        
        try:
            balance = float(balance)
        except:
            balance = 0.0

        if not isinstance(date_created, date):
            date_created = date.today()

        self.__account_number = account_number
        self.__client_number = client_number
        self.__balance = balance
        self._date_created = date_created

    @property
    def account_number(self) -> int:
        """Gets the account number of the account.
        
        Returns:
            int: The accounts account number.
        """

        return self.__account_number

    @property
    def client_number(self) -> int:
        """Gets the client number of the account.
        
        Returns:
            int: The accounts client number.
        """

        return self.__client_number
    
    @property
    def balance(self) -> float:
        """Gets the balance of the account.
        
        Returns:
            float: The balance of the account.
        """

        return self.__balance
    
    def update_balance(self, amount: float) -> None:
        """Receives an amount and adds it to the current balance.
        Number can be negative or positive.
        
        Args:
            amount (float): A float defining the amount to be added.
        """
        
        try:
            amount = float(amount)
            self.__balance += amount
        except ValueError:
            self.__balance += 0

        if self.__balance < self.LOW_BALANCE_LEVEL:
            self.notify((f"Low balance warning {self.__balance}: "
                         f"on account {self.__account_number}."))
            
        if amount > self.LARGE_TRANSACTION_THRESHOLD:
            self.notify((f"Large transaction ${amount:,.2f} "
                         f"on account {self.__account_number}."))
    
    def deposit(self, amount: float) -> None:
        """Makes a deposit into the bank account with the given amount.
        
        Args:
            amount (float): The amount to be deposited.

        Raises:
            ValueError: When the amount is not a float or is
            not positive
        """

        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(f"Deposit amount: {amount} must be numeric.")      
        
        if amount < 0:
            raise ValueError(f"Deposit amount: ${amount:,.2f} must be positive.")

        self.update_balance(amount)

    def withdraw(self,amount: float) -> None:
        """Withdraw the given amount from the bank account.
        
        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: When amount is not a float, is negative, or when
            the withdraw action brings account balance bellow zero.
        """

        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(f"Withdrawal amount: {amount} must be numeric.") 
        
        if amount < 0:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} must be positive.")
        
        if self.balance - amount < 0:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} must not exceed the"
                             + f" account balance: ${self.__balance:,.2f}")
        
        self.update_balance(-amount)
    
    def __str__(self) -> str:
        """Formats a string using the objects attributes.
        
        Returns:
            str: A formatted string that includes the
            objects attributes.
        """

        formatted_string = (f"Account Number: {self.__account_number}"
                            + f" Balance: ${self.__balance:,.2f}")
        
        return formatted_string

    @abstractmethod
    def get_service_charges(self) -> float:
        """Calculates the service charges that will be applied to this
        bank account.

        Returns:
            float: The calculated service charge.
        """

        pass

    def attach(self, observer: Observer) -> None:
        """Attaches an observer to this bank account.
        
        Args:
            observer (Observer): The observer being attached.
        """

        self._observers.append(observer)

    def detach(self, observer) -> None:
        """Detaches an observer from this bank account.
        
        Args:
            observer (Observer): The observer being detached.
        """

        self._observers.remove(observer)

    def notify(self, message) -> None:
        """Notifies all observers with the given message.
        
        Args:
            message (str): The message being sent.
        """

        for observer in self._observers:
            observer.update(message)
