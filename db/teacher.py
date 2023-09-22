from dataclasses import dataclass
from PyQt6.QtSql import QSqlQuery
from db.connection import ConnectionPool

import logging
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)


deprecated_INSERT_USER = """
    INSERT INTO appuser (f_login, f_salt, f_role)
    VALUES (?, ?, ?)
    returning id ;
"""

deprecated_INSERT = """
    INSERT INTO teacher (f_fio, f_phone, f_email, f_comment, user_id) 
    VALUES(?, ?, ?, ?, ?);
"""

# parameters: f_login, f_fio, f_phone, f_email, f_comment
INSERT_ONE = " SELECT new_teacher(?, ?, ?, ?, ?) ; "

# parameters: f_login, f_fio, f_phone, f_email, f_comment
UPDATE_ONE = " SELECT update_teacher(?, ?, ?, ?, ?) ; "

# parameters: f_login, f_fio, f_phone, f_email, f_comment
DELETE_ONE = " SELECT delete_teacher(?) ; "

deprecated_UPDATE = """
    UPDATE teacher SET f_fio=?, f_phone=?, f_email=?, f_comment=? 
    WHERE id=? ;
"""

deprecated_SELECT_ONE = """
    SELECT 
        u.f_login,
        u.f_fio,
        t.f_phone,
        u.f_email,
        u.f_comment,
        t.user_id
    from teacher as t
    inner join appuser as u
        on u.id = t.user_id 
    where t.id = ?	;
"""
SELECT_ONE = """
     SELECT pk, f_login, f_fio, f_phone, f_email, f_comment, user_id 
     FROM v_teacher
     WHERE pk = ?  ;
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
    def deprecated_user_data(self):
        return self.login, "1", "teacher"

    @property
    def teacher_data(self):
        return self.login, self.fio, self.phone, self.email, self.comment

    def load(self) -> "Teacher":
        conn = ConnectionPool.get_root_connection()
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
        conn = ConnectionPool.get_root_connection()
        query = QSqlQuery(db=conn)
        data = self.teacher_data
        query.prepare(INSERT_ONE)
        query.addBindValue(data[0])
        query.addBindValue(data[1])
        query.addBindValue(data[2])
        query.addBindValue(data[3])
        query.addBindValue(data[4])
        if query.exec() and query.first():
            self.pk = query.value(0)
            LOG.info("Teacher {0} inserted successfully!".format(self.fio))
        else:
            LOG.info(query.lastError().text())

    def update(self):
        conn = ConnectionPool.get_root_connection()
        query = QSqlQuery(db=conn)
        data = self.teacher_data
        query.prepare(UPDATE_ONE)
        query.addBindValue(self.pk)
        query.addBindValue(data[1])
        query.addBindValue(data[2])
        query.addBindValue(data[3])
        query.addBindValue(data[4])
        if query.exec():
            LOG.info("Teacher pk = {0} updated successfully!".format(self.pk))
        else:
            LOG.info(query.lastError().text())

    def delete(self):
        conn = ConnectionPool.get_root_connection()
        query = QSqlQuery(db=conn)
        query.prepare(DELETE_ONE)
        query.addBindValue(self.pk)
        if query.exec():
            LOG.info("Teacher pk = {0} deleted successfully!".format(self.pk))
        else:
            LOG.info(query.lastError().text())

    def save(self):
        if self.pk is None:
            return self.insert()
        else:
            return self.update()

