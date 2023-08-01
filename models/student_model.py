from PyQt6.QtSql import QSqlQueryModel, QSqlQuery
from db.connection import ConnectionPool


SELECT_BY_ID = """
   SELECT f_fio, f_email, f_comment 
   FROM student
   WHERE id=? ; 
"""

INSERT = """
    INSERT INTO student (f_fio, f_email, f_comment) 
    VALUES(?, ?, ?);
"""

UPDATE = """
    UPDATE student SET f_fio=?, f_email=?, f_comment=? 
    WHERE id=? ;
"""

DELETE = """
    DELETE FROM student WHERE id=? ;
"""


class StudentModel(QSqlQueryModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__db = ConnectionPool.get_admin_connection()
        self.refresh()

    def refresh(self):
        sql = "SELECT id, f_fio, f_email, f_comment FROM student;"
        self.setQuery(sql, db=self.__db)

    def select(self, rid: int) -> tuple:
        query = QSqlQuery(db=self.__db)
        query.prepare(SELECT_BY_ID)
        query.addBindValue(rid)
        query.exec()
        if query.first():
            result = (query.value("f_fio"), query.value("f_email"), query.value("f_comment"),)
        else:
            result = (None, None, None)
        return result

    def add(self, fio, email, comment):
        query = QSqlQuery()
        query.prepare(INSERT)
        query.addBindValue(fio)
        query.addBindValue(email)
        query.addBindValue(comment)
        query.exec()
        self.refresh()

    def update(self, rid: int, fio: str, email: str, comment: str):
        query = QSqlQuery()
        query.prepare(UPDATE)
        query.addBindValue(fio)
        query.addBindValue(email)
        query.addBindValue(comment)
        query.addBindValue(rid)
        query.exec()
        self.refresh()

    def delete(self, rid: int):
        query = QSqlQuery()
        query.prepare(DELETE)
        query.addBindValue(rid)
        query.exec()
        self.refresh()
