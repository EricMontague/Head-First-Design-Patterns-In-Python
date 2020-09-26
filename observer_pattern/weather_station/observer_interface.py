from abc import ABC, abstractmethod


class IObserver(ABC):
    """Interface for an observer class in the observer pattern."""

    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass

    
