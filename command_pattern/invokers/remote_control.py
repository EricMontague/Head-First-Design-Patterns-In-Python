from command_pattern.commands import NoCommand


class RemoteControl:
    def __init__(self):
        self._on_commands = [NoCommand()] * 7
        self._off_commands = [NoCommand()] * 7

    def set_command(self, slot, on_command, off_command):
        self._on_commands[slot] = on_command
        self._off_commands[slot] = off_command

    def on_button_was_pushed(self, slot):
        self._on_commands[slot].execute()

    def off_button_was_push(self, slot):
        self._off_commands[slot].execute()

    def __str__(self):
        print("\n------- Remote Control -------\n")
        for index in range(len(self._on_commands)):
            print(
                f"[slot {index}] {self._on_commands[index].__class__.__name__}"
                + f"{self._off_commands[index].__class__.__name__}\n"
            )

