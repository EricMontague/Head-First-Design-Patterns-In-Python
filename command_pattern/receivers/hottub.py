class Hottub:

    _DEFAULT_TEMPERATURE = 98

    def __init__(self):
        self._on = True
        self._temperature = self._DEFAULT_TEMPERATURE

    def on(self):
        self._on = True

    def off(self):
        self._on = False

    def bubbles_on(self):
        if self._on:
            print("Hottub is bubbling")

    def bubbles_off(self):
        if not self._on:
            print("Hottub is not bubbling")

    def jets_on(self):
        if self._on:
            print("Hottub jets are on")

    def jets_off(self):
        if not self._on:
            print("Hottub jets are off")

    def set_temperature(self, temperature):
        self._temperature = temperature

    def heat(self):
        self._temperature = 105
        print(f"Hottub is heating to a steaming {self._temperature} degrees")

    def cool(self):
        self._temperature = self._DEFAULT_TEMPERATURE
        print(f"Hottub is cooling to {self._DEFAULT_TEMPERATURE} degrees")
