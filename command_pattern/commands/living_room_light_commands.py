from command_pattern.commands.command_interface import ICommand


class LivingRoomLightOnCommand(ICommand):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.on()

    def undo(self):
        self._light.off()


class LivingRoomLightOffCommand(ICommand):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.off()

    def undo(self):
        self._light.on()

