import sys
from event import EventRegistry
from event.test import EventTester
from config.Config import Config
from event.EventManager import EventManager
from event.impl import EventCommand
# from wrapper.BotWrapper import BotWrapper
from command.test import CommandTest
import Bot

EventManager.respawn(EventCommand.EventCommand)
EventManager.call(EventCommand.EventCommand)

config = Config(sys.path[0])
bot = Bot.Bot(Config.get_host(), Config.get_user(), Config.get_pass())

# printer_connection = PrinterConnection(config.get_printer_config().get_host())
# life = printer_connection.get_toner_remaining_life('Black')
# output = ('Life remaining for black color: ' + life)
# bot.create_message(output)

sys.exit()
