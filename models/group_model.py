from PyQt6.QtSql import QSqlQueryModel, QSqlQuery
from db.connection import ConnectionPool


SELECT_BY_ID = """
   SELECT f_title, f_comment 
   FROM stgroup
   WHERE id=? ; 
"""

INSERT = """
    INSERT INTO stgroup (f_title, f_comment) 
    VALUES(?, ?);
"""

UPDATE = """
    UPDATE stgroup SET f_title=?, f_comment=? 
    WHERE id=? ;
"""

DELETE = """
    DELETE FROM stgroup WHERE id=? ;
"""


class GroupModel(QSqlQueryModel):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__db = ConnectionPool.get_admin_connection()
        self.refresh()

    def refresh(self):
        sql = "SELECT id, f_title, f_comment FROM stgroup ;"
        self.setQuery(sql, db=self.__db)

    def select(self, rid: int) -> tuple:
        query = QSqlQuery(db=self.__db)
        query.prepare(SELECT_BY_ID)
        query.addBindValue(rid)
        query.exec()
        if query.first():
            result = (query.value("f_title"), query.value("f_comment"))
        else:
            result = (None, None,)
        return result

    def add(self, title: str, comment: str):
        query = QSqlQuery(db=self.__db)
        query.prepare(INSERT)
        query.addBindValue(title)
        query.addBindValue(comment)
        query.exec()
        self.refresh()

    def update(self, rid: int, title: str, comment: str):
        query = QSqlQuery(db=self.__db)
        query.prepare(UPDATE)
        query.addBindValue(title)
        query.addBindValue(comment)
        query.addBindValue(rid)
        query.exec()
        self.refresh()

    def delete(self, rid: int):
        query = QSqlQuery(db=self.__db)
        query.prepare(DELETE)
        query.addBindValue(rid)
        query.exec()
        self.refresh()
