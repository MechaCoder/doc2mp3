from tempfile import TemporaryDirectory
from pdf2image import convert_from_path
from pytesseract import image_to_string

from rich.progress import track

from doc.data import Pdf, TextData, Settings
from doc.utills import sleepy, getPdfPagesAmount

def convertPDF(src:str, tag:str):

    objpdf = Pdf()
    objtxt = TextData()

    pageNum = getPdfPagesAmount(src)


    if objpdf.exists('path', src) == False:
        raise Exception('this file has not been added to the system')

    if objpdf.exists('key', tag) == False:
        raise Exception('this key has not been recoinsed')

    with TemporaryDirectory() as path:
        imgs = convert_from_path(
            pdf_path=src,
            output_folder=path,
            fmt='jpeg'
        )

        docIds = []

        for Img in track(imgs, description='processing'):
            text = image_to_string(
                Img,
                lang=Settings().get('pytesseract-lang')
            )

            if objtxt.exists('pageOn', len(docIds)) and objtxt.exists('docTag', tag):
                # check to make sure that page dose not already exists
                continue
            
            print(f'added to: {tag} page {len(docIds)} of {pageNum} ')
            sleepy()
            doc = objtxt.create(
                tag,
                len(docIds),
                text
            )
            docIds.append(doc)
    return docIds
