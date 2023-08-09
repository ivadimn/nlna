from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import pyqtSlot
from models.student_model import StudentModel
from ui.dialogs.student_dialog import StudentDialog
from ui.views.view import View
from db.student import Student


class StudentView(View):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.model = StudentModel()
        self.setModel(self.model)

        hh = self.horizontalHeader()
        hh.setSectionResizeMode(3, hh.ResizeMode.Stretch)

    @property
    def pk(self):
        row = self.currentIndex().row()
        return self.model.record(row).value(0)

    @pyqtSlot()
    def add(self):
        dlg = StudentDialog(parent=self)
        if dlg.exec():
            data = Student()
            dlg.get(data)
            data.insert()
            self.model.refresh()

    @pyqtSlot()
    def update(self):
        dlg = StudentDialog(parent=self)
        data = Student(pk=self.pk).load()
        dlg.put(data)
        if dlg.exec():
            dlg.get(data)

    @pyqtSlot()
    def delete(self):
        row = self.currentIndex().row()
        rid = self.model.record(row).value(0)
        ans = QMessageBox.question(self, "Удаление записи", "Вы уверены, что хотите удалить запись?")
        if ans == QMessageBox.StandardButton.Yes:
            self.model.delete(rid)