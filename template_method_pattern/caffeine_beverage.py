from abc import ABC, abstractmethod


class CaffeineBeverage(ABC):
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()

    def boil_water(self):
        print("Boiling water")

    def pour_in_cup(self):
        print("Pouring into cup")
        
    def customer_wants_condiments(self):
        return True
        
    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass


