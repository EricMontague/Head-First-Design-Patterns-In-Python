from beverage import IBeverage
from abc import abstractmethod


class CondimentDecorator(IBeverage):
    def __init__(self, beverage):
        self._beverage = beverage

    @property
    @abstractmethod
    def description(self):
        pass

    @abstractmethod
    def cost(self):
        pass

