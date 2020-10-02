class CDPlayer:
    def __init__(self, description, amplifier):
        self._description = description
        self._title = None
        self._current_track = -1
        self._amplifier = amplifier

    def on(self):
        print(f"{self._description} on")

    def off(self):
        print(f"{self._description} off")

    def eject(self):
        self._title = None
        print(f"{self._description} eject")

    def set_cd_title(self, title):
        self._title = title
        self._current_track = 0
        print(f"CD named {title} is set")

    def play_track(self, track):
        if not self._title:
            print(
                f"{self._description} can't play track {self._current_track}, no cd inserted"
            )
        else:
            self._current_track = track
            print(f"{self._description} playing track {self._current_track}")

    def stop(self):
        self._current_track = 0
        print(f"{self._description} stopped")

    def pause(self):
        print(f"{self._description} paused {self._title}")

    def __str__(self):
        return self._description
