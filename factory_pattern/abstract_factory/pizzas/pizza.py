from abc import ABC, abstractmethod


class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, pizza_name):
        self._name = pizza_name

    def __str__(self):
        return self._name

