from setup_imports import setup_imports

# add the parent directory to PYTHON PATH
setup_imports()

from invokers import RemoteControl
from receivers import Light, CeilingFan, GarageDoor, Stereo
from commands import (
    LightOffCommand,
    LightOnCommand,
    CeilingFanOffCommand,
    CeilingFanOnCommand,
    GarageDoorCloseCommand,
    GarageDoorOpenCommand,
    StereoOffCommand,
    StereoOnWithCDCommand,
)


# this function is the client
def remote_loader():

    # Instantiate invoker class
    remote_control = RemoteControl()

    # Instantiate receiver classes
    living_room_light = Light("Living Room")
    kitchen_light = Light("Kitchen")
    ceiling_fan = CeilingFan("Living Room")
    garage_door = GarageDoor()
    stereo = Stereo("Living Room")

    # Instantiate command classes
    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)

    kitchen_light_on = LightOnCommand(kitchen_light)
    kitchen_light_off = LightOffCommand(kitchen_light)

    ceiling_fan_on = CeilingFanOnCommand(ceiling_fan)
    ceiling_fan_off = CeilingFanOffCommand(ceiling_fan)

    garage_door_open = GarageDoorOpenCommand(garage_door)
    garage_door_closed = GarageDoorCloseCommand(garage_door)

    stereo_on_with_cd = StereoOnWithCDCommand(stereo)
    stereo_off = StereoOffCommand(stereo)

    # Pass commands to invoker
    remote_control.set_command(0, living_room_light_on, living_room_light_off)
    remote_control.set_command(1, kitchen_light_on, kitchen_light_off)
    remote_control.set_command(2, ceiling_fan_on, ceiling_fan_off)
    remote_control.set_command(3, stereo_on_with_cd, stereo_off)
    remote_control.set_command(4, garage_door_open, garage_door_closed)

    remote_control.show_commands()

    # Invoke commands using hte invoker's methods
    remote_control.on_button_was_pushed(0)
    remote_control.off_button_was_pushed(0)

    remote_control.on_button_was_pushed(1)
    remote_control.off_button_was_pushed(1)

    remote_control.on_button_was_pushed(2)
    remote_control.off_button_was_pushed(2)

    remote_control.on_button_was_pushed(3)
    remote_control.off_button_was_pushed(3)


if __name__ == "__main__":
    remote_loader()
