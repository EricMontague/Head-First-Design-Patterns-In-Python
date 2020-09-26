from command_pattern.commands.command_interface import ICommand


class CeilingFanOnCommand(ICommand):

    def __init__(self, ceiling_fan):
        self._ceiling_fan = ceiling_fan

    def execute(self):
        self._ceiling_fan.high()


class CeilingFanOffCommand(ICommand):

    def __init__(self, ceiling_fan):
        self._ceiling_fan = ceiling_fan

    def execute(self):
        self._ceiling_fan.off()