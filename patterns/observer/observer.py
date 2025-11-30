"""Defines the interface used by concrete observers."""

__author__ = "Dylan Kaspick"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class Observer(ABC):
    """A class defining the behavior of an observer."""

    @abstractmethod
    def update(self, message: str) -> None:
        """Notifies the observer when there are changes in the subject.
        
        Args:
            message (str): The message sent from the subject.
        """

        pass