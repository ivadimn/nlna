from PyQt6.QtWidgets import (
    QApplication,
    QDockWidget,
    QFrame,
    QMainWindow,
    QMessageBox)
from PyQt6.QtGui import QImage
from PyQt6.QtCore import pyqtSlot, Qt
from ui.main_menu import MainMenu
from ui.views.teachers_view import TeachersView
from ui.views.student_view import StudentView
from ui.views.group_view import GroupView
from ui.dialogs.login_dialog import LoginDialog
from ui.dialogs.change_password import ChangePassword
from datetime import datetime
from db.connection import get_user_info, update_password, ConnectionPool
from utils import password_hash, check_password
from ui.views.grp_students_view import GrpStudentsView
from PyQt6.uic import loadUi


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(100, 100, 1000, 500)

        main_menu = MainMenu(parent=self)
        self.setMenuBar(main_menu)

        main_menu.about_qt.triggered.connect(self.about_qt)
        main_menu.about.triggered.connect(self.about)
        main_menu.teacher_mode_request.connect(self.teacher_mode_on)
        main_menu.student_mode_request.connect(self.student_mode_on)
        main_menu.group_mode_request.connect(self.group_mode_on)

        if not self.authorize():
            main_menu.lock()

    @property
    def all_docks(self):
        return [x for x in self.children() if isinstance(x, QDockWidget)]

    def authorize(self) -> bool:
        dlg = LoginDialog(self)
        if not dlg.exec():
            return False
        user_info = get_user_info(dlg.login)
        if not user_info:
            return False
        if not user_info["enabled"]:
            return False
        if not user_info["expire"].isNull:
            if user_info["expire"] < datetime.now():
                return False
        if (user_info["password_hash"] is None or len(user_info["password_hash"]) == 0) and (dlg.password is None):
            dlg_change = ChangePassword(self)
            if not dlg_change.exec():
                return False
            user_info["password_hash"] = password_hash(dlg_change.password1, user_info["salt"])
            update_password(user_info)
        else:
            if not check_password(dlg.password, user_info["password_hash"], user_info["salt"]):
                return False
        QApplication.instance().set_authorized(user_info["login"], user_info["role"])
        #ConnectionPool.new_connection(user_info["login"], dlg.password)
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
        if not self.mode_off(atype=TeachersView):
            return
        view = TeachersView(parent=self)
        self.setCentralWidget(view)
        self.menuBar().set_teacher_mode(view)

    @pyqtSlot()
    def student_mode_on(self):
        if not self.mode_off(atype=StudentView):
            return
        view = StudentView(parent=self)
        self.setCentralWidget(view)

        dock_title = QApplication.translate("MainWindow", "Groups")
        dock_widget = QDockWidget(dock_title, parent=self)
        dock_frame = QFrame(parent=dock_widget)
        dock_frame.setStyleSheet("background: green")
        dock_widget.setWidget(dock_frame)

        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock_widget)
        self.menuBar().set_student_mode(view, [dock_widget])

    @pyqtSlot()
    def group_mode_on(self):
        if not self.mode_off(atype=GroupView):
            return
        view = GroupView(parent=self)
        self.setCentralWidget(view)        # меняем центральный виджет

        dock_title = QApplication.translate("MainWindow", "Students")
        dock_widget = QDockWidget(dock_title, parent=self)
        docked_window = GrpStudentsView(parent=dock_widget)
        dock_widget.setWidget(docked_window)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock_widget)

        view.group_selected.connect(docked_window.select_group)
        self.menuBar().set_group_mode(view, [dock_widget])

    def mode_off(self, atype=None) -> bool:
        old = self.centralWidget()
        if old is None:
            return True
        if isinstance(old, atype):
            return False
        # запросить пользователя о допустимости выключения режима
        self.setCentralWidget(None)
        old.deleteLater()
        for w in self.all_docks:
            w.deleteLater()
        return True

