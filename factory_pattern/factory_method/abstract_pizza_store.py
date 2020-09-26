from abc import ABC, abstractmethod


class AbstractPizzaStore(ABC):
    def order_pizza(self, pizza_type):
        pizza = self.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @abstractmethod
    def create_pizza(self, pizza_type):
        pass
