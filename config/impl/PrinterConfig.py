class PrinterConfig:
    config = {}
    instance = None

    def __init__(self, config):
        PrinterConfig.instance = self
        self.config = config

    def get_host(self):
        return self.config['host']

    def get_port(self):
        return self.config['port']

    @classmethod
    def get_instance(cls):
        return cls.instance
