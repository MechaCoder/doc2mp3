from rich.table import Table
from rich.console import Console
from pyttsx3 import init
from click import prompt, confirm, Choice

from .data import Settings

def newVoiceIdOffline(): 
    # TODO: list and print out a table of voices presnt in the system.
    # TODO: allow user select a id

    tbl = Table(title='Available voices')
    tbl.add_column('Name')
    tbl.add_column('Gender')
    # tbl.add_column('Age')

    engine = init()
    con = Console()
    c = []
    for voice in engine.getProperty('voices'):
        tbl.add_row(
            str(voice.id),
            str(voice.gender)
        )
        c.append(voice.id)

    while True:
        txt = prompt('enter new voice id', type=Choice(c))
        
        engine.setProperty('voice', txt)
        engine.say('Spread love everywhere you go. Let no one ever come to you without leaving happier. -Mother Teresa')
        with con.status('speaking'):
            engine.runAndWait()

        if confirm('are you content', default=True):
            Settings().set('voice_pyttsx3', txt)
            break

