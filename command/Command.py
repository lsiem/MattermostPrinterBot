class Command:
    name = None

    def __init__(self, name):
        self.name = name

    def get_data(self):
        return self.name

    @staticmethod
    def is_command(text):
        if text.startswith('!'):
            return True
        else:
            return False
