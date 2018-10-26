from http import client

from debug.ClientLogger import ClientLogger, LoggingMode


class ConnectionManager:
    connection = None

    def __init__(self, host, port=443):
        ClientLogger.log(LoggingMode.INFO, 'Establishing connection at <' + host + '> on port <' + str(port) + '>')
        self.connection = client.HTTPConnection(host, port)
        self.connection.connect()
        pass

    def request(self, method, file):
        self.connection.request(method, file)



