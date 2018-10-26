from Bot import Bot
from command.CommandRegistry import CommandRegistry
from command.impl.PrinterDrumLifecycle import PrinterDrumLifecycle
from config.impl.PrinterConfig import PrinterConfig
from connection.impl.PrinterConnection import PrinterConnection


class CommandTest:

    @staticmethod
    @CommandRegistry.register(PrinterDrumLifecycle)
    def on_command(color):
        print("on_command was called with argument: ", color)
        color = color.strip()
        printer_connection = PrinterConnection(PrinterConfig.get_instance().get_host())
        life = printer_connection.get_toner_remaining_life(color=color)
        output = ('Life remaining for ' + color + ' color: ' + str(life))
        Bot.bot.create_message(output)
