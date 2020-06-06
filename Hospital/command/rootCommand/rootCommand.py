from command.rootCommand import helpCommand, infoCommand, guestCommand, changeCommand
from utils import Config
import EventListener

config_ini_path = "data/config.ini"

class rootCommand():
    def __init__(self):
        self.config = Config.Config()

    def root_command(self):
        print("コマンドを入力してください")
        cmd = input("command>>")

        self.check_command(cmd)

    def check_command(self, cmd):
        """

        :param cmd: str
        """
        cmd_split = cmd.split()
        if cmd == "help" or cmd == "h":
            helpCommand.help()

        elif cmd_split[0] == "info":
            if cmd_split[1]:
                infoCommand.info(cmd_split)

            else:
                print(self.config.getMessage(config_ini_path, "no-argument"))
                print("\n")
                self.root_command()

        elif cmd == "guests":
            guestCommand.guest()

        elif cmd_split[0] == "change":
            # if cmd_split[1] == True and cmd_split[2] == True and cmd_split[3] == True:
            changeCommand.change(cmd_split)

            '''else:
                print(self.config.getMessage(config_ini_path, "no-argument"))
                print("\n")
                self.root_command()'''

        elif cmd == "end":
            func = EventListener.EventListener(config_ini_path)
            func.whatCheck()

        else:
            print(self.config.getMessage(config_ini_path, "no-command"))
            self.root_command()