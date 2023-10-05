from PyQt6.QtWidgets import QDialog, QTableView, QDialogButtonBox, QVBoxLayout
from PyQt6.QtSql import QSqlQueryModel
from PyQt6.QtCore import Qt


class _View(QTableView):

    def __init__(self, parent=None):
        super().__init__(parent)


class OldDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        lay = QVBoxLayout(self)
        view = _View(parent=self)
        lay.addWidget(view)

        btn = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok
                               | QDialogButtonBox.StandardButton.Cancel, parent=self)
        lay.addWidget(btn)

        btn.accepted.connect(self.accept)
        btn.rejected.connect(self.reject)
