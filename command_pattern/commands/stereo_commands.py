from command_pattern.commands.command_interface import ICommand


class StreoOnCommand(ICommand):
    def __init__(self, stereo):
        self._stereo = stereo

    def execute(self):
        self._stereo.on()


class StreoOffCommand(ICommand):
    def __init__(self, stereo):
        self._stereo = stereo

    def execute(self):
        self._stereo.off()


class StreoOnWithCDCommand(ICommand):
    def __init__(self, stereo):
        self._stereo = stereo

    def execute(self):
        self._stereo.on()
        self._stereo.setCD()
        self._stereo.setVolume(11)

