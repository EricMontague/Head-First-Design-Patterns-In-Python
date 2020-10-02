from abc import ABC, abstractmethod


class IDuck(ABC):
    @abstractmethod
    def quack(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class MallardDuck(IDuck):
    def quack(self):
        print("Quack")

    def fly(self):
        print("I'm flying")
