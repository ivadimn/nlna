import typing
from PyQt6.QtCore import QAbstractTableModel, QModelIndex, Qt


class StgroupsModel(QAbstractTableModel):

    def __init__(self, parent=None):
        super().__init__(parent)

    def rowCount(self, parent_index: QModelIndex = ...) -> int:
        if parent_index.isValid():
            return 0
        return 10

    def columnCount(self, parent_index: QModelIndex = ...) -> int:
        return 0 if parent_index.isValid() else 1

    def data(self, index: QModelIndex, role: int = ...) -> typing.Any:
        if role == Qt.ItemDataRole.DisplayRole:
            r = index.row()
            c = index.column()
            return f"{r=}, {c=}"
        else:
            return None

    #def refill(self):



