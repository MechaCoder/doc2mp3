from tinydb import Query
from .base import Base

class TextData(Base):

    def __init__(self, requiredKeys='pageOn:int,docTag:str,content:str'):
        super().__init__(requiredKeys=requiredKeys)
        self.table = 'text'

    def create(self, doc, page, content):

        db = self.createObj()
        if db.tbl.contains((Query().pageOn == page) & (Query().docTag == doc)):
            return 0

        row = {
            'pageOn': page,
            'docTag': doc,
            'content': content
        }
        db.close()
        return super().create(row)


    def readAllByDoc(self, doc:str):

        obj = self.createObj()
        rows = obj.tbl.search(
            Query().docTag == doc
        )

        obj.close()
        return rows
