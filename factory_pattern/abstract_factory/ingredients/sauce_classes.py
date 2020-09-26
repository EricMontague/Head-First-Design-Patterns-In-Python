from abstract_factory.ingredients.sauce import Sauce


class MarinaraSauce(Sauce):
    def __str__(self):
        return "Marinara Sauce"


class PlumTomatoSauce(Sauce):
    def __str__(self):
        return "Tomato sauce with plum tomatoes"
