class Tuner:

    def __init__(self, description, amplifier):
        self._description = description
        self._amplifier = amplifier
        self._frequency = 0

    def on(self):
        print(f"{self._description} on")

    def off(self):
        print(f"{self._description} off")

    def set_frequency(self, frequency):
        print(f"{self._description} setting frequency to {frequency}")
        self._frequency = frequency

    def set_am(self):
        print(f"{self._description} setting AM mode")

    def set_fm(self):
        print(f"{self._description} setting FM mode")

    def __str__(self):
        return self._description
