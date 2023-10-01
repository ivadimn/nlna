from PyQt6.QtWidgets import QTableView
from models.stgroups_model import StgroupsModel


class StgroupsView(QTableView):

    def __init__(self, parent=None):
        super().__init__(parent)
        model = StgroupsModel(parent=self)
        self.setModel(model)

