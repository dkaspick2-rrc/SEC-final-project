"""Description: A class to manage client data."""

__author__ = "Dylan Kaspick"
__version__ = "1.1.0"

from email_validator import validate_email, EmailNotValidError
from patterns.observer.observer import Observer
from utility import file_utils
from datetime import date

class Client(Observer):
    """A class representing a client."""

    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str):
        """Initializes a Client object with client id, first name,
        last name, and email address.

        Args:
            client_number (int): An int representing the client number.
            first_name (str): A string defining the clients first name.
            last_name (str): A string defining the clients last name.
            email_address (str): A string defining the clients email
            address.

        Raises:
            ValueError: When the client number is not an integer; When
            first name or last name are blank strings.
        """

        if not isinstance(client_number, int):
            raise ValueError("Client ID must be of type int.")
        
        if len(first_name.strip()) == 0:
            raise ValueError("First name cannot be blank.")
        
        if len(last_name.strip()) == 0:
            raise ValueError("Last name cannot be blank.")
        
        try:
            validated_email = validate_email(email_address, check_deliverability=False)
            email_address = validated_email.normalized
        except EmailNotValidError:
            email_address = "email@pixell-river.com"

        self.__client_number = client_number
        self.__first_name = first_name.strip()
        self.__last_name = last_name.strip()
        self.__email_address = email_address
    
    @property
    def client_number(self) -> int:
        """Gets the clients ID number.
        
        Returns:
            int: The clients ID number.
        """

        return self.__client_number

    @property
    def first_name(self) -> str:
        """Gets the clients first name.
        
        Returns:
            str: The clients first name.
        """

        return self.__first_name
    
    @property
    def last_name(self) -> str:
        """Gets the clients last name.
        
        Returns:
            str: The clients last name.
        """

        return self.__last_name
    
    @property
    def email_address(self) -> str:
        """Gets the clients email address.
        
        Returns:
            str: The clients email address.
        """

        return self.__email_address

    def __str__(self) -> str:
        """Formats a string using the objects attributes.
        
        Returns:
            str: A formatted string that includes the
            objects attributes.
        """

        formatted_string = (f"{self.__last_name}, {self.__first_name} [{self.__client_number}]"
                            f" - {self.__email_address}")
        
        return formatted_string

    def update(self, message: str) -> None:
        """When updated send an email with the given message.
        
        Args:
            message (str): The message to be included in the email.
        """

        subject = f"ALERT: Unusual Activity: {date.today()}"
        email_message = (f"Notification {self.__client_number}: "
                         f"{self.__first_name} {self.__last_name}: {message}")
        
        file_utils.simulate_send_email(self.__email_address, subject, email_message)
