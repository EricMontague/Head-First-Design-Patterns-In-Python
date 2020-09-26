from abstract_pizza_store import AbstractPizzaStore
from ny_pizzas import (
    NYStyleCheesePizza, 
    NYStyleVeggiePizza, 
    NYStyleClamPizza, 
    NYStylePepperoniPizza
)


class NYPizzaStore(AbstractPizzaStore):

    def create_pizza(self, pizza_type):
        pizza = None
        if pizza_type.lower() == "cheese":
            pizza = NYStyleCheesePizza(
                "NY Style Sauce and Cheese Pizza",
                "Thin Crust Dough",
                "Marinara Sauce",
                ["Grated Reggiano Cheese"]
            )
        elif pizza_type.lower() == "veggie":
            pizza = NYStyleVeggiePizza(
                "NY Style Veggie Pizza",
                "Thin Crust Dough",
                "Marinara Sauce",
                ["Grated Reggiano Cheese", "Garlic", "Onion", "Mushrooms", "Red Pepper"]
            )
        elif pizza_type.lower() == "clam":
            pizza = NYStyleClamPizza(
                "NY Style Clam Pizza",
                "Thin Crust Dough",
                "Marinara Sauce",
                ["Grated Reggiano Cheese", "Fresh Clams from Long Island Sound"]
            )
        elif pizza_type.lower() == "pepperoni":
            pizza = NYStylePepperoniPizza(
                "NY Style Pepperoni Pizza",
                "Thin Crust Dough",
                "Marinara Sauce",
                ["Grated Reggiano Cheese", "Sliced Pepperoni", "Garlic", "Onion", "Mushrooms", "Red Pepper"]
            )
        return pizza

