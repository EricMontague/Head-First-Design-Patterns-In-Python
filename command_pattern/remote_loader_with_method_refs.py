from setup_imports import setup_imports

# add the parent directory to PYTHON PATH
setup_imports()

from invokers import RemoteControlWithMethodRefs
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
    load_commands,
)


# this function is the client
def remote_loader():

    # Instantiate invoker class
    remote_control = RemoteControlWithMethodRefs()

    # Instantiate receiver classes
    living_room_light = Light("Living Room")
    kitchen_light = Light("Kitchen")
    ceiling_fan = CeilingFan("Living Room")
    garage_door = GarageDoor()
    stereo = Stereo("Living Room")

    # Pass methods reference of receivers to invoker
    remote_control.set_command(0, living_room_light.on, living_room_light.off)
    remote_control.set_command(1, kitchen_light.on, kitchen_light.off)
    remote_control.set_command(2, ceiling_fan.high, ceiling_fan.off)

    commands = [(stereo.on, []), (stereo.set_cd, []), (stereo.set_volume, [11])]
    remote_control.set_command(3, load_commands(commands), stereo.off)
    remote_control.set_command(4, garage_door.open, garage_door.close)

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
