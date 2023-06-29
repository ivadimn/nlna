from PyQt6.QtWidgets import QTableView, QMessageBox
from PyQt6.QtCore import pyqtSlot
from models.teacher_model import TeacherModel
from ui.dialogs.teacher_dialog import TeacherDialog


class TeachersView(QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.model = TeacherModel(parent=self)
        self.setModel(self.model)

    @pyqtSlot()
    def add(self):
        dlg = TeacherDialog(parent=self)
        if dlg.exec():
            self.model.add(dlg.fio, dlg.phone, dlg.email, dlg.comment)

    @pyqtSlot()
    def update(self):
        dlg = TeacherDialog(parent=self)
        row = self.currentIndex().row()
        rid = self.model.record(row).value(0)
        (dlg.fio, dlg.phone, dlg.email, dlg.comment) = self.model.select(rid)
        if dlg.exec():
            self.model.update(rid, dlg.fio, dlg.phone, dlg.email, dlg.comment)



    @pyqtSlot()
    def delete(self):
        row = self.currentIndex().row()
        rid = self.model.record(row).value(0)
        ans = QMessageBox.question(self, "Удаление записи", "Вы уверены, что хотите удалить запись?")
        if ans == QMessageBox.StandardButton.Yes:
            self.model.delete(rid)


