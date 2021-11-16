from genericpath import isfile
from os import mkdir
from os.path import isdir, abspath, dirname, join
from time import sleep

from psutil import cpu_percent
from requests import get

from doc.data.settings import Settings
from PyPDF4 import PdfFileReader

def checkPath(docTag:str):

    projectRoot = dirname(abspath('Pipfile'))
    path = join(projectRoot, 'outputed_files', docTag)

    if isdir(join(projectRoot, 'outputed_files')) is False:
        mkdir(join(projectRoot, 'outputed_files'))

    if isdir(path) is False:
        mkdir(path)

    return path


def sleepy():
    sObj = Settings()
    val = sObj.get('sleep-time')
    sleep(val)
    # cpu = cpu_percent()
    if cpu_percent() >= 75: #  if the CPU is running about 75% or above sleep more.
        sleep(val)
    
    return True

def downloadFileFromURL(url:str, fname:str):
    req = get(url, allow_redirects=True)
    f = open(fname, 'wb')
    f.write(req.content)
    f.close()
    return True

def getPdfPagesAmount(path:str):
    fileObj = open(
        path,
        'rb'
    )

    pdf = PdfFileReader(fileObj)
    num = pdf.getNumPages()
    fileObj.close()
    return num