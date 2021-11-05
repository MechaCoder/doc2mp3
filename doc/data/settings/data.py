from os.path import join, dirname, abspath
from tinydb_base import factory
from tinydb_base.getSet import GetSet, Factory

class Settings(GetSet):

    def __init__(self, table: str = 'settings'):
        file = join(dirname(abspath('Pipfile')), 'ds.json' )
        super().__init__(file=file, table=table)

        self.defaultRows({
            'voice_pyttsx3': 'default',
            'tts-engine': 'gtts',
            'sleep-time': 5,
            'pytesseract-lang': 'eng'
        })

    def getTags(self):

        factory = Factory(self.fileName, self.tableName)
        rList = []

        for row in factory.tbl.all():
            rList.append(row['tag'])

        return rList
