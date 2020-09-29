from command_pattern.commands import no_command


class RemoteControlWithMethodRefs:
    def __init__(self):
        self._on_commands = [no_command] * 7
        self._off_commands = [no_command] * 7

    def set_command(self, slot, on_command, off_command):
        self._on_commands[slot] = on_command
        self._off_commands[slot] = off_command

    def on_button_was_pushed(self, slot):
        command = self._on_commands[slot]
        command()

    def off_button_was_pushed(self, slot):
        command = self._off_commands[slot]
        command()

    def show_commands(self):
        print("\n------- Remote Control -------\n")
        for index in range(len(self._on_commands)):
            print(
                f"[slot {index}] {self._on_commands[index].__name__} "
                + f"{self._off_commands[index].__name__}\n"
            )

