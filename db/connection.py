from typing import Optional
from PyQt6.QtSql import QSqlDatabase, QSqlQuery
from PyQt6.QtWidgets import QApplication
from settings import db_params

import logging
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)

SELECT_LOGIN = """
    SELECT id, f_login, f_password_hash, f_enabled, f_expire, f_role, f_salt
    FROM appuser WHERE f_login=? ;
"""

UPDATE_PASSWORD = """
    UPDATE appuser SET f_password_hash=? WHERE id=? ;
"""


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
            LOG.info("Connection {0} successed!".format(name))
        else:
            print("Connection failed!")
            LOG.error("Connection failed!")

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
    def get_root_connection(cls) -> QSqlDatabase:
        return cls.__connections[db_params["user"]].connection

    @classmethod
    def get_noroot_connection(cls) -> QSqlDatabase:
        for key, value in cls.__connections.items():
            if key != db_params["user"]:
                return value
        else:
            return cls.get_noroot_connection()

    @classmethod
    def get_connection(cls, name) -> QSqlDatabase:
        for key, value in cls.__connections.items():
            if key == name:
                return value
        else:
            return cls.get_noroot_connection()


def get_user_info(login: str) -> Optional[dict]:
    query = QSqlQuery(ConnectionPool.get_root_connection())
    query.prepare(SELECT_LOGIN)
    query.addBindValue(login)
    query.exec()
    data = dict()
    if query.first():
        data["user_id"] = query.value("id")
        data["login"] = query.value("f_login")
        data["password_hash"] = query.value("f_password_hash")
        data["enabled"] = query.value("f_enabled")
        data["expire"] = query.value("f_expire")
        data["role"] = query.value("f_role")
        data["salt"] = query.value("f_salt")
        return data
    else:
        return None


def update_password(user_info: dict):
    query = QSqlQuery(ConnectionPool.get_root_connection())
    query.prepare(UPDATE_PASSWORD)
    query.addBindValue(user_info["password_hash"])
    query.addBindValue(user_info["user_id"])
    query.exec()
