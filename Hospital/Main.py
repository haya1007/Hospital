# -*- coding: UTF-8 -*-
import EventListener

from utils import Config
from utils import SQLiteProvider

number = [1, 2]
config_ini_path = "data/config.ini"

class Main:
    def __init__(self):
        pass

    def onEnable(self):
        config_instance = Config.Config()
        config_instance.createConfig(config_ini_path)
        sqlite_instance = SQLiteProvider.SQLite()
        sqlite_instance.createDB()


        func = EventListener.EventListener("data/config.ini")
        func.check(number, func.whatCheck())

if __name__ == '__main__':
    Main().onEnable()
    db = SQLiteProvider.SQLite()
    db.saveDB()
    db.close()