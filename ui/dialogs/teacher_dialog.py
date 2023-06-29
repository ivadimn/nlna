from PyQt6.QtWidgets import QDialog
from PyQt6.QtWidgets import QLabel, QLineEdit, QTextEdit, QPushButton
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import pyqtSlot


class TeacherDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Учитель")

        lbl_fio = QLabel("Фамилия, Имя, Отчество", parent=self)
        self.__edt_fio = QLineEdit(parent=self)

        lbl_phone = QLabel("Телефон", parent=self)
        self.__edt_phone = QLineEdit(parent=self)

        lbl_email = QLabel("E-mail", parent=self)
        self.__edt_email = QLineEdit(parent=self)

        lbl_comment = QLabel("Примечание", parent=self)
        self.__edt_comment = QTextEdit(parent=self)

        btn_ok = QPushButton("Ok", parent=self)
        btn_cancel = QPushButton("Отмена", parent=self)

        vbox = QVBoxLayout(self)

        lay_fam = QVBoxLayout()
        lay_fam.setSpacing(0)
        lay_fam.addWidget(lbl_fio)
        lay_fam.addWidget(self.__edt_fio)
        vbox.addLayout(lay_fam)

        lay_phone = QVBoxLayout()
        lay_phone.setSpacing(0)
        lay_phone.addWidget(lbl_phone)
        lay_phone.addWidget(self.__edt_phone)

        lay_email = QVBoxLayout()
        lay_email.setSpacing(0)
        lay_email.addWidget(lbl_email)
        lay_email.addWidget(self.__edt_email)

        lay_phone_email = QHBoxLayout()
        lay_phone_email.addLayout(lay_phone)
        lay_phone_email.addLayout(lay_email)
        vbox.addLayout(lay_phone_email)

        lay_comment = QVBoxLayout()
        lay_comment.setSpacing(0)
        lay_comment.addWidget(lbl_comment)
        lay_comment.addWidget(self.__edt_comment)
        vbox.addLayout(lay_comment)

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(btn_ok)
        hbox.addWidget(btn_cancel)
        vbox.addLayout(hbox)

        btn_cancel.clicked.connect(self.reject)
        btn_ok.clicked.connect(self.finish)

    @property
    def fio(self):
        result = self.__edt_fio.text().strip()
        return None if result == "" else result

    @fio.setter
    def fio(self, value: str):
        self.__edt_fio.setText(value)

    @property
    def phone(self):
        result = self.__edt_phone.text().strip()
        return None if result == "" else result

    @phone.setter
    def phone(self, value: str):
        self.__edt_phone.setText(value)

    @property
    def email(self):
        result = self.__edt_email.text().strip()
        return None if result == "" else result

    @email.setter
    def email(self, value: str):
        self.__edt_email.setText(value)

    @property
    def comment(self):
        result = self.__edt_comment.toPlainText().strip()
        return None if result == "" else result

    @comment.setter
    def comment(self, value: str):
        self.__edt_comment.setPlainText(value)

    @pyqtSlot()
    def finish(self):
        if self.fio is None:
            return
        self.accept()
