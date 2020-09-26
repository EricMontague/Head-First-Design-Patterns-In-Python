from command_pattern.commands.command_interface import ICommand


class NoCommand(ICommand):
    def __init__(self):
        self._receiver = None

    def execute(self):
        pass
