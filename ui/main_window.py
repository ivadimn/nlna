from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtCore import pyqtSlot
from ui.main_menu import MainMenu
from ui.views.teachers_view import TeachersView


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(250, 250, 1000, 500)

        main_menu = MainMenu(parent=self)
        self.setMenuBar(main_menu)

        main_menu.about_qt.triggered.connect(self.about_qt)
        main_menu.about.triggered.connect(self.about)
        main_menu.teacher_add.triggered.connect(self.teacher_add)
        main_menu.teacher_update.triggered.connect(self.teacher_update)
        main_menu.teacher_delete.triggered.connect(self.teacher_delete)

        self.__teachers_view = TeachersView(parent=self)
        self.setCentralWidget(self.__teachers_view)

    @pyqtSlot()
    def teacher_add(self):
        self.__teachers_view.add()

    @pyqtSlot()
    def teacher_update(self):
        self.__teachers_view.update()

    @pyqtSlot()
    def teacher_delete(self):
        self.__teachers_view.delete()

    @pyqtSlot()
    def about(self):
        title = "Управление заданиями для учащихся"
        text = ("Программа для управления задачами\n" +
                "и заданиями для учащихся школ.")
        QMessageBox.about(self, title, text)

    @pyqtSlot()
    def about_qt(self):
        QMessageBox.aboutQt(self, "Управление заданиями для учащихся")
