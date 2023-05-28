from PyQt6.QtSql import QSqlQueryModel


class TeacherModel(QSqlQueryModel):
    def __init__(self, parent=None):
        super().__init__(parent)