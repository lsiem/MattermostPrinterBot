import asyncio

from mattermostdriver import Driver
import json
import sys

from config.Config import Config
from debug.ClientLogger import ClientLogger, LoggingMode


class Bot:
    bot = None

    host = None
    port = None
    https = None
    username = None
    passwd = None

    driver = None

    bot_info = None

    def __init__(self, host, username, passwd, port=443, https=True):
        Bot.bot = self
        self.host = host
        self.port = port
        self.https = https
        self.username = username
        self.passwd = passwd

        ClientLogger.log(LoggingMode.INFO, "Creating mettermost driver... ")
        self.create_driver()
        ClientLogger.log(LoggingMode.INFO, "Logging in... ")
        self.login()
        ClientLogger.log(LoggingMode.INFO, 'Successfully logged in!')
        from connection.WebSocket import WebSocket
        ClientLogger.log(LoggingMode.INFO, "Setting up web socket...")
        websocket = WebSocket()
        ClientLogger.log(LoggingMode.INFO, "Listening for user commands...")
        asyncio.get_event_loop().run_until_complete(websocket.listen())

    @classmethod
    def get_bot(cls):
        return Bot.bot

    def create_driver(self):
        self.driver = Driver({
            'url': self.host,
            'login_id': self.username,
            'password': self.passwd,
            'scheme': 'https' if self.https else 'http',
            'port': self.port
        })

    def login(self):
        self.driver.login()

        self.bot_info = self.driver.users.get_user_by_username(Config.get_user())

    def logout(self):
        self.driver.logout()

    def kill(self):
        self.logout()
        sys.exit()

    def get_bot_id(self):
        return self.get_id_from_json_data(self.bot_info)

    def get_bot_channel_id(self):
        return self.get_id_from_json_data(
            self.driver.channels.get_channel_by_name_and_team_name(Config.get_team(), Config.get_channel()))

    def create_message(self, text):
        self.driver.posts.create_post({
            'user_id': self.get_bot_id(),
            'channel_id': self.get_bot_channel_id(),
            'message': text
        })

    def get_all_unread_messages(self):
        return self.driver.channels.get_unread_messages(self.get_bot_id(), self.get_bot_channel_id())

    def get_auth_token(self):
        return self.driver.users.get_au

    @staticmethod
    def get_team_name():
        return Config.get_team()

    @staticmethod
    def get_id_from_json_data(data):
        json.loads(json.dumps(data))
        return data['id']
