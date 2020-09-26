from command_pattern.commands.command_interface import ICommand


class HottubOnCommand(ICommand):
    def __init__(self, hottub):
        self._hottub = hottub

    def execute(self):
        self._hottub.heat()
        self._hottub.on()
        self._hottub.bubbles_on()


class HottubOffCommand(ICommand):
    def __init__(self, hottub):
        self._hottub = hottub

    def execute(self):
        self._hottub.cool()
        self._hottub.off()
        self._hottub.bubbles_off()

