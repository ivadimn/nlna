from PyQt6.QtSql import QSqlDatabase
#import psycopg
from settings import db_params


class Connection:

    def __init__(self, name: str, pwd: str):

        self.__connection = QSqlDatabase.addDatabase("QPSQL", name)
        self.__connection.setHostName(db_params["host"])
        self.__connection.setDatabaseName(db_params["dbname"])
        self.__connection.setPort(db_params["port"])
        self.__connection.setUserName(name)
        self.__connection.setPassword(pwd)
        ok = self.__connection.open()
        if ok:
            print("Connection {0} successed!".format(name))
        else:
            print("Connection failed!")

    def __del__(self):
        if self.__connection:
            self.__connection.close()

    @property
    def connection(self):
        return self.__connection


class ConnectionPool:
    __connections = dict()

    @classmethod
    def new_connection(cls, name: str, password: str) -> Connection:
        conn = Connection(name, password)
        cls.__connections.update({name: conn})
        return conn

    @classmethod
    def get_admin_connection(cls) -> QSqlDatabase:
        return cls.__connections[db_params["user"]].connection

    @classmethod
    def get_noadmin_connection(cls) -> QSqlDatabase:
        for key, value in cls.__connections.items():
            if key != db_params["user"]:
                return value
        else:
            return cls.get_noadmin_connection()

    @classmethod
    def get_connection(cls, name) -> QSqlDatabase:
        for key, value in cls.__connections.items():
            if key == name:
                return value
        else:
            return cls.get_noadmin_connection()
