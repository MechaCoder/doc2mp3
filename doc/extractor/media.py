from posixpath import join
from time import sleep
from doc.data import TextData
from doc.data.settings import voice
from doc.data.settings.data import Settings
from doc.utills import checkPath, sleepy
from gtts import gTTS
from gtts.tts import gTTSError
from pyttsx3 import init
from rich.console import Console


class Media:

    def ExportPage(self, tag: str):

        obj = TextData()
        settings = Settings()
        dirPath = checkPath(tag)
        con = Console()

        ttsEngine = settings.get('tts-engine')
        engineVoice = settings.get('voice_pyttsx3')

        fnList = []

        with con.status(f'converting files useing {ttsEngine} ...'):
            for doc in obj.readAllByDoc(tag):

                fn = join(dirPath, f'{tag}-{doc["pageOn"]}.mp3')
                con.status(f'converting: {fn}')

                if ttsEngine == 'gtts':
                    try: #  gtts makes use of the google's tts and may fault becouse there are too many requests over a short space of time
                        tts = gTTS(doc['content'])
                        tts.save(fn)
                        continue
                    except gTTSError as err:
                        ttsEngine = 'pyttsx3'
                
                if ttsEngine == 'pyttsx3':
                    tts = init()
                    tts.setProperty('voice', engineVoice)
                    tts.save_to_file(doc['content'], fn)
                    tts.runAndWait()
                
                sleepy()

                fnList.append(fn)
                con.print(f'converted {fn}')
        return fnList

            
