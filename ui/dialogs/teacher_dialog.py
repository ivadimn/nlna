from PyQt6.QtWidgets import QDialog
from PyQt6.QtWidgets import QLabel, QLineEdit, QTextEdit, QPushButton
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout


class TeacherDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

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
        vbox.addWidget(lbl_fio)
        vbox.addWidget(self.__edt_fio)
        vbox.addWidget(lbl_phone)
        vbox.addWidget(self.__edt_phone)
        vbox.addWidget(lbl_email)
        vbox.addWidget(self.__edt_email)
        vbox.addWidget(lbl_comment)
        vbox.addWidget(self.__edt_comment)

        hbox = QHBoxLayout()
        hbox.addWidget(btn_ok)
        hbox.addWidget(btn_cancel)
        vbox.addLayout(hbox)

        btn_cancel.clicked.connect(self.reject)


