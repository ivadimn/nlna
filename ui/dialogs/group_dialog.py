from PyQt6.QtWidgets import QDialog
from PyQt6.QtWidgets import QLabel, QLineEdit
from PyQt6.QtCore import pyqtSlot


class GroupDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Группа")

        lbl_number = QLabel("Номер группы", parent=self)
        self.__edt_number = QLineEdit(parent=self)

        lbl_name = QLabel("Наименование группы", parent=self)
        self.__edt_name = QLineEdit(parent=self)


