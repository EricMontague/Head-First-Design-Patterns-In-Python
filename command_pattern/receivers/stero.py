class Stereo:
    def __init__(self, location):
        self._location = location
        self._volume = 3

    def on(self):
        print(f"{self._location} Stereo is on")

    def off(self):
        print(f"{self._location} Stereo is off")

    def set_cd(self):
        print(f"{self._location} Stereo is set for CD input")

    def set_dvd(self):
        print(f"{self._location} Stereo is set for DVD input")

    def set_volume(self, volume):
        self._volume = volume
        print(f"{self._location} Stereo volume is set to {self._volume}")

