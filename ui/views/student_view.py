from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import pyqtSlot
from models.student_model import StudentModel
from ui.dialogs.student_dialog import StudentDialog
from ui.views.view import View


class StudentView(View):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.model = StudentModel()
        self.setModel(self.model)

        hh = self.horizontalHeader()
        hh.setSectionResizeMode(3, hh.ResizeMode.Stretch)

    @pyqtSlot()
    def add(self):
        dlg = StudentDialog(parent=self)
        if dlg.exec():
            self.model.add(dlg.fio, dlg.email, dlg.comment)

    @pyqtSlot()
    def update(self):
        dlg = StudentDialog(parent=self)
        row = self.currentIndex().row()
        rid = self.model.record(row).value(0)
        (dlg.fio, dlg.email, dlg.comment) = self.model.select(rid)
        if dlg.exec():
            self.model.update(rid, dlg.fio, dlg.email, dlg.comment)

    @pyqtSlot()
    def delete(self):
        row = self.currentIndex().row()
        rid = self.model.record(row).value(0)
        ans = QMessageBox.question(self, "Удаление записи", "Вы уверены, что хотите удалить запись?")
        if ans == QMessageBox.StandardButton.Yes:
            self.model.delete(rid)