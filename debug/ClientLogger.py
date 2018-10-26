from time import gmtime, strftime


class ClientLogger:

    @staticmethod
    def log(mode, text):
        print('[', mode, ']', strftime("%Y-%m-%d %H:%M:%S", gmtime()), text)


class LoggingMode:
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
