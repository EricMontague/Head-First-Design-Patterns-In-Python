from abstract_pizza import AbstractPizza


class ChicagoStyleCheesePizza(AbstractPizza):

    def __init__(self, name, dough, sauce, toppings):
        super().__init__(name, dough, sauce, toppings)

    def cut(self):
        print("Cutting pizza into square slices")


class ChicagoStyleVeggiePizza(AbstractPizza):

    def __init__(self, name, dough, sauce, toppings):
        super().__init__(name, dough, sauce, toppings)

    def cut(self):
        print("Cutting pizza into square slices")


class ChicagoStyleClamPizza(AbstractPizza):

    def __init__(self, name, dough, sauce, toppings):
        super().__init__(name, dough, sauce, toppings)

    def cut(self):
        print("Cutting pizza into square slices")


class ChicagoStylePepperoniPizza(AbstractPizza):

    def __init__(self, name, dough, sauce, toppings):
        super().__init__(name, dough, sauce, toppings)

    def cut(self):
        print("Cutting pizza into square slices")