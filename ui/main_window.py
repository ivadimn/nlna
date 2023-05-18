from PyQt6.QtWidgets import QMainWindow
from ui.main_menu import MainMenu


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        main_menu = MainMenu(parent=self)
        self.setMenuBar(main_menu)
