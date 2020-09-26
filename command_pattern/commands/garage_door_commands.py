from command_pattern.commands.command_interface import ICommand


class GarageDoorOpenCommand(ICommand):

    def __init__(self, garage_door):
        self._garage_door = garage_door

    def execute(self):
        self._garage_door.open()


class GarageDoorCloseCommand(ICommand):

    def __init__(self, garage_door):
        self._garage_door = garage_door

    def execute(self):
        self._garage_door.close()        