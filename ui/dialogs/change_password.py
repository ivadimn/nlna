from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton
from PyQt6.QtCore import pyqtSlot


class ChangePassword(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        vbox = QVBoxLayout(self)

        lay_passwd1 = QVBoxLayout()
        lay_passwd1.setSpacing(0)
        lbl_passwd1 = QLabel("Введите пароль:", parent=self)
        self.__edt_passwd1 = QLineEdit(parent=self)
        lay_passwd1.addWidget(lbl_passwd1)
        lay_passwd1.addWidget(self.__edt_passwd1)
        vbox.addLayout(lay_passwd1)

        lay_passwd2 = QVBoxLayout()
        lay_passwd2.setSpacing(0)
        lbl_passwd2 = QLabel("Введите пароль ещё раз:", parent=self)
        self.__edt_passwd2 = QLineEdit(parent=self)
        lay_passwd1.addWidget(lbl_passwd2)
        lay_passwd1.addWidget(self.__edt_passwd2)
        vbox.addLayout(lay_passwd2)

        lay_buttons = QHBoxLayout()
        btn_ok = QPushButton("Ок", parent=self)
        lay_buttons.addStretch()
        lay_buttons.addWidget(btn_ok)
        vbox.addLayout(lay_buttons)

        btn_ok.clicked.connect(self.finish)

    @property
    def password1(self):
        result = self.__edt_passwd1.text().strip()
        return None if result == "" else result

    @property
    def password2(self):
        result = self.__edt_passwd2.text().strip()
        return None if result == "" else result


    @pyqtSlot()
    def finish(self):
        if self.password1 != self.password2 or self.password1 is None:
            return
        self.accept()
