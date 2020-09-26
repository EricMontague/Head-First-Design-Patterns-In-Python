from abc import ABC, abstractmethod


class IBeverage(ABC):
    @property
    @abstractmethod
    def description(self):
        pass

    @abstractmethod
    def cost(self):
        pass

