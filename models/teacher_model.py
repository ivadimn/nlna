from PyQt6.QtSql import QSqlQueryModel, QSqlQuery
from db.connection import ConnectionNative, Connection
import psycopg


INSERT = """
    INSERT INTO teacher (f_fio, f_phone, f_email, f_comment) 
    VALUES(%s, %s, %s, %s);
"""


class TeacherModel(QSqlQueryModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.refresh()

    def refresh(self):
        sql = "SELECT id, f_fio, f_phone, f_email, f_comment FROM teacher;"
        self.setQuery(sql, Connection().connection )

    def add(self, fio, phone, email, comment):
        conn = ConnectionNative().connection
        cursor = conn.cursor()
        data = (fio, phone, email, comment)
        cursor.execute(INSERT, data)
        conn.commit()
        self.refresh()

    def add1(self, fio, phone, email, comment):
        query = QSqlQuery(Connection().connection)
        query.prepare(INSERT)
        query.addBindValue(fio)
        query.addBindValue(phone)
        query.addBindValue(email)
        query.addBindValue(comment)
        query.exec()
        self.refresh()






