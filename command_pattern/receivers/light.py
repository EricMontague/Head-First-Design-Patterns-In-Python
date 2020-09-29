class Light:
    def __init__(self, location):
        self._location = location

    def on(self):
        print(f"{self._location} Light is On")

    def off(self):
        print(f"{self._location} Light is off")

