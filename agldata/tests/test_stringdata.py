import unittest
from agldata import availablestudies, get_stringdata
from agldata.stringdata import StringData


class TestStringData(unittest.TestCase):
    def test_validkeys(self):
        for study in availablestudies:
            self.assertIsInstance(get_stringdata(study), StringData, msg=study)