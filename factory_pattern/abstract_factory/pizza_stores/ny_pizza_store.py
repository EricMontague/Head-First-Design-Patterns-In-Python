from abstract_factory.pizza_stores.pizza_store import PizzaStore
from abstract_factory.ingredient_factories import NYIngredientFactory
from abstract_factory.pizzas import CheesePizza, VeggiePizza, ClamPizza, PepperoniPizza


class NYPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        pizza = None
        ingredient_factory = NYIngredientFactory()
        if pizza_type.lower() == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.name = "New York Style Cheese Pizza"
        elif pizza_type.lower() == "veggie":
            pizza = VeggiePizza(ingredient_factory)
            pizza.name = "New York Style Veggie Pizza"
        elif pizza_type.lower() == "clam":
            pizza = ClamPizza(ingredient_factory)
            pizza.name = "New York Style Clam Pizza"
        elif pizza_type.lower() == "pepperoni":
            pizza = PepperoniPizza(ingredient_factory)
            pizza.name = "New York Style Pepperoni Pizza"
        return pizza

