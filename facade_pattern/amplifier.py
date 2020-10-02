class Amplifier:

    def __init__(self, description):
        self._description = description
        self._volume = 0
        self._tuner = None
        self._dvd_player = None
        self._cd_player = None

    def on(self):
        print(f"{self._description} is On")

    def off(self):
        print(f"{self._description} is Off")

    def set_surround_sound(self):
        print(f"{self._description} Surround Sound Enabled")

    def set_stereo_sound(self):
        print(f"{self._description} Stereo Mode enabled")

    def set_tuner(self, tuner):
        self._tuner = tuner

    def set_dvd_player(self, dvd_player):
        self._dvd_player = dvd_player

    def set_cd_player(self, cd_player):
        self._cd_player = cd_player

    def set_volume(self, volume):
        self._volume = volume
    
    def __str__(self):
        return self._description