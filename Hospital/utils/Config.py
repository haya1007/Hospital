# -*- coding: UTF-8 -*-
import configparser

# ファイル存在チェック用
import os

class Config():
    def __init__(self):
        pass

    def createConfig(self, config_ini_path):
        """

        :param config_ini_path: str
        """

        config = configparser.ConfigParser()
        if not os.path.exists(config_ini_path):
            section = "String"
            config.add_section(section)
            config.set(section, 'check-failed', '入力された値が正しくありません')
            config.set(section, 'not-int', '数字で入力してください')
            config.set(section, 'not-str', '文字列で入力してください')
            config.set(section, 'not-sex', '性別の入力方法が違います')
            config.set(section, 'successfully-save', '予約しました')
            config.set(section, 'successfully-cancel', 'キャンセルしました')
            config.set(section, 'check-id', 'IDを確認しました')
            config.set(section, 'not-exist', 'IDが存在しませんでした')
            config.set(section, 'is_none', '入力してください')
            config.set(section, 'miss-first', '第一引数が間違っています')
            config.set(section, 'change-success', '変更しました')
            config.set(section, 'no-argument', '引数がありません')
            config.set(section, 'no-command', 'そのようなコマンドはありません')

            with open(config_ini_path, 'w') as file:
                config.write(file)

    def getMessage(self, config_ini_path, key, section="String"):
        """
        :param config_ini_path: path
        :param key: str
        :param string: str
        :rtype: str or None
        """

        config = configparser.ConfigParser()
        config.read(config_ini_path)

        if config.has_option(section, key):
            return config.get(section, key)

        else:
            return None