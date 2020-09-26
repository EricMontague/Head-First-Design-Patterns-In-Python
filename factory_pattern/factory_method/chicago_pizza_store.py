from abstract_pizza_store import AbstractPizzaStore
from chicago_pizzas import (
    ChicagoStyleCheesePizza, 
    ChicagoStyleVeggiePizza, 
    ChicagoStyleClamPizza, 
    ChicagoStylePepperoniPizza
)


class ChicagoPizzaStore(AbstractPizzaStore):

    def create_pizza(self, pizza_type):
        pizza = None
        if pizza_type.lower() == "cheese":
            pizza = ChicagoStyleCheesePizza(
                "Chicago Style Deep Dish Cheese Pizza",
                "Extra Thick Crust Dough",
                "Plum Tomato Sauce",
                ["Shredded Mozzarella Cheese"]
            )
        elif pizza_type.lower() == "veggie":
            pizza = ChicagoStyleVeggiePizza(
                "Chicago Deep Dish Veggie Pizza",
                "Extra Thick Crust Dough",
                "Plum Tomato Sauce",
                [
                    "Shredded Mozzarella Cheese",
                    "Black Olives",
                    "Spinach",
                    "Eggplant"
                ]
            )
        elif pizza_type.lower() == "clam":
            pizza = ChicagoStyleClamPizza(
                "Chicago Style Clam Pizza",
                "Extra Thick Crust Dough",
                "Plum Tomato Sauce",
                ["Shredded Mozzarella Cheese", "Frozen Clams from Chesapeake Bay"]
            )
        elif pizza_type.lower() == "pepperoni":
            pizza = ChicagoStylePepperoniPizza(
                "Chicago Style Pepperoni Pizza",
                "Extra Thick Crust Dough",
                "Plum Tomato Sauce",
                [
                    "Shredded Mozzarella Cheese",
                    "Black Olives",
                    "Spinach",
                    "Eggplant",
                    "Sliced Pepperoni"
                ]
            )
        return pizza

        