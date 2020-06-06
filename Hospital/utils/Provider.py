# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod

class Provider(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        # SQLite3の作成、または読み込み
        pass

    @abstractmethod
    def createDB(self):
        pass

    @abstractmethod
    def saveDB(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def getDB(self):
        pass

    @abstractmethod
    def addRecord(self, id, name, age, sex, number):
        """

        :param id: PRIMARY KEY
        :param name: str
        :param age: int
        :param sex: str
        :param number: int
        """
        pass

    @abstractmethod
    def removeRecord(self, id):
        """

        :param id: PRIMARY KEY
        """
        pass

    @abstractmethod
    def newId(self):
        pass

    @abstractmethod
    def getGuests(self):
        """

        :return: list[id, name, age, sex, number] * ?
        """
        pass

    @abstractmethod
    def getGuest(self, id):
        """

        :param id: PRIMARY KEY
        :return: list[id, name, age, sex, number]
        """
        pass

    @abstractmethod
    def id_exist(self, id):
        """

        :param id: PRIMARY KEY
        :return: True or False
        """
        pass

    @abstractmethod
    def setName(self, id, name):
        """

        :param id: PRIMARY KEY
        :param name: str
        """
        pass

    @abstractmethod
    def setAge(self, id, age):
        """

        :param id: PRIMARY KEY
        :param age: int
        """
        pass

    @abstractmethod
    def setSex(self, id, sex):
        """

        :param id: PRIMARY KEY
        :param sex: str
        """
        pass

    @abstractmethod
    def setNumber(self, id, number):
        """

        :param id: PRIMARY KEY
        :param number: int
        """
        pass