from abstract_factory.ingredients.veggie import Veggie


class BlackOlives(Veggie):
    def __str__(self):
        return "Black Olives"


class Garlic(Veggie):
    def __str__(self):
        return "Garlic"


class Onion(Veggie):
    def __str__(self):
        return "Onion"


class Eggplant(Veggie):
    def __str__(self):
        return "Eggplant"


class Mushrooms(Veggie):
    def __str__(self):
        return "Mushroom"


class RedPepper(Veggie):
    def __str__(self):
        return "RedPepper"


class Spinach(Veggie):
    def __str__(self):
        return "Spinach"
