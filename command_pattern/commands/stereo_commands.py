from command_pattern.commands.command_interface import ICommand


class StereoOnCommand(ICommand):
    def __init__(self, stereo):
        self._stereo = stereo

    def execute(self):
        self._stereo.on()

    def undo(self):
        self._stereo.off()


class StereoOffCommand(ICommand):
    def __init__(self, stereo):
        self._stereo = stereo

    def execute(self):
        self._stereo.off()

    def undo(self):
        self._stereo.on()


class StereoOnWithCDCommand(ICommand):
    def __init__(self, stereo):
        self._stereo = stereo

    def execute(self):
        self._stereo.on()
        self._stereo.set_cd()
        self._stereo.set_volume(11)

    def undo(self):
        self._stereo.off()

