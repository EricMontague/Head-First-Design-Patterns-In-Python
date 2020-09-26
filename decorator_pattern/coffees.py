from beverage import IBeverage


class Espresso(IBeverage):
    def __init__(self, description):
        self._description = description

    @property
    def description(self):
        return self._description

    def cost(self):
        return 1.99


class HouseBlend(IBeverage):
    def __init__(self, description):
        self._description = description

    @property
    def description(self):
        return self._description

    def cost(self):
        return 0.89


class DarkRoast(IBeverage):
    def __init__(self, description):
        self._description = description

    @property
    def description(self):
        return self._description

    def cost(self):
        return 0.99


class Decaf(IBeverage):
    def __init__(self, description):
        self._description = description

    @property
    def description(self):
        return self._description

    def cost(self):
        return 1.05
