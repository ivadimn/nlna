import typing
from PyQt6.QtCore import QAbstractTableModel
from PyQt6.QtSql import QSqlQuery
from PyQt6.QtCore import QModelIndex, Qt
from db.connection import ConnectionPool
import logging
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)


SELECT_ALL = """
    select s.id as pk, s.f_title  
        from student_group sg 
        inner join stgroup s on s.id = sg.group_id 
        where sg.student_id = ? ;
"""


class StGroupsModel(QAbstractTableModel):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__groups = []

    def refill(self, student_id=None):
        self.beginResetModel()
        try:
            self.__groups.clear()
            if student_id is None:
                self.endResetModel()
                return
            self.__get_groups(student_id)
        finally:
            self.endResetModel()

    def rowCount(self, parent_index: QModelIndex = ...) -> int:
        if parent_index.isValid():
            return 0
        return len(self.__groups)

    def columnCount(self, parent_index: QModelIndex = ...) -> int:
        return 0 if parent_index.isValid() else 1

    def data(self, index: QModelIndex, role: int = ...) -> typing.Any:
        if role == Qt.ItemDataRole.DisplayRole:
            r = index.row()
            c = index.column()
            if c == 0:
                return self.__groups[r][1]
            else:
                return None
        else:
            return None

    def __get_groups(self, student_id):
        conn = ConnectionPool.get_root_connection()
        query = QSqlQuery(db=conn)
        query.prepare(SELECT_ALL)
        query.addBindValue(student_id)
        if query.exec():
            while query.next():
                data = (query.value("pk"), query.value("f_title"), )
                self.__groups.append(data)
        else:
            LOG.info(query.lastError().text())
