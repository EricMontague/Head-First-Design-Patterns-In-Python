from command_pattern.commands import NoCommand


class RemoteControlWithUndo:
    def __init__(self):
        self._on_commands = [NoCommand()] * 7
        self._off_commands = [NoCommand()] * 7
        self._undo_command = NoCommand()

    def set_command(self, slot, on_command, off_command):
        self._on_commands[slot] = on_command
        self._off_commands[slot] = off_command

    def on_button_was_pushed(self, slot):
        self._on_commands[slot].execute()
        self._undo_command = self._on_commands[slot]

    def off_button_was_pushed(self, slot):
        self._off_commands[slot].execute()
        self._undo_command = self._off_commands[slot]

    def undo_button_was_pushed(self):
        self._undo_command.undo()

    def show_commands(self):
        print("\n------- Remote Control -------\n")
        for index in range(len(self._on_commands)):
            print(
                f"[slot {index}] {self._on_commands[index].__class__.__name__}"
                + f"{self._off_commands[index].__class__.__name__}\n"
            )

