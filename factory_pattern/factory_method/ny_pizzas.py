from abstract_pizza import AbstractPizza


class NYStyleCheesePizza(AbstractPizza):
    def __init__(self, name, dough, sauce, toppings):
        super().__init__(name, dough, sauce, toppings)


class NYStyleClamPizza(AbstractPizza):
    def __init__(self, name, dough, sauce, toppings):
        super().__init__(name, dough, sauce, toppings)


class NYStyleVeggiePizza(AbstractPizza):
    def __init__(self, name, dough, sauce, toppings):
        super().__init__(name, dough, sauce, toppings)


class NYStylePepperoniPizza(AbstractPizza):
    def __init__(self, name, dough, sauce, toppings):
        super().__init__(name, dough, sauce, toppings)

