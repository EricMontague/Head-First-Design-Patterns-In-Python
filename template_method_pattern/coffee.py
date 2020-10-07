from caffeine_beverage import CaffeineBeverage


class Coffee(CaffeineBeverage):

    def brew(self):
        print("Dripping coffee through filter")

    def add_condiments(self):
        print("Adding sugar and milk")

    def customer_wants_condiments(self):
        answer = self.get_user_input()
        if answer.lower().startswith("y"):
            return True
        return False

    def get_user_input(self):
        answer = input("Would you like milk and sugar with your coffee (y/n)? ")
        if answer.lower() in ("1", "yes", "y"):
            return "yes"
        return "no"