from abstract_factory.pizzas.pizza import Pizza


class CheesePizza(Pizza):
    def __init__(self, ingredient_factory):
        self._ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"Preparing {self}")
        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()


class ClamPizza(Pizza):
    def __init__(self, ingredient_factory):
        self._ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"Preparing {self}")
        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()
        self._clam = self._ingredient_factory.create_clam()


class VeggiePizza(Pizza):
    def __init__(self, ingredient_factory):
        self._ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"Preparing {self}")
        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()
        self._veggies = self._ingredient_factory.create_veggies()


class PepperoniPizza(Pizza):
    def __init__(self, ingredient_factory):
        self._ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"Preparing {self}")
        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()
        self._pepperoni = self._ingredient_factory.create_pepperoni()

