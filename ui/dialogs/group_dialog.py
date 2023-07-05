from PyQt6.QtWidgets import QDialog
from PyQt6.QtWidgets import QLabel, QLineEdit, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt6.QtCore import pyqtSlot


class GroupDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Группа")

        lbl_title = QLabel("Название группы", parent=self)
        self.__edt_title = QLineEdit(parent=self)

        lbl_comment = QLabel("Комментарии", parent=self)
        self.__edt_comment = QTextEdit(parent=self)

        btn_ok = QPushButton("Ok", parent=self)
        btn_cancel = QPushButton("Отмена", parent=self)

        vbox = QVBoxLayout(self)

        lay_number = QVBoxLayout()
        lay_number.setSpacing(0)
        lay_number.addWidget(lbl_title)
        lay_number.addWidget(self.__edt_title)
        vbox.addLayout(lay_number)

        lay_name = QVBoxLayout()
        lay_name.setSpacing(0)
        lay_name.addWidget(lbl_comment)
        lay_name.addWidget(self.__edt_comment)
        vbox.addLayout(lay_name)

        lay_buttons = QHBoxLayout()
        lay_buttons.addStretch()
        lay_buttons.addWidget(btn_ok)
        lay_buttons.addWidget(btn_cancel)
        vbox.addLayout(lay_buttons)

        btn_cancel.clicked.connect(self.reject)
        btn_ok.clicked.connect(self.finish)

    @property
    def title(self) -> str:
        result = self.__edt_title.text().strip()
        return None if result == "" else result

    @title.setter
    def title(self, value: str):
        self.__edt_title.setText(value)

    @property
    def comment(self) -> str:
        result = self.__edt_comment.toPlainText().strip()
        return None if result == "" else result

    @comment.setter
    def comment(self, value: str):
        self.__edt_comment.setPlainText(value)

    @pyqtSlot()
    def finish(self):
        if self.title is None:
            return
        self.accept()

