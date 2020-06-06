# -*- coding: UTF-8 -*-
import EventListener

from utils import SQLiteProvider
from utils import Config

config_ini_path = "data/config.ini"

class Cancel():
    def __init__(self):
        self.db = SQLiteProvider.SQLite()
        self.config_instance = Config.Config()

    def cancel(self):
        cmd = True
        while cmd:
            print("----==キャンセル==----")
            print("お客様が予約した際のIDを入力してください")
            print("-----==========-----")

            func = EventListener.EventListener(config_ini_path)
            id = func.input(config_ini_path, "ID")

            if not func.is_str(id):
                if not self.db.id_exist(id):
                    self.db.removeRecord(id)
                    print(self.config_instance.getMessage(config_ini_path, "check-id"))
                    print(self.config_instance.getMessage(config_ini_path, "successfully-cancel"))
                    func.whatCheck()
                    print("\n")
                    
                else:
                    print(self.config_instance.getMessage(config_ini_path, "check-id"))
                    func.whatCheck()
                    print("\n")

                cmd = False
            else:
                print(self.config_instance.getMessage(config_ini_path, "not-int"))