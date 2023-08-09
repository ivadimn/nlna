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

SELECT_ONE = """
    SELECT 
        u.f_login,
        t.f_fio,
        t.f_phone,
        t.f_email,
        t.f_comment,
        t.user_id
    from teacher as t
    inner join appuser as u
        on u.id = t.user_id 
    where t.id = ?	;
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

    def load(self) -> "Teacher":
        conn = db = ConnectionPool.get_admin_connection()
        query = QSqlQuery(db=conn)
        query.prepare(SELECT_ONE)
        query.addBindValue(self.pk)
        if query.exec() and query.first():
            self.login = query.value("f_login")
            self.fio = query.value("f_fio")
            self.phone = query.value("f_phone")
            self.email = query.value("f_email")
            self.comment = query.value("f_comment")
            self.user_id = query.value("user_id")
        else:
            print(query.lastError().text())
        return self


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





