from PyQt6.QtSql import QSqlDatabase
import psycopg
from settings import db_params


class Connection:

    _instance: ["Connection"] = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.__connection = QSqlDatabase.addDatabase("QPSQL")
        self.__connection.setHostName(db_params["host"])
        self.__connection.setDatabaseName(db_params["dbname"])
        self.__connection.setPort(db_params["port"])
        self.__connection.setUserName(db_params["user"])
        self.__connection.setPassword(db_params["password"])
        ok = self.__connection.open()
        if ok:
            print("Connection successed!")
        else:
            print("Connection failed!")

    def __del__(self):
        if self.__connection:
            self.__connection.close()

    @property
    def connection(self):
        return self.__connection


class ConnectionNative:

    _instance: ["ConnectionNative"] = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.__connection = psycopg.connect(**db_params)
        if self.__connection:
            print("Connection successed!")
        else:
            print("Connection failed!")

    @property
    def connection(self):
        return self.__connection
