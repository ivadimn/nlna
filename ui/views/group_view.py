from PyQt6.QtWidgets import QTableView, QMessageBox
from PyQt6.QtCore import pyqtSlot
from models.group_model import GroupModel
from ui.dialogs.group_dialog import GroupDialog
from ui.views.view import View


class GroupView(View):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.model = GroupModel()
        self.setModel(self.model)

        hh = self.horizontalHeader()
        hh.setSectionResizeMode(2, hh.ResizeMode.Stretch)

    @pyqtSlot()
    def add(self):
        dlg = GroupDialog(parent=self)
        if dlg.exec():
            self.model.add(dlg.title, dlg.comment)

    @pyqtSlot()
    def update(self):
        dlg = GroupDialog(parent=self)
        row = self.currentIndex().row()
        rid = self.model.record(row).value(0)
        (dlg.title, dlg.comment,) = self.model.select(rid)
        if dlg.exec():
            self.model.update(rid, dlg.title, dlg.comment)

    @pyqtSlot()
    def delete(self):
        row = self.currentIndex().row()
        rid = self.model.record(row).value(0)
        ans = QMessageBox.question(self, "Удаление записи", "Вы уверены, что хотите удалить запись?")
        if ans == QMessageBox.StandardButton.Yes:
            self.model.delete(rid)
