from PyQt6.QtWidgets import QTableView, QMessageBox
from PyQt6.QtCore import pyqtSlot
from models.student_model import StudentModel
from ui.dialogs.student_dialog import StudentDialog


class StudentView(QTableView):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.model = StudentModel()
        self.setModel(self.model)

        self.setSelectionBehavior(self.SelectionBehavior.SelectRows)
        self.setSelectionMode(self.SelectionMode.SingleSelection)
        self.hideColumn(0)
        self.setWordWrap(False)

        vh = self.verticalHeader()
        vh.setSectionResizeMode(vh.ResizeMode.Fixed)

        hh = self.horizontalHeader()
        hh.setSectionResizeMode(hh.ResizeMode.ResizeToContents)
        hh.setSectionResizeMode(4, hh.ResizeMode.Stretch)

    @pyqtSlot()
    def add(self):
        dlg = StudentDialog(parent=self)
        if dlg.exec():
            self.model.add(dlg.fio, dlg.phone, dlg.email, dlg.comment)

    @pyqtSlot()
    def update(self):
        dlg = StudentDialog(parent=self)
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