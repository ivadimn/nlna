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

        self.__selected_rows = set()
        self.__selected_ids = set()

        self.setQuery(query)

    @property
    def selected_ids(self):
        return self.__selected_ids

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        fl = super().flags(index)
        if index.column() == 1:
            fl |= Qt.ItemFlag.ItemIsUserCheckable
        return fl

    def data(self, item: QModelIndex, role: int = ...) -> typing.Any:
        if role == Qt.ItemDataRole.UserRole:
            return self.query().value(0)
        elif role == Qt.ItemDataRole.CheckStateRole:
            if item.column() != 1:
                return super().data(item, role)
            else:
                #pk = item.data(Qt.ItemDataRole.UserRole + 0)
                row = item.row()
                #print("func data", row, self.__selected_ids)
                if row in self.__selected_rows:
                    return Qt.CheckState.Checked
                else:
                    return Qt.CheckState.Unchecked
        else:
            return super().data(item, role)

    def setData(self, index: QModelIndex, value: typing.Any, role: int = ...) -> bool:
        if role != Qt.ItemDataRole.CheckStateRole or index.column() != 1:
            return super().setData(index, value, role)
        student_id = index.data(Qt.ItemDataRole.UserRole + 0)
        row = index.row()
        self.beginResetModel()
        try:

            if value == 0: #Qt.CheckState.Unchecked:
                self.__selected_ids.remove(student_id)
                self.__selected_rows.remove(row)
            else:
                self.__selected_ids.add(student_id)
                self.__selected_rows.add(row)
            print(row, value, self.__selected_ids, self.__selected_rows)
        finally:
            self.endResetModel()
        return True


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
        self.__view = _View(group_id, parent=self)
        lay.addWidget(self.__view)

        btn = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok
                               | QDialogButtonBox.StandardButton.Cancel, parent=self)
        lay.addWidget(btn)

        btn.accepted.connect(self.accept)
        btn.rejected.connect(self.reject)

    @property
    def selected_ids(self):
        return self.__view.model().selected_ids
