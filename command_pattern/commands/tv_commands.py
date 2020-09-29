from command_pattern.commands.command_interface import ICommand


class TVOnCommand(ICommand):
    def __init__(self, tv):
        self._tv = tv

    def execute(self):
        self._tv.on()
        self._tv.set_channel(45)

    def undo(self):
        self._tv.off()


class TVOffCommand(ICommand):
    def __init__(self, tv):
        self._tv = tv

    def execute(self):
        self._tv.off()

    def undo(self):
        self._tv.on()
