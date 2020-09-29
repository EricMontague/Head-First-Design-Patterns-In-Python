import functools
from command_pattern.commands.command_interface import ICommand


class MacroCommand(ICommand):
    def __init__(self, commands):
        self._commands = commands

    def execute(self):
        for command in self._commands:
            command.execute()

    def undo(self):
        for command in self._commands:
            command.undo()




def load_commands(commands):
    @functools.wraps(load_commands)
    def wrapper():
        for command, arguments in commands:
            if arguments:
                command(*arguments)
            else:
                command()

    return wrapper

