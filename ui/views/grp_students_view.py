from PyQt6.QtWidgets import QTableView
from PyQt6.QtCore import pyqtSlot
from models.grp_students_model import GrpStudentsModel


class GrpStudentsView(QTableView):

    def __init__(self, parent=None):
        super().__init__(parent)
        model = GrpStudentsModel(parent=self)
        self.setModel(model)

    @pyqtSlot(int)
    def select_group(self, group_id=None):
        self.model().refill(group_id)