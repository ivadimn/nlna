from PyQt6.QtWidgets import QTableView
from PyQt6.QtCore import pyqtSlot
from models.st_groups_model import StGroupsModel


class StGroupsView(QTableView):

    def __init__(self, parent=None):
        super().__init__(parent)
        model = StGroupsModel(self)
        self.setModel(model)

    @pyqtSlot(int)
    def select_student(self, student_id=None):
        self.model().refill(student_id)