# -*- coding: UTF-8 -*-
from utils import Provider

import sqlite3
import os

import datetime

db_path = "data\database.db"

class SQLite(Provider.Provider):
    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()

    def createDB(self):
        create_table = '''CREATE TABLE IF NOT EXISTS guest (id int PRIMARY KEY, name varchar(64),
                              age int, sex varchar(6), number int, date varchar(126));'''
        self.c.execute(create_table)

        if not self.id_exist(id=1):
            sql = '''insert into guest (id, name, age, sex, number, date) values (?,?,?,?,?,?);'''
            root_record = (1, "root", 99, "男", 00000000000, datetime.datetime.today())
            self.c.execute(sql, root_record)
        self.saveDB()

    def saveDB(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

    def getDB(self):
        return self.c

    def addRecord(self, id, name, age, sex, number):

        sql = '''insert into guest (id, name, age, sex, number, date) values (?,?,?,?,?,?);'''
        user_info = (id, name, age, sex, number, datetime.datetime.today())

        self.c.execute(sql, user_info)
        self.saveDB()

    def removeRecord(self, id):
        self.c.execute("delete from guest where id = %s;" % id)
        self.saveDB()

    def newId(self):
        data = self.getGuests()
        if data == []:
            return 1

        else:
            last_id = data[-1][0]
            return last_id + 1

    def getGuests(self):
        select_guest = '''select * from guest;'''
        self.c.execute(select_guest)

        data = self.c.fetchall()
        return data

    def getGuest(self, id):
        self.c.execute("SELECT * FROM guest WHERE id = %s;" % id)
        data = self.c.fetchone()

        return data

    def id_exist(self, id):
        self.c.execute('''SELECT * FROM guest WHERE id = %s;''' % id)
        data = self.c.fetchone()
        if data:
            return True

        else:
            return False

    def setName(self, id, name):
        self.c.execute(f"UPDATE guest SET name={name} WHERE id={id};")

    def setAge(self, id, age):
        self.c.execute(f'UPDATE guest SET name={age} WHERE id={id};')

    def setSex(self, id, sex):
        self.c.execute(f'UPDATE guest SET sex={sex} WHERE id={id};')

    def setNumber(self, id, number):
        self.c.execute(f'UPDATE guest SET number={number} WHERE id={id};')
