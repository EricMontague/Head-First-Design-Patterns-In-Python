from condiment_decorator import CondimentDecorator


class SteamedMilk(CondimentDecorator):
    def __init__(self, beverage):
        super().__init__(beverage)

    @property
    def description(self):
        return self._beverage.description + " with " + "Steamed Milk"

    def cost(self):
        return self._beverage.cost() + 0.1


class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        super().__init__(beverage)

    @property
    def description(self):
        return self._beverage.description + " with " + "Mocha"

    def cost(self):
        return self._beverage.cost() + 0.2


class Soy(CondimentDecorator):
    def __init__(self, beverage):
        super().__init__(beverage)

    @property
    def description(self):
        return self._beverage.description + " with " + "Soy"

    def cost(self):
        return self._beverage.cost() + 0.15


class Whip(CondimentDecorator):
    def __init__(self, beverage):
        super().__init__(beverage)

    @property
    def description(self):
        return self._beverage.description + " with " + "Whip"

    def cost(self):
        return self._beverage.cost() + 0.1
