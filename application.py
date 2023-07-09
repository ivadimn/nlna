from PyQt6.QtWidgets import QApplication
from db.connection import ConnectionPool
from settings import db_params


class Application(QApplication):

    def __init__(self, argv):
        super().__init__(argv)
        conn = ConnectionPool.new_connection(db_params["user"], db_params["password"])
        

