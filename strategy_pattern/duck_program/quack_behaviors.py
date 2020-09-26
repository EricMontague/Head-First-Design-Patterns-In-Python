from abc import ABC, abstractmethod


class IQuackBehavior(ABC):
    """Interface for quack behaviors."""

    @abstractmethod
    def quack(self):
        pass


class Quack(IQuackBehavior):
    """Class that allows a duck to quack."""

    def quack(self):
        print("Quack!")


class MuteQuack(IQuackBehavior):
    """Class for ducks that can't quack."""

    def quack(self):
        print("<<Silence>>")


class Squeak(IQuackBehavior):
    """Class for ducks that squeak."""

    def quack(self):
        print("Squeak!")
