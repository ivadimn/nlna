from PyQt6.QtSql import QSqlQueryModel, QSqlQuery


SELECT_BY_ID = """
   SELECT f_title, f_comment 
   FROM groups
   WHERE id=? ; 
"""

INSERT = """
    INSERT INTO groups (f_title, f_comment) 
    VALUES(?, ?);
"""

UPDATE = """
    UPDATE groups SET f_title=?, f_comment=? 
    WHERE id=? ;
"""

DELETE = """
    DELETE FROM groups WHERE id=? ;
"""


class GroupModel(QSqlQueryModel):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.refresh()

    def refresh(self):
        sql = "SELECT id, f_title, f_comment FROM groups ;"
        self.setQuery(sql)

    def select(self, rid: int) -> tuple:
        query = QSqlQuery()
        query.prepare(SELECT_BY_ID)
        query.addBindValue(rid)
        query.exec()
        if query.first():
            result = (query.value("f_title"), query.value("f_comment"))
        else:
            result = (None, None,)
        return result

    def add(self, title: str, comment: str):
        query = QSqlQuery()
        query.prepare(INSERT)
        query.addBindValue(title)
        query.addBindValue(comment)
        query.exec()
        self.refresh()

    def update(self, rid: int, title: str, comment: str):
        query = QSqlQuery()
        query.prepare(UPDATE)
        query.addBindValue(title)
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