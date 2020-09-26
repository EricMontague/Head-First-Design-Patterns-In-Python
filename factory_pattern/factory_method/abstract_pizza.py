from abc import ABC, abstractmethod


class AbstractPizza(ABC):
    def __init__(self, name, dough, sauce, toppings):
        self._name = name
        self._dough = dough
        self._sauce = sauce
        self._toppings = toppings

    def prepare(self):
        print(f"Preparing {self._name}")
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings...")
        for topping in self._toppings:
            print(f" {topping}")

    def bake(self):
         print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")

    @property
    def name(self):
        return self._name

