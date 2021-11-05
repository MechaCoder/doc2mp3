import click
from rich.console import Console
from rich.live import Live

from psutil import cpu_percent

from doc.data import Pdf, TextData, Settings
from doc.extractor.pdf import convertPDF
from doc.extractor.media import Media


@click.group()
def cli(): pass

@cli.command()
@click.argument('path', type=click.Path(exists=True, file_okay=True, dir_okay=False))
def convert(path):
    """converts a pdf to mp3"""
    pdfData = Pdf()
    txtData = TextData()
    con = Console()

    if pdfData.exists('path', path) == False:

        # with con.status('importing data into system!'):
        with Live(f'importing data into system! :: CPU process {cpu_percent()}%', refresh_per_second=4):
            tag = pdfData.create(path) #  adds the the file to the system
            convertPDF(path, tag) #  converts the pdf to text

    doc = pdfData.readByPath(path)
    if txtData.exists('docTag', doc['key']) == False:
        with con.status('importing information from file'):
            doc = pdfData.readByPath(path)
            convertPDF(path, doc['key'])

    Media().ExportPage(doc['key'])
    con.print('Finshed')

@cli.command()
@click.argument('tag', type=click.Choice(Settings().getTags()))
@click.argument('value')
def settings(tag, value):
    """sets a declered setings"""

    if tag == 'tts-engine':
        if value != 'gtts' or value != 'pyttsx3':
            print(f'{value} is not a vaild tts libary')
            return

    if tag == 'sleep-time':
        try:
            value = float(value)
        except TypeError as err:
            print('sleep-time must float')
            return

    Settings().set(tag, value)

if __name__ == '__main__':
    cli()
