import typing
from PyQt6.QtCore import QAbstractTableModel, QModelIndex, Qt, pyqtSlot
from PyQt6.QtSql import QSqlQuery
from db.connection import ConnectionPool
from db.student import Student
import logging
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)


SELECT_ALL = """
 select vs.pk, vs.f_fio, vs.f_comment  
        from student_group sg
        inner join v_student vs on vs.pk  = sg.student_id  
        where sg.group_id  = ? ;
"""


class GrpStudentsModel(QAbstractTableModel):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__students = []
        self.__group_id = None
        self.refill()

    @property
    def group_id(self):
        return self.__group_id

    def rowCount(self, parent_index: QModelIndex = ...) -> int:
        if parent_index.isValid():
            return 0
        return len(self.__students)

    def columnCount(self, parent_index: QModelIndex = ...) -> int:
        return 0 if parent_index.isValid() else 2

    def data(self, index: QModelIndex, role: int = ...) -> typing.Any:
        if role == Qt.ItemDataRole.DisplayRole:
            r = index.row()
            c = index.column()
            if c == 0:
                return self.__students[r].fio
            elif c == 1:
                return self.__students[r].comment
            else:
                return f"{r=}, {c=}"
        else:
            return None

    @pyqtSlot(int)
    def refill(self, group_id=None):
        self.beginResetModel()
        self.__group_id = group_id
        try:
            self.__students.clear()
            if group_id is None:
                self.endResetModel()
                return
            self.__get_students(group_id)
        finally:
            self.endResetModel()

    def __get_students(self, group_id):
        conn = ConnectionPool.get_root_connection()
        query = QSqlQuery(db=conn)
        query.prepare(SELECT_ALL)
        query.addBindValue(group_id)
        if query.exec():
            while query.next():
                data = Student(pk=query.value("pk"), fio=query.value("f_fio"), comment=query.value("f_comment"))
                self.__students.append(data)
        else:
            LOG.info(query.lastError().text())



