from Bot import Bot
from command.CommandRegistry import CommandRegistry
import sys
import inspect

from command.impl.PrinterDrumLifecycle import PrinterDrumLifecycle


class CommandManager:

    @staticmethod
    def call(command, *args):
        for f, c in CommandRegistry.commands.items():
            if command == f:
                func = c[0]
                func_name = func.__name__
                module_name = func.__module__
                module = sys.modules[module_name]
                class_members = inspect.getmembers \
                    (module, lambda member: inspect.isclass(member) and member.__module__ == module_name)
                tmp = class_members[0]
                dic = dict(class_members)
                class_member = dic.get(tmp[0])
                cls = getattr(class_member, func_name)
                cls(*args)

    @staticmethod
    def check_command(name, arg):
        if name == '!printer':
            printer_colors = ['Black', 'Yellow', 'Cyan', 'Magenta']
            if arg in printer_colors:
                CommandManager.call(PrinterDrumLifecycle, arg)
            elif arg == '':
                for color in printer_colors:
                    CommandManager.call(PrinterDrumLifecycle, color)
            else:
                Bot.get_bot().create_message('Unknown argument: ' + arg)
        else:
            Bot.get_bot().create_message('Unknown command: ' + name)
