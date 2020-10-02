from ducks import IDuck


class TurkeyAdapter(IDuck):
    def __init__(self, turkey):
        self._turkey = turkey

    def quack(self):
        self._turkey.gobble()

    def fly(self):
        self._turkey.fly()

