from command.rootCommand import rootCommand
from utils import SQLiteProvider, Config

config_ini_path = "data/config.ini"

class change():
    def __init__(self, index):
        """

        :param index: list
        """
        self.root = rootCommand.rootCommand()
        self.db = SQLiteProvider.SQLite()
        self.config = Config.Config()

        if self.db.id_exist(index[1]):
            if index[2] == "name":
                print("a")
                self.db.setName(id, index[3])
                print(self.config.getMessage(config_ini_path, "change-success"))

            elif index[2] == "age":
                self.db.setAge(id, index[3])
                print(self.config.getMessage(config_ini_path, "change-success"))

            elif index[2] == "sex":
                self.db.setSex(id, index[3])
                print(self.config.getMessage(config_ini_path, "change-success"))

            elif index[2] == "number":
                self.db.setNumber(id, index[3])
                print(self.config.getMessage(config_ini_path, "change-success"))

            else:
                print(self.config.getMessage(config_ini_path, "miss-first"))

            self.db.saveDB()
        else:
            print("そのIDの人はいません")

        print("\n")

        self.root.root_command()