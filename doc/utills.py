from genericpath import isfile
from os import mkdir
from os.path import isdir, abspath, dirname, join
from time import sleep

from psutil import cpu_percent

from doc.data.settings import Settings

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
    sleep(sObj.get('sleep-time'))
    cpu = cpu_percent()
    # print(f'CPU running at {cpu}%')
    if cpu >= 75: #  if the CPU is running about 75% or above sleep more.
        sleep(sObj.get('sleep-time') * 2)
    return True
