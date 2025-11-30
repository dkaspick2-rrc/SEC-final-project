"""Defines the interface used by concrete subjects."""

__author__ = "Dylan Kaspick"
__version__ = "1.0.0"

from patterns.observer.observer import Observer
from abc import ABC, abstractmethod

class Subject(ABC):
    """A class defining the behavior of a subject."""

    def __init__(self):
        """Initializes a Subject object with an empty list."""

        self._observers = []

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """Attaches an observer to the subject.
        
        Args:
            observer (Observer): The Observer object being added to the
            subjects list of observers.
        """

        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """Detaches an observer from the subject.
        
        Args:
            observer (Observer): The observer being removed from the
            subjects list of observers.
        """

        pass

    @abstractmethod
    def notify(self, message: str) -> None:
        """Notifies all observers of a change made to the subject.
        
        Args:
            message (str): The message being sent to the observers.
        """

        pass
