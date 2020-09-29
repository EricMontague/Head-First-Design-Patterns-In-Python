class TV:
    def __init__(self, location):
        self._location = location
        self._channel = -1

    def on(self):
        print("TV is on")

    def off(self):
        print("TV is off")

    def set_channel(self, channel):
        self._channel = channel
        print("Channel is set for VCR")
