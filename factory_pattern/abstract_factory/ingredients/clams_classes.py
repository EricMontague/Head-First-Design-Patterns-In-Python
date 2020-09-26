from abstract_factory.ingredients.clams import Clams


class FreshClams(Clams):
    def __str__(self):
        return "Fresh Clams from London Island Sound"


class FrozenClams(Clams):
    def __str__(self):
        return "Frozen Clams from the Chesapeake Bay"

