from decorator import singleton
from metaclass import SingletonMeta


class ChocolateBoiler(metaclass=SingletonMeta):
    def __init__(self, value):
        self._empty = True
        self._boiled = False
        self._value = 12
        print(value)

    def fill(self):
        if self.is_empty():
            self._empty = False
            self._boiled = False
            print("Filling the boiler with milk/chocolate mixture")

    def drain(self):
        if not self.is_empty() and self.is_boiled():
            self._boiled = True
            print("Drain the boiled milk and chocolate")

    def boil(self):
        if not self.is_empty() and not self.is_boiled():
            self._boiled = True
            print("Boil milk/choclate mixture")

    def is_empty(self):
        return self._empty

    def is_boiled(self):
        return self._boiled


old_boiler = ChocolateBoiler(4)
# this second value doesn't matter because it's not going to give me a new instance of the class
new_boiler = ChocolateBoiler(3)
print(old_boiler == new_boiler)
print(type(old_boiler))
print(isinstance(old_boiler, ChocolateBoiler))
