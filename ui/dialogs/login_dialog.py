from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton
from PyQt6.QtCore import pyqtSlot
from settings import global_salt
from hashlib import sha1, md5


class LoginDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        vbox = QVBoxLayout(self)

        login_lay = QVBoxLayout()
        login_lay.setSpacing(0)
        lbl_login = QLabel("Имя пользователя:", parent=self)
        self.__edt_login = QLineEdit(parent=self)
        login_lay.addWidget(lbl_login)
        login_lay.addWidget(self.__edt_login)
        vbox.addLayout(login_lay)

        passwd_lay = QVBoxLayout()
        passwd_lay.setSpacing(0)
        lbl_passwd = QLabel("Пароль:", parent=self)
        self.__edt_passwd = QLineEdit(parent=self)
        self.__edt_passwd.setEchoMode(QLineEdit.EchoMode.Password)
        passwd_lay.addWidget(lbl_passwd)
        passwd_lay.addWidget(self.__edt_passwd)
        vbox.addLayout(passwd_lay)

        lay_buttons = QHBoxLayout()
        btn_yes = QPushButton("Ок", parent=self)
        btn_no = QPushButton("Отменить", parent=self)
        lay_buttons.addStretch()
        lay_buttons.addWidget(btn_no)
        lay_buttons.addWidget(btn_yes)
        vbox.addLayout(lay_buttons)

        btn_yes.clicked.connect(self.finish)
        btn_no.clicked.connect(self.reject)

    @property
    def login(self):
        result = self.__edt_login.text().strip()
        return None if result == "" else result

    @property
    def password(self):
        result = self.__edt_passwd.text().strip()
        return None if result == "" else result

    def finish(self):
        if self.login is None:
            return
        self.accept()




#data = "ивановвадимниколаевич21.06.19653d2cb093-f1b9-4a8d-b8ec-f15ada921033"
#print(md5(data.encode("UTF-8")).hexdigest())
a : str  = "qqq"
print(len(a))