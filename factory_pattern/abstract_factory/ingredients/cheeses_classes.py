from abstract_factory.ingredients.cheese import Cheese


class ReggianoCheese(Cheese):

    def __str__(self):
        return "Reggiano Cheese"


class ParmesanCheese(Cheese):

    def __str__(self):
        return "Shredded Parmesan"


class MozzarellaCheese(Cheese):

    def __str__(self):
        return "Shredded Mozzarella"