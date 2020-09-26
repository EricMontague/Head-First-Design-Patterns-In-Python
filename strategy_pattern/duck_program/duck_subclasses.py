from duck import Duck
from fly_behaviors import FlyWithWings, FlyNoWay
from quack_behaviors import Quack


class MallardDuck(Duck):
    """Class to represent a mallard duck."""

    def __init__(self):
        self.quack_behavior = Quack()
        self.fly_behavior = FlyWithWings()

    def display(self):
        print("I'm a real Mallard duck!")


class ModelDuck(Duck):
    """Class to represent a model duck."""

    def __init__(self):
        self.quack_behavior = Quack()
        self.fly_behavior = FlyNoWay()

    def display(self):
        print("I'm a model duck!")
