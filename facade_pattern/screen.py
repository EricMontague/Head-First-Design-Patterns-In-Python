class Screen:

    def __init__(self, description):
        self._description = description

    def up(self):
        print(f"{self._description} going up")

    def down(self):
        print(f"{self._description} going down")

    def __str__(self):
        return self._description

        