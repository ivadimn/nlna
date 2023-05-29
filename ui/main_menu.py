from PyQt6.QtWidgets import QMenuBar


class MainMenu(QMenuBar):

    def __init__(self, parent=None):
        super().__init__(parent)

        nsi_menu = self.addMenu("Учителя")
        self.__teacher_add = nsi_menu.addAction("Добавить...")
        self.__teacher_update = nsi_menu.addAction("Редактировать...")
        self.__teacher_delete = nsi_menu.addAction("Удалить...")

        help_menu = self.addMenu("Справка")
        self.__about = help_menu.addAction("О программе...")
        self.__about_qt = help_menu.addAction("О библиотеке Qt...")

    @property
    def teacher_add(self):
        return self.__teacher_add

    @property
    def teacher_update(self):
        return self.__teacher_update

    @property
    def teacher_delete(self):
        return self.__teacher_delete

    @property
    def about(self):
        return self.__about

    @property
    def about_qt(self):
        return self.__about_qt
