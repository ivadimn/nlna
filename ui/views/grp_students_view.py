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
        dlg = OldDialog(parent=self)
        dlg.exec()

