from PyQt6.QtSql import QSqlQueryModel, QSqlQuery
#from db.connection import ConnectionNative, Connection
#import psycopg


SELECT_BY_ID = """
   SELECT f_fio, f_phone, f_email, f_comment 
   FROM teacher
   WHERE id=? ; 
"""

INSERT = """
    INSERT INTO teacher (f_fio, f_phone, f_email, f_comment) 
    VALUES(?, ?, ?, ?);
"""

UPDATE = """
    UPDATE teacher SET f_fio=?, f_phone=?, f_email=?, f_comment=? 
    WHERE id=? ;
"""

DELETE = """
    DELETE FROM teacher WHERE id=? ;
"""


class TeacherModel(QSqlQueryModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.refresh()

    def refresh(self):
        sql = "SELECT id, f_fio, f_phone, f_email, f_comment FROM teacher;"
        self.setQuery(sql)

    def select(self, rid: int) -> tuple:
        query = QSqlQuery()
        query.prepare(SELECT_BY_ID)
        query.addBindValue(rid)
        query.exec()
        if query.first():
            result = (query.value("f_fio"), query.value("f_phone"),
                      query.value("f_email"), query.value("f_comment"),)
        else:
            result = (None, None, None, None,)
        return result

    def add(self, fio, phone, email, comment):
        query = QSqlQuery()
        query.prepare(INSERT)
        query.addBindValue(fio)
        query.addBindValue(phone)
        query.addBindValue(email)
        query.addBindValue(comment)
        query.exec()
        self.refresh()

    def update(self, rid: int, fio: str, phone: str, email: str, comment: str):
        query = QSqlQuery()
        query.prepare(UPDATE)
        query.addBindValue(fio)
        query.addBindValue(phone)
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





