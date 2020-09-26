from abc import ABC, abstractmethod


class ISubject(ABC):
    """Interface for the subject in the observer pattern."""

    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass