# -*- coding: UTF-8 -*-
from utils import Config

from command import Reservation
from command import Cancel

from command.rootCommand import rootCommand

class EventListener:
    def __init__(self, path=None):
        self.config_instance = Config.Config()
        self.reservation = Reservation.Reservation()
        self.cancel = Cancel.Cancel()

        if path is not None:
            self.path = path

    def whatCheck(self):
        """

        :rtype: int
        """
        cmd = None
        while cmd == None:
            print("-----===病院===-----")
            print("予約の方: 「1]を入力")
            print("キャンセルの方: 「2」を入力")
            print("-----=========-----")

            cmd = self.input(self.path, "入力")
            if self.is_int(cmd):
                return cmd

            cmd = None

            print('\n')

    def check(self, number, cmd):
        """

        :param number: List[int, int, ・・・]
        :param cmd: int
        :rtype: int
        """

        if number[0] == cmd:
             # 予約
             self.reservation.check_info()

        elif number[1] == cmd:
             # キャンセル
            self.cancel.cancel()

        elif cmd == 9999:
            #管理者
            print("管理者モード有効")
            root = rootCommand.rootCommand()
            root.root_command()


        else:
            print(self.config_instance.getMessage(self.path, "check-failed"))
            self.whatCheck()

    def input(self, path, string):
        """
        :param path: path
        ;param string: str
        :rtype: int or None
        """

        global cmd
        cmd = ""
        try:
            cmd = int(input("%s=>" % string))

        except ValueError:
            print(self.config_instance.getMessage(path, "is-none"))
            cmd = None

        return cmd

    def is_str(self, obj):
        """

        :param obj: object
        :rtype: bool
        """
        return isinstance(obj, str)

    def is_int(self, obj):
        """

        :param obj: object
        :rtype: bool
        """
        return isinstance(obj, int)

    def is_sex(self, obj):
        """

        :param obj: object
        :rtype: bool
        """
        result = True if obj == "男" or obj == "女" else False
        return result