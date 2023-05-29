from PyQt6.QtWidgets import QTableView, QMessageBox
from PyQt6.QtCore import pyqtSlot
from models.teacher_model import TeacherModel
from ui.dialogs.teacher_dialog import TeacherDialog


class TeachersView(QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)
        model = TeacherModel(parent=self)
        self.setModel(model)

    @pyqtSlot()
    def add(self):
        dlg = TeacherDialog(parent=self)
        dlg.exec()
        #QMessageBox.information(self, "Учитель", "Добавление")

    @pyqtSlot()
    def update(self):
        QMessageBox.information(self, "Учитель", "Редактирование")

    @pyqtSlot()
    def delete(self):
        QMessageBox.information(self, "Учитель", "Удаление")
