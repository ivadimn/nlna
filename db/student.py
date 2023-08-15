from dataclasses import dataclass
from PyQt6.QtSql import QSqlQuery
from .connection import ConnectionPool

INSERT_USER = """
    INSERT INTO appuser (f_login, f_salt, f_role)
    VALUES (?, ?, ?)
    returning id ;
"""

INSERT = """
    INSERT INTO student (f_fio, f_email, f_comment, user_id) 
    VALUES(?, ?, ?, ?);
"""

UPDATE = """
    UPDATE student SET f_fio=?, f_email=?, f_comment=? 
    WHERE id=? ;
"""

SELECT_ONE = """
    SELECT 
        u.f_login,
        t.f_fio,
        t.f_email,
        t.f_comment,
        t.user_id
    from student as t
    inner join appuser as u
        on u.id = t.user_id 
    where t.id = ?	;
"""


@dataclass
class Student:
    pk: int = None
    login: str = None
    fio: str = None
    email: str = None
    comment: str = None
    user_id: int = None

    @property
    def user_data(self):
        return self.login, "1", "student"

    @property
    def student(self):
        return self.fio, self.email, self.comment

    def load(self) -> "Student":
        conn = db = ConnectionPool.get_admin_connection()
        query = QSqlQuery(db=conn)
        query.prepare(SELECT_ONE)
        query.addBindValue(self.pk)
        if query.exec() and query.first():
            self.login = query.value("f_login")
            self.fio = query.value("f_fio")
            self.email = query.value("f_email")
            self.comment = query.value("f_comment")
            self.user_id = query.value("user_id")
        else:
            print(query.lastError().text())
        return self

    def insert(self):
        conn = db = ConnectionPool.get_admin_connection()
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
            data = self.student
            query.addBindValue(data[0])
            query.addBindValue(data[1])
            query.addBindValue(data[2])
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

    def update(self):
        conn = db = ConnectionPool.get_admin_connection()
        query = QSqlQuery(db=conn)
        data = self.student
        query.prepare(UPDATE)
        query.addBindValue(data[0])
        query.addBindValue(data[1])
        query.addBindValue(data[2])
        query.addBindValue(data[3])
        query.addBindValue(self.pk)
        if not query.exec():
            print(query.lastError().text())

    def save(self):
        if self.pk is None:
            return self.insert()
        else:
            return self.update()