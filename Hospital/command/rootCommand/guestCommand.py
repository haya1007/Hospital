from command.rootCommand import rootCommand
from utils import SQLiteProvider, Config

class guest():
    def __init__(self):
        self.root = rootCommand.rootCommand()
        self.db = SQLiteProvider.SQLite()

        for row in self.db.getGuests():
            print(row)

        print("\n")

        self.root.root_command()