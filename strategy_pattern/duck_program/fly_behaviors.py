from abc import ABC, abstractmethod


class IFlyBehavior(ABC):
    """Interface that defines flying behaviors."""

    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(IFlyBehavior):
    """Class that implements flying with wings."""

    def fly(self):
        print("I'm flying!")


class FlyNoWay(IFlyBehavior):
    """Class for a duck that can't fly."""

    def fly(self):
        print("I can't fly")


class FlyRocketPowered(IFlyBehavior):
    def fly(self):
        print("I'm flying with a rocket!")

