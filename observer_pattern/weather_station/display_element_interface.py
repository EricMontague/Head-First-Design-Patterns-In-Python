from abc import ABC, abstractmethod


class IDisplayElement(ABC):
    """Interface for a weather display element."""

    @abstractmethod
    def display(self):
        pass