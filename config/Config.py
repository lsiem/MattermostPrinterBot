import sys

from config.impl.PrinterConfig import PrinterConfig
from debug.ClientLogger import ClientLogger, LoggingMode


class Config:
    instance = None
    config = {}
    additional_configs = []
    path = ''

    def __init__(self, path):
        Config.instance = self
        self.path = path
        ClientLogger.log(LoggingMode.INFO, 'Trying to read bot configuration...')
        try:
            file = open(path + '/config.txt', 'r')
        except FileNotFoundError:
            ClientLogger.log(LoggingMode.ERROR, 'No config found... Exciting!')
            sys.exit()
        cfg = {}
        for line in file:
            if line.startswith('#'):
                continue
            (key, val) = line.split(':')
            cfg[key] = val.strip()
        global config
        config = cfg
        self.handle_additional_sources()
        self.cleanup()

    @staticmethod
    def cleanup():
        valid_entries = ['host', 'user', 'pass', 'channel', 'team', 'access_token']
        for k in list(config.keys()):
            if k not in valid_entries:
                del config[k]

    def handle_additional_sources(self):
        for key in config.keys():
            if key == 'source':
                self.additional_configs.append(self.load_additional_config(self.path + '/' + config[key]))

    @staticmethod
    def load_additional_config(path):
        file = open(path)
        cfg = {}
        for line in file:
            if line.startswith('#'):
                continue
            (key, val) = line.split(':')
            cfg[key] = val.strip()

        for key in cfg.keys():
            if key == 'plugin':
                if cfg[key] == 'printer':
                    return PrinterConfig(cfg)

    @staticmethod
    def get_host():
        return config['host']

    @staticmethod
    def get_user():
        return config['user']

    @staticmethod
    def get_pass():
        return config['pass']

    @staticmethod
    def get_channel():
        return config['channel']

    @staticmethod
    def get_team():
        return config['team']

    @staticmethod
    def get_access_token():
        return config['access_token']

    def get_printer_config(self):
        for obj in self.additional_configs:
            if isinstance(obj, PrinterConfig):
                return obj

    @classmethod
    def get_instance(cls):
        return cls.instance
