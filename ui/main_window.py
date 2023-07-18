from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtCore import pyqtSlot
from ui.main_menu import MainMenu
from ui.views.teachers_view import TeachersView
from ui.views.student_view import StudentView
from ui.views.group_view import GroupView
from ui.dialogs.login_dialog import LoginDialog
from ui.dialogs.change_password import ChangePassword
from datetime import datetime
from db.connection import get_user_info
from utils import password_hash


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(300, 300, 1000, 500)

        main_menu = MainMenu(parent=self)
        self.setMenuBar(main_menu)

        main_menu.about_qt.triggered.connect(self.about_qt)
        main_menu.about.triggered.connect(self.about)
        main_menu.teacher_mode_request.connect(self.teacher_mode_on)
        main_menu.student_mode_request.connect(self.student_mode_on)
        main_menu.group_mode_request.connect(self.group_mode_on)

        allowed_flag = False
        if not self.authorize():
            main_menu.lock()

    def authorize(self) -> bool:
        dlg = LoginDialog(self)
        if not dlg.exec():
            return False
        user_info = get_user_info(dlg.login)
        if not user_info:
            return False
        if not user_info["enabled"]:
            return False
        if user_info["expire"] is not None:
            if user_info["expire"] < datetime.now():
                return False
        if user_info["password_hash"] is None:
            dlg = ChangePassword(self)
            if not dlg.exec():
                return False
            user_info["password_hash"] = password_hash(dlg.password1, user_info["salt"])
        else:
            print("Проверить пароль")
        print(user_info)
        return True




    @pyqtSlot()
    def about(self):
        title = "Управление заданиями для учащихся"
        text = ("Программа для управления задачами\n" +
                "и заданиями для учащихся школ.")
        QMessageBox.about(self, title, text)

    @pyqtSlot()
    def about_qt(self):
        QMessageBox.aboutQt(self, "Управление заданиями для учащихся")

    @pyqtSlot()
    def teacher_mode_on(self):
        old_view = self.centralWidget()
        view = TeachersView(parent=self)
        self.setCentralWidget(view)
        self.menuBar().set_teacher_mode(view)
        print("Teacher mode on")
        if old_view is not None:
            old_view.deleteLater()

    @pyqtSlot()
    def student_mode_on(self):
        old_view = self.centralWidget()
        view = StudentView(parent=self)
        self.setCentralWidget(view)
        self.menuBar().set_student_mode(view)
        if old_view is not None:
            old_view.deleteLater()

    @pyqtSlot()
    def group_mode_on(self):
        old_view = self.centralWidget()
        view = GroupView(parent=self)
        self.setCentralWidget(view)
        self.menuBar().set_group_mode(view)
        if old_view is not None:
            old_view.deleteLater()