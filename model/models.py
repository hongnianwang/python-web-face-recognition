# -*- coding: utf-8 -*-

from .db import DbConnection
import time

class UserModel(DbConnection):

    def add_user(self, **kwargs):
        # 往数据里添加用户信息
        try:
            self.connect()
            sql = "insert into user (username, groupname , c_time) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, (
                kwargs['username'], kwargs['groupname'], time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))
            self.close()
            return self.cursor.lastrowid
        except Exception as e:
            print(e)

    def add_user_login(self, **kwargs):
        # 往login表里添加用户信息
        try:
            self.connect()
            sql = "insert into user_login (username, groupname , c_time) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, (
                kwargs['username'], kwargs['groupname'], time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))
            self.close()
            return self.cursor.lastrowid
        except Exception as e:
            print(e)

    def get_id_by_name(self, username):
        # group by username
        try:
            self.connect()
            sql = "select count(*) count,username from user_login where username=%s group by username;"
            print(sql)
            self.cursor.execute(sql, (username, ))
            id = self.cursor.fetchone()
            print(id)
            if id:
                return id
        except Exception as e:
            print(e)