from command.rootCommand import rootCommand
from utils import SQLiteProvider, Config

class info():
    def __init__(self, index):
        """

        :param index: list
        """
        self.root = rootCommand.rootCommand()
        self.db = SQLiteProvider.SQLite()

        data = self.db.getGuest(index[1])
        print(data)
        print("\n")

        self.root.root_command()