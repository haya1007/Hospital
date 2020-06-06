# -*- coding: UTF-8 -*-
import EventListener

from utils import SQLiteProvider
from utils import Config

config_ini_path = "data/config.ini"

class Reservation():
    def __init__(self):
        self.db = SQLiteProvider.SQLite()
        self.config_instance = Config.Config()

    def check_info(self):

        func = EventListener.EventListener(config_ini_path)
        id = self.db.newId()
        print("-----===予約===-----")
        print("お客様の個人情報を入力してください")
        print("順番に")
        print("1.名前(漢字でフルネーム")
        print("2.年齢")
        print("3.性別(男 or 女)")
        print("4.電話番号(ハイフンなし)")
        print("-----=========-----")

        data = self.guest_info_input()
        self.db.addRecord(id, data[0], data[1], data[2], data[3])
        print(self.config_instance.getMessage(config_ini_path, "successfully-save"))
        print("ID: %d\n必ず保管しておいてください" % id)
        func.whatCheck()
        print("\n")


    def guest_info_input(self):
        """

        :return: [name, age, sex, number]
        """
        global number, sex, age, name
        index = [True, True, True, True]
        func = EventListener.EventListener()
        while index[0]:
            name = input("名前=>")
            if func.is_str(name):
                if not name == "":
                    index[0] = False
                else:
                    print(self.config_instance.getMessage(config_ini_path, "is-none"))
            else:
                print(self.config_instance.getMessage(config_ini_path, "not-str"))

        while index[1]:
            age = func.input(config_ini_path, "年齢")
            if func.is_int(age):
                index[1] = False
            else:
                print(self.config_instance.getMessage(config_ini_path, "not-int"))

        while index[2]:
            sex = input("性別=>")
            if func.is_sex(sex):
                index[2] = False
            else:
                print(self.config_instance.getMessage(config_ini_path, "not-sex"))

        while index[3]:
            number = func.input(config_ini_path, "電話番号")
            if func.is_int(number):
                index[3] = False
            else:
                print(self.config_instance.getMessage(config_ini_path, "not-int"))

        data = [name, age, sex, number]
        return data