from PyQt6.QtSql import QSqlQueryModel


class TeacherModel(QSqlQueryModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.refresh()

    def refresh(self):
        sql = "SELECT id, f_fio, f_phone, f_email, f_comment FROM teacher;"
        self.setQuery(sql)

    #def add(self, fio, phone, email, comment):
