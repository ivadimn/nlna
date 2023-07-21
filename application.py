from PyQt6.QtWidgets import QApplication
from db.connection import ConnectionPool
from settings import db_params


class Application(QApplication):

    def __init__(self, argv):
        super().__init__(argv)

        self.__login = None
        self.__role = None

        conn = ConnectionPool.new_connection(db_params["user"], db_params["password"])
        
    @property
    def login(self):
        return self.__login

    @property
    def role(self):
        return self.__role

    def set_authorized(self, login: str, role: str):
        self.__login = login
        self.__role = role
