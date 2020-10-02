class Projector:

    def __init__(self, description, dvd_player):
        self._description = description
        self._dvd_player = dvd_player

    def on(self):
        print(f"{self._description} on")

    def off(self):
        print(f"{self._description} off")

    def wide_screen_mode(self):
        print(f"{self._description} in Widescreen Mode (16x9 Aspect Ratio)")

    def tv_mode(self):
        print(f"{self._description} in TV Mode (4x3 Aspect Ratio)")

    def __str__(self):
        return self._description

