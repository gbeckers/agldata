import unittest
from agldata import availablestudies, get_stringdata
from agldata.stringdata import StringData


class DataFiles(unittest.TestCase):

    def test_validkeys(self):
        for study in availablestudies:
            self.assertIsInstance(get_stringdata(study), StringData)