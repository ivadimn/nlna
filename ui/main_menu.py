from PyQt6.QtGui import QActionGroup
from PyQt6.QtWidgets import QMenuBar, QDockWidget
from PyQt6.QtCore import pyqtSlot, pyqtSignal

from ui.views.view import View
from ui.view_menu import ViewMenu


class MainMenu(QMenuBar):

    teacher_mode_request = pyqtSignal()
    student_mode_request = pyqtSignal()
    group_mode_request = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        teacher_menu = self.addMenu("Учителя")
        self.__teacher_menu_action = teacher_menu.menuAction()
        self.__teacher_add = teacher_menu.addAction("Добавить...")
        self.__teacher_update = teacher_menu.addAction("Редактировать...")
        self.__teacher_delete = teacher_menu.addAction("Удалить...")

        student_menu = self.addMenu("Студенты")
        self.__student_menu_action = student_menu.menuAction()
        self.__student_add = student_menu.addAction("Добавить...")
        self.__student_update = student_menu.addAction("Редактировать...")
        self.__student_delete = student_menu.addAction("Удалить...")

        group_menu = self.addMenu("Группы")
        self.__group_menu_action = group_menu.menuAction()
        self.__group_add = group_menu.addAction("Добавить...")
        self.__group_update = group_menu.addAction("Редактировать...")
        self.__group_delete = group_menu.addAction("Удалить...")

        mode_menu = menu = self.addMenu("Режимы")
        mode_action_group = ag = QActionGroup(self)
        self.__mode_menu_action = menu.menuAction()

        self.__teacher_mode_action = act = menu.addAction("Учителя")
        act.setCheckable(True)
        act.toggled.connect(self.toggle_teacher_mode)
        ag.addAction(act)

        self.__student_mode_action = act = menu.addAction("Студенты")
        act.setCheckable(True)
        act.toggled.connect(self.toggle_student_mode)
        ag.addAction(act)

        self.__group_mode_action = act = menu.addAction("Группы")
        act.setCheckable(True)
        act.toggled.connect(self.toggle_group_mode)
        ag.addAction(act)

        self.__view_menu = vm = ViewMenu(parent=self)
        self.addMenu(vm)

        help_menu = self.addMenu("Справка")
        self.__about = help_menu.addAction("О программе...")
        self.__about_qt = help_menu.addAction("О библиотеке Qt...")

        self.toggle_teacher_mode(False)
        self.toggle_student_mode(False)
        self.toggle_group_mode(False)

    def lock(self):
        self.__mode_menu_action.setEnabled(False)

    @pyqtSlot(bool)
    def toggle_teacher_mode(self, enable: bool):
        if not enable:
            self.__teacher_menu_action.setVisible(False)
            self.__teacher_menu_action.setEnabled(False)
            self.__teacher_add.setEnabled(False)
            self.__teacher_update.setEnabled(False)
            self.__teacher_delete.setEnabled(False)
        else:
            self.teacher_mode_request.emit()

    @pyqtSlot(bool)
    def toggle_student_mode(self, enable: bool):
        if not enable:
            self.__student_menu_action.setVisible(False)
            self.__student_menu_action.setEnabled(False)
            self.__student_add.setEnabled(False)
            self.__student_update.setEnabled(False)
            self.__student_delete.setEnabled(False)
        else:
            self.student_mode_request.emit()

    @pyqtSlot(bool)
    def toggle_group_mode(self, enable: bool):
        if not enable:
            self.__group_menu_action.setVisible(False)
            self.__group_menu_action.setEnabled(False)
            self.__group_add.setEnabled(False)
            self.__group_update.setEnabled(False)
            self.__group_delete.setEnabled(False)
        else:
            self.group_mode_request.emit()

    def set_group_mode(self, view: View, dock_widgets=[]):
        self.__group_add.triggered.connect(view.add)
        self.__group_update.triggered.connect(view.update)
        self.__group_delete.triggered.connect(view.delete)

        self.__group_menu_action.setVisible(True)
        self.__group_menu_action.setEnabled(True)
        self.__group_add.setEnabled(True)
        self.__group_update.setEnabled(True)
        self.__group_delete.setEnabled(True)

        for wid in dock_widgets:
            self.__view_menu.add_window(wid)

    def set_teacher_mode(self, view: View):
        self.__teacher_add.triggered.connect(view.add)
        self.__teacher_update.triggered.connect(view.update)
        self.__teacher_delete.triggered.connect(view.delete)

        self.__teacher_menu_action.setVisible(True)
        self.__teacher_menu_action.setEnabled(True)
        self.__teacher_add.setEnabled(True)
        self.__teacher_update.setEnabled(True)
        self.__teacher_delete.setEnabled(True)

    def set_student_mode(self, view: View, dock_widgets=[]):
        self.__student_add.triggered.connect(view.add)
        self.__student_update.triggered.connect(view.update)
        self.__student_delete.triggered.connect(view.delete)

        self.__student_menu_action.setVisible(True)
        self.__student_menu_action.setEnabled(True)
        self.__student_add.setEnabled(True)
        self.__student_update.setEnabled(True)
        self.__student_delete.setEnabled(True)

        for wid in dock_widgets:
            self.__view_menu.add_window(wid)

    def disable_all_modes(self):
        self.__teacher_menu_action.setVisible(False)
        self.__teacher_menu_action.setEnabled(False)
        self.__teacher_add.setEnabled(False)
        self.__teacher_update.setEnabled(False)
        self.__teacher_delete.setEnabled(False)

        self.__student_menu_action.setVisible(False)
        self.__student_menu_action.setEnabled(False)
        self.__student_add.setEnabled(False)
        self.__student_update.setEnabled(False)
        self.__student_delete.setEnabled(False)

        self.__group_menu_action.setVisible(False)
        self.__group_menu_action.setEnabled(False)
        self.__group_add.setEnabled(False)
        self.__group_update.setEnabled(False)
        self.__group_delete.setEnabled(False)

    @property
    def about(self):
        return self.__about

    @property
    def about_qt(self):
        return self.__about
