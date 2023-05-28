from PyQt6.QtWidgets import QApplication
from db.connection import Connection


class Application(QApplication):

    def __init__(self, argv):
        super().__init__(argv)
        conn = Connection()
        

