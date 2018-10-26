import websockets
import Bot
from command.Command import Command
from command.CommandManager import CommandManager
from command.impl.PrinterDrumLifecycle import PrinterDrumLifecycle
from config.Config import Config
import json


class WebSocket:
    auth_cookie = ''
    uri = 'wss://' + Config.get_host() + '/api/v4/websocket'

    def __init__(self):
        self.auth_cookie = 'MMAUTHTOKEN=' + Config.get_access_token() + '; MMUSERID=' + Bot.Bot.get_bot().get_bot_id()

    async def listen(self):
        async with websockets.connect(
                uri=self.uri,
                extra_headers=[('Cookie', self.auth_cookie)]) \
                as websocket:
            while True:
                receive = await websocket.recv()
                dump = json.loads(receive)
                if 'data' in dump:
                    if 'post' in dump['data']:
                        post_dump = dump['data']['post']
                        post_dump = post_dump.strip()
                        index = post_dump.index('message')
                        message = post_dump[index + len('message') + 2:post_dump.index(',', index)]
                        message = message[1:len(message) - 1]
                        message = message.strip()
                        if Command.is_command(message):
                            if ' ' in message:
                                command, arg = message.split(' ')
                                CommandManager.check_command(command, arg)
                            else:
                                CommandManager.check_command(message, '')
