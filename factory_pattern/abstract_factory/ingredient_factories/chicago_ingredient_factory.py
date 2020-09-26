from abstract_factory.ingredient_factories.pizza_ingredient_factory import (
    PizzaIngredientFactory,
)
from abstract_factory.ingredients import (
    ThickCrustDough,
    PlumTomatoSauce,
    MozzarellaCheese,
    BlackOlives,
    Spinach,
    Eggplant,
    SlicedPepperoni,
    FrozenClams,
)


class ChicagoIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThickCrustDough()

    def create_sauce(self):
        return PlumTomatoSauce()

    def create_cheese(self):
        return MozzarellaCheese()

    def create_veggies(self):
        veggies = [BlackOlives(), Spinach(), Eggplant()]
        return veggies

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clams(self):
        return FrozenClams()

