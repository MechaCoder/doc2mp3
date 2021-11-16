from os.path import isfile
from string import ascii_letters, digits
from random import choices

from tinydb.queries import Query

from .base import Base


def mkKey(l:int = 12):
    pool = choices(
        str(ascii_letters + digits),
        k=l
    )

    return ''.join(pool)


class Pdf(Base):

    def __init__(self, requiredKeys='path:str,key:str'):
        super().__init__(requiredKeys=requiredKeys)
        self.table = 'pdf'

    def create(self, path:str):
        key = mkKey(8)

        while self.exists('key', key):
            key = mkKey(8)

        if isfile(path) is False:
            raise Exception('this path dose not exists')

        if self.exists('path', path):
            raise Exception('this path already exists')

        row = {
            'path': path,
            'key': key
        }
        super().create(row)
        return key

    def readByPath(self, path:str):
        db = self.createObj()
        row = db.tbl.get(Query().path == path)
        db.close()

        return row

    def readTags(self):
        rList = []

        for e in self.readAll():
            rList.append(e['key'])
        return rList

    