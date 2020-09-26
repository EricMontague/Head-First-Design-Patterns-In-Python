from abstract_factory.ingredient_factories.pizza_ingredient_factory import (
    PizzaIngredientFactory,
)
from abstract_factory.ingredients import (
    ThinCrustDough,
    MarinaraSauce,
    ReggianoCheese,
    Garlic,
    Onion,
    Mushrooms,
    RedPepper,
    SlicedPepperoni,
    FreshClams,
)


class NYIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThinCrustDough()

    def create_sauce(self):
        return MarinaraSauce()

    def create_cheese(self):
        return ReggianoCheese()

    def create_veggies(self):
        veggies = [Garlic(), Onion(), Mushrooms(), RedPepper()]
        return veggies

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clams(self):
        return FreshClams()
