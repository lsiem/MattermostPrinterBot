import sys
import inspect

from event import EventRegistry


class EventManager:

    @staticmethod
    def call(event):
        for f, c in EventRegistry.Registry.events.items():
            if event in c:
                func = f
                func_name = func.__name__
                module_name = func.__module__
                module = sys.modules[module_name]
                class_members = inspect.getmembers \
                    (module, lambda member: inspect.isclass(member) and member.__module__ == module_name)
                tmp = class_members[0]
                dic = dict(class_members)
                class_member = dic.get(tmp[0])
                cls = getattr(class_member, func_name)
                cls()
        """
    @staticmethod
    def kill(event):
        for k in EventRegistry.Registry.events.values():
            if k == event:
                del EventRegistry.Registry.events[k]
        """

    @staticmethod
    def respawn(event):
        EventRegistry.Registry.register(event)
