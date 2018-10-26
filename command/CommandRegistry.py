class CommandRegistry:

    commands = {}

    @classmethod
    def register(cls, *args):
        def decorator(cmd):
            if args[0] in cls.commands:
                cls.commands[args[0]].append(cmd)
            else:
                cls.commands[args[0]] = [cmd]
            return cmd

        return decorator

