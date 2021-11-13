from unittest import TestCase
from random import randint, choice
from os.path import join, dirname, abspath
from faker import Faker
from os import remove

from doc.data.pdf import Pdf, mkKey
from doc.data.text import TextData

class Tests_Pdf(TestCase):

    def setUp(self):
        try:
            remove(join(dirname(abspath('Pipfile')), 'ds.test.json'))
            pass
        except:
            pass
        return super().setUp()

    def test_init(self):

        obj = Pdf()
        obj.fileName = join(dirname(abspath('Pipfile')), 'ds.test.json')

        self.assertEqual(
            obj.table,
            'pdf'
        )

    def test_create(self):
        a = Pdf()
        a.fileName =  join(dirname(abspath('Pipfile')), 'ds.test.json')

        x = a.create( join(dirname(abspath('Pipfile')), 'Agenda Contents.pdf') )
        
        self.assertIsInstance(
            x, 
            str
        )

        self.assertEqual(
            len(x),
            8
        )
        

    def test_MkKey(self):

        obj = mkKey()
        self.assertIsInstance(
            obj,
            str
        )

        self.assertTrue(
            len(obj),
            12
        )

class Test_text(TestCase):

    def setUp(self):
        try:
            remove(join(dirname(abspath('Pipfile')), 'ds.test.json'))
            pass
        except:
            pass
        return super().setUp()

    def test_create(self):
        obj = TextData()
        obj.fileName =  join(dirname(abspath('Pipfile')), 'ds.test.json')

        x = obj.create(
            mkKey(),
            randint(1, 1000),
            'able'
        )

        self.assertIsInstance(
            x,
            int
        )


    def test_readAllByDoc(self):
        
        control = mkKey()
        b = [
            control,
            mkKey(),
            mkKey(),
            mkKey()
        ]

        obj = TextData()
        obj.fileName =  join(dirname(abspath('Pipfile')), 'ds.test.json')

        for e in range(1,5):

            obj.create(
                choice(b),
                randint(1, 10000),
                'bravo'
            )

        count = obj.readAllByDoc(control)
        self.assertIsInstance(count, list)
