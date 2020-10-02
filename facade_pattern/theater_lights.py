class TheaterLights:

    def __init__(self, description):
        self._description = description
        self._level = 20

    def on(self):
        print(f"{self._description} on ")
    
    def off(self):
        print(f"{self._description} off")

    def dim(self, level):
        print(f"{self._description} dimming to {level}%")
        self._level = level

    def __str__(self):
        return self._description

        