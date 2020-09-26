from enum import Enum


class FanLevel(Enum):

    OFF = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class CeilingFan:
    def __init__(self, location):
        self._location = location
        self._level = FanLevel.OFF

    def high(self):
        self._level = FanLevel.HIGH
        print(f"{self._location} ceiling fan is on high")

    def medium(self):
        self._level = FanLevel.MEDIUM
        print(f"{self._location} ceiling fan is on medium")

    def low(self):
        self._level = FanLevel.LOW
        print(f"{self._location} ceiling fan is on low")

    def off(self):
        self._level = FanLevel.OFF
        print(f"{self._location} ceiling fan is off")

    def get_speed(self):
        return self._level

