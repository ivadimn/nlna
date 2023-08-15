from PyQt6.QtWidgets import QDialog
from PyQt6.QtWidgets import QLabel, QLineEdit, QTextEdit, QPushButton
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QFrame
from PyQt6.QtCore import pyqtSlot
from .ui_student_form import Ui_StudentForm
from db.student import Student


class _Frame(QFrame):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_StudentForm()
        self.ui.setupUi(self)


class StudentDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Студент")
        self.__frame = _Frame(self)


        btn_ok = QPushButton("Ok", parent=self)
        btn_cancel = QPushButton("Отмена", parent=self)

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.__frame)

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(btn_ok)
        hbox.addWidget(btn_cancel)
        vbox.addLayout(hbox)

        btn_cancel.clicked.connect(self.reject)
        btn_ok.clicked.connect(self.finish)

    @property
    def login(self):
        result = self.__frame.ui.edt_login.text().strip()
        return None if result == "" else result

    @login.setter
    def login(self, value):
        self.__frame.ui.edt_login.setText(value)


    @property
    def fio(self):
        result = self.__frame.ui.edt_fio.text().strip()
        return None if result == "" else result

    @fio.setter
    def fio(self, value: str):
        self.__frame.ui.edt_fio.setText(value)

    @property
    def email(self):
        result = self.__frame.ui.edt_email.text().strip()
        return None if result == "" else result

    @email.setter
    def email(self, value: str):
        self.__frame.ui.edt_email.setText(value)

    @property
    def comment(self):
        result = self.__frame.ui.edt_comment.toPlainText().strip()
        return None if result == "" else result

    @comment.setter
    def comment(self, value: str):
        self.__frame.ui.edt_comment.setPlainText(value)

    @pyqtSlot()
    def finish(self):
        if self.fio is None:
            return
        self.accept()

    def get(self, data: Student):
        data.login = self.login
        data.fio = self.fio
        data.email = self.email
        data.comment = self.comment

    def put(self, data: Student, *, for_update=False):
        self.login = data.login
        self.fio = data.fio
        self.email = data.email
        self.comment = data.comment
        self.__frame.ui.edt_login.setReadOnly(for_update)
