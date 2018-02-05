#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
数据库驱动模块
"""
import pymysql


class mysqlad(object):
    def __init__(self, dbconf, cursor=pymysql.cursors.DictCursor):
        self.__conf = dbconf
        self.__cursor = cursor
        try:
            self.__conn = pymysql.connect(host=self.__conf['host'],
                                          port=self.__conf['port'],
                                          user=self.__conf['user'],
                                          password=self.__conf['password'],
                                          charset='utf8',
                                          db=self.__conf['db'],
                                          cursorclass=self.__cursor)
        except Exception, e:
            raise e

    def close(self):
        self.__conn.close()

    def re_connect(self):
        self.__conn = pymysql.connect(host=self.__conf['host'],
                                      port=self.__conf['port'],
                                      user=self.__conf['user'],
                                      password=self.__conf['password'],
                                      charset='utf8',
                                      db=self.__conf['db_name'],
                                      cursorclass=self.__cursor)

    # 执行插入语句
    def execute_insert(self, dml):
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(dml)
            self.__conn.commit()
        except pymysql.OperationalError as e:
            self.re_connect()
            with self.__conn.cursor() as cursor:
                cursor.execute(dml)
            self.__conn.commit()
        except Exception as e:
            raise e
        return 0

    # 执行查询语句
    def execute_query(self, dml, args=None):
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(dml, args)
                rs = cursor.fetchall()
            self.__conn.commit()
        except pymysql.OperationalError as e:
            self.re_connect()
            with self.__conn.cursor() as cursor:
                cursor.execute(dml, args)
                rs = cursor.fetchall()
            self.__conn.commit()
        except Exception as e:
            raise e
        return rs

    # 执行批量插入数据语句
    def execute_inset_many(self, dml, args):
        try:
            with self.__conn.cursor() as cursor:
                cursor.executemany(dml, args)
            self.__conn.commit()
        except pymysql.OperationalError as e:
            self.re_connect()
            with self.__conn.cursor() as cursor:
                cursor.executemany(dml, args)
            self.__conn.commit()
        except Exception as e:
            raise e
        return 0

    # 展示数据表
    def show_tb(self):
        with self.__conn.cursor() as cursor:
            cursor.execute('show tables')
            tables = cursor.fetchall()
            tables = [item.values()[0] for item in tables]
        return tables

    def insertmany(self, dml):
        try:
            with self.__conn.cursor() as cursor:
                cursor.executemany(dml)
            self.__conn.commit()
        except Exception, e:
            raise e
        return 0