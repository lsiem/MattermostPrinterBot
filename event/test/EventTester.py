from event.EventRegistry import Registry
from event.impl.EventCommand import EventCommand


class EventTester:

    @staticmethod
    @Registry.register(EventCommand)
    def foo():
        # main.get_bot().create_message("Event system working!")
        pass
