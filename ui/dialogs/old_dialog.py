import typing

from PyQt6.QtWidgets import QDialog, QTableView, QDialogButtonBox, QVBoxLayout
from PyQt6.QtSql import QSqlQueryModel, QSqlQuery
from PyQt6.QtCore import Qt, QModelIndex
from db.connection import ConnectionPool


_SELECT = """
select vs.pk, vs.f_fio  
        from v_student vs
        where vs.pk not in (select student_id from student_group sg where group_id = :GROUP_ID) ;
"""


class _Model(QSqlQueryModel):

    def __init__(self, group_id: int, parent=None):
        super().__init__(parent)
        db = ConnectionPool.get_root_connection()
        query = QSqlQuery(db)
        query.prepare(_SELECT)
        query.bindValue(":GROUP_ID", group_id)
        query.exec()
        self.setQuery(query)

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        fl = super().flags(index)
        if index.column() == 1:
            fl |= Qt.ItemFlag.ItemIsUserCheckable
        return fl

    def data(self, item: QModelIndex, role: int = ...) -> typing.Any:
        if role != Qt.ItemDataRole.CheckStateRole:
            return super().data(item, role)
        return None


class _View(QTableView):

    def __init__(self, group_id: int, parent=None):
        super().__init__(parent)

        self.setModel(_Model(group_id, parent=self))
        hh = self.horizontalHeader()
        hh.setSectionResizeMode(hh.ResizeMode.Stretch)
        self.hideColumn(0)


class OldDialog(QDialog):

    def __init__(self, group_id: int, parent=None):
        super().__init__(parent)

        lay = QVBoxLayout(self)
        view = _View(group_id, parent=self)
        lay.addWidget(view)

        btn = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok
                               | QDialogButtonBox.StandardButton.Cancel, parent=self)
        lay.addWidget(btn)

        btn.accepted.connect(self.accept)
        btn.rejected.connect(self.reject)
