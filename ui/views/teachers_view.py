from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import pyqtSlot
from models.teacher_model import TeacherModel
from ui.dialogs.teacher_dialog import TeacherDialog
from ui.views.view import View
from db.teacher import Teacher


class TeachersView(View):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.model = TeacherModel(parent=self)
        self.setModel(self.model)

        self.hideColumn(0)
        hh = self.horizontalHeader()
        hh.setSectionResizeMode(4, hh.ResizeMode.Stretch)

    @property
    def pk(self):
        row = self.currentIndex().row()
        return self.model.record(row).value(0)

    @pyqtSlot()
    def add(self):
        dlg = TeacherDialog(parent=self)
        if dlg.exec():
            data = Teacher()
            dlg.get(data)
            data.insert()
            self.model.refresh()

    @pyqtSlot()
    def update(self):
        dlg = TeacherDialog(parent=self)
        data = Teacher(pk=self.pk).load()
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


