from command_pattern.commands.command_interface import ICommand
from command_pattern.receivers.ceiling_fan import FanLevel


class CeilingFanOnCommand(ICommand):
    def __init__(self, ceiling_fan):
        self._ceiling_fan = ceiling_fan
        self._previous_speed = -1

    def execute(self):
        self._previous_speed = self._ceiling_fan.get_speed()
        self._ceiling_fan.high()

    def undo(self):
        if self._previous_speed == FanLevel.HIGH:
            self._ceiling_fan.high()
        elif self._previous_speed == FanLevel.MEDIUM:
            self._ceiling_fan.medium()
        elif self._previous_speed == FanLevel.LOW:
            self._ceiling_fan.low()
        elif self._previous_speed == FanLevel.OFF:
            self._ceiling_fan.off()


class CeilingFanOffCommand(ICommand):
    def __init__(self, ceiling_fan):
        self._ceiling_fan = ceiling_fan
        self._previous_speed = -1

    def execute(self):
        self._previous_speed = self._ceiling_fan.get_speed()
        self._ceiling_fan.off()

    def undo(self):
        if self._previous_speed == FanLevel.HIGH:
            self._ceiling_fan.high()
        elif self._previous_speed == FanLevel.MEDIUM:
            self._ceiling_fan.medium()
        elif self._previous_speed == FanLevel.LOW:
            self._ceiling_fan.low()
        elif self._previous_speed == FanLevel.OFF:
            self._ceiling_fan.off()
