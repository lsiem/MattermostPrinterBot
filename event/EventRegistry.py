class Registry:
    events = {}

    @classmethod
    def register(cls, *args):
        def decorator(fn):
            cls.events[fn] = args
            return fn
        return decorator
