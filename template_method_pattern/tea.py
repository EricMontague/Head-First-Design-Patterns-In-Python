from caffeine_beverage import CaffeineBeverage


class Tea(CaffeineBeverage):

    def brew(self):
        print("Steeping the tea")

    def add_condiments(self):
        print("Adding lemon")

    def customer_wants_condiments(self):
        answer = self.get_user_input()
        if answer.lower().startswith("y"):
            return True
        return False

    def get_user_input(self):
        answer = input("Would you like lemon in your tea (y/n)? ")
        if answer.lower() in ("1", "yes", "y"):
            return "yes"
        return "no"