from PyQt6.QtWidgets import QTableView
from PyQt6.QtCore import pyqtSlot
from models.grp_students_model import GrpStudentsModel
from ui.dialogs.old_dialog import OldDialog


class GrpStudentsView(QTableView):

    def __init__(self, parent=None):
        super().__init__(parent)
        model = GrpStudentsModel(parent=self)
        self.setModel(model)

    @pyqtSlot(int)
    def select_group(self, group_id=None):
        self.model().refill(group_id)

    @pyqtSlot()
    def add_old_student(self):
        group_id = self.model().group_id
        if group_id is None:
            return
        dlg = OldDialog(group_id, parent=self)
        if dlg.exec():
            print(dlg.selected_ids)

