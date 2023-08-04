from dataclasses import dataclass
from PyQt6.QtSql import QSqlQuery
from db.connection import ConnectionPool

INSERT_USER = """
    INSERT INTO appuser (f_login, f_salt, f_role)
    VALUES (?, ?, ?)
    returning id ;
"""

INSERT = """
    INSERT INTO teacher (f_fio, f_phone, f_email, f_comment, user_id) 
    VALUES(?, ?, ?, ?, ?);
"""


@dataclass
class Teacher:
    pk: int = None
    login: str = None
    fio: str = None
    phone: str = None
    email: str = None
    comment: str = None
    user_id: int = None

    @property
    def user_data(self):
        return self.login, "1", "teacher"

    @property
    def teacher(self):
        return self.fio, self.phone, self.email, self.comment

    def insert(self):
        conn = db=ConnectionPool.get_admin_connection()
        query = QSqlQuery(db=conn)
        data = self.user_data
        conn.transaction()
        query.prepare(INSERT_USER)
        query.addBindValue(data[0])
        query.addBindValue(data[1])
        query.addBindValue(data[2])
        if query.exec() and query.first():
            self.user_id = query.value("id")
            query.prepare(INSERT)
            data = self.teacher
            query.addBindValue(data[0])
            query.addBindValue(data[1])
            query.addBindValue(data[2])
            query.addBindValue(data[3])
            query.addBindValue(self.user_id)
            if query.exec():
                self.pk = query.lastInsertId()
                print(self.pk)
                conn.commit()
            else:
                conn.rollback()
                print(query.lastError().text())
        else:
            conn.rollback()
            print(query.lastError().text())





