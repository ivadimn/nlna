from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtCore import pyqtSlot
from ui.main_menu import MainMenu
from ui.views.teachers_view import TeachersView


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(300, 300, 1000, 500)

        main_menu = MainMenu(parent=self)
        self.setMenuBar(main_menu)

        main_menu.about_qt.triggered.connect(self.about_qt)
        main_menu.about.triggered.connect(self.about)

        self.__view = TeachersView(parent=self)
        main_menu.set_teacher_mode(self.__view)
        self.setCentralWidget(self.__view)

    @pyqtSlot()
    def about(self):
        title = "Управление заданиями для учащихся"
        text = ("Программа для управления задачами\n" +
                "и заданиями для учащихся школ.")
        QMessageBox.about(self, title, text)

    @pyqtSlot()
    def about_qt(self):
        QMessageBox.aboutQt(self, "Управление заданиями для учащихся")
