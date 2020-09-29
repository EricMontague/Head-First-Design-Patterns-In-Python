from setup_imports import setup_imports

# add the parent directory to PYTHON PATH
setup_imports()

from invokers import RemoteControl
from receivers import Light, Stereo, TV, Hottub
from commands import (
    LightOffCommand,
    LightOnCommand,
    StereoOffCommand,
    StereoOnWithCDCommand,
    TVOffCommand,
    TVOnCommand,
    HottubOffCommand,
    HottubOnCommand,
    MacroCommand,
)


# this function is the client
def remote_loader():

    # Instantiate invoker class
    remote_control = RemoteControl()

    # Instantiate receiver classes
    living_room_light = Light("Living Room")
    tv = TV("Living Room")
    hottub = Hottub()
    stereo = Stereo("Living Room")

    # Instantiate command classes
    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)

    tv_on = TVOnCommand(tv)
    tv_off = TVOffCommand(tv)

    hottub_on = HottubOnCommand(hottub)
    hottub_off = HottubOffCommand(hottub)

    stereo_on_with_cd = StereoOnWithCDCommand(stereo)
    stereo_off = StereoOffCommand(stereo)

    # instantiate macro commands with lists of commands
    on_commands = [living_room_light_on, tv_on, hottub_on, stereo_on_with_cd]
    off_commands = [living_room_light_off, tv_off, hottub_off, stereo_off]

    party_on_macro = MacroCommand(on_commands)
    party_off_macro = MacroCommand(off_commands)

    # Pass commands to invoker
    remote_control.set_command(0, party_on_macro, party_off_macro)
    remote_control.show_commands()

    # Invoke commands using hte invoker's methods
    remote_control.on_button_was_pushed(0)
    remote_control.off_button_was_pushed(0)
    remote_control.undo_button_was_pushed()
    print()


if __name__ == "__main__":
    remote_loader()
