from connection.ConnectionManager import ConnectionManager
from debug.ClientLogger import ClientLogger, LoggingMode
from Bot import Bot


class PrinterConnection:
    con_manager = None

    def __init__(self, host, port=80):
        ClientLogger.log(LoggingMode.INFO, 'Connecting to printer...')
        self.con_manager = ConnectionManager(host, port)

    def get_toner_remaining_life(self, color):
        ClientLogger.log(LoggingMode.INFO, 'Gathering toner information...')
        self.con_manager.request('GET', '/general/information.html')
        response = self.con_manager.connection.getresponse()
        data = response.read()
        data = data.strip()
        print(data)

        pattern = self.get_pattern(data, 'Toner&nbsp;' + color)
        data = data[pattern:]
        start = self.get_pattern(data, '<dd>')
        end = self.get_pattern(data, '</dd>')
        data = data[start + len('<dd>'):end]
        data = data.strip(b'()')
        return data.decode()

    @staticmethod
    def get_pattern(data, name):
        return data.index(str.encode(name))
