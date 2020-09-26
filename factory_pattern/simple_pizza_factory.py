class SimplePizzaFactory:

    def create_pizza(self, pizza_type):
        pizza = None
        if pizza_type.lower() == "cheese":
            pizza = CheesePizza()
        elif pizza_type.lower() == "pepperoni":
            pizza = PepperoniPizza()
        elif pizza_type.lower() == "clam":
            pizza = ClamPizza()
        elif pizza_type.lower() == "veggie":
            pizza = VeggiePizza()
        return pizza
        
         