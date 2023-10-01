from PyQt6.QtWidgets import QApplication, QMenu, QDockWidget


class ViewMenu(QMenu):

    def __init__(self, parent=None):
        title = QApplication.translate("MainMenu.ViewMenu", "View")
        super().__init__(title=title, parent=parent)

        title = QApplication.translate("MainMenu.ViewMenu", "Windows")
        self.__windows_menu = self.addMenu(title)

        title = QApplication.translate("MainMenu.ViewMenu", "Tool bars")
        self.__toolbars_menu = self.addMenu(title)

    def add_window(self, dock_widget: QDockWidget):
        self.__windows_menu.addAction(dock_widget.toggleViewAction())
        print("dock_widget added!!")
