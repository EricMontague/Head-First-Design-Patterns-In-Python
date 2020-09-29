from command_pattern.commands.light_commands import LightOffCommand, LightOnCommand
from command_pattern.commands.no_command import NoCommand, no_command
from command_pattern.commands.ceiling_fan_commands import (
    CeilingFanOffCommand,
    CeilingFanOnCommand,
)
from command_pattern.commands.garage_door_commands import (
    GarageDoorCloseCommand,
    GarageDoorOpenCommand,
)
from command_pattern.commands.hottub_commands import HottubOffCommand, HottubOnCommand
from command_pattern.commands.living_room_light_commands import (
    LivingRoomLightOffCommand,
    LivingRoomLightOnCommand,
)
from command_pattern.commands.stereo_commands import (
    StereoOffCommand,
    StereoOnCommand,
    StereoOnWithCDCommand,
)
from command_pattern.commands.tv_commands import TVOffCommand, TVOnCommand
from command_pattern.commands.macro_command import MacroCommand, load_commands
