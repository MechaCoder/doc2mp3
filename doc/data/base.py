from os.path import dirname, abspath, join
from tinydb_base import DatabaseBase

class Base(DatabaseBase):

    def __init__(self,requiredKeys='title:str'):
        table = 'BASE'
        file = join(dirname(abspath('Pipfile')), 'ds.json' )
        super().__init__(file=file, table=table, requiredKeys=requiredKeys)