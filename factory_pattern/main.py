import sys
import os

current_directory = os.path.abspath(os.path.dirname(__file__))
if current_directory not in sys.path:
    sys.path.insert(0, current_directory)
from abstract_factory.pizza_stores import NYPizzaStore, ChicagoPizzaStore


def main():

    ny_store = NYPizzaStore()
    chicago_store = ChicagoPizzaStore()

    pizza = ny_store.order_pizza("cheese")
    print(f"Ethan ordered a {pizza.name}\n")

    pizza = chicago_store.order_pizza("cheese")
    print(f"Joel order a {pizza.name}\n")


if __name__ == "__main__":
    main()
