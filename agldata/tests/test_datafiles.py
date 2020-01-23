import unittest
from agldata import availablestudies, get_datadict


class DataFiles(unittest.TestCase):

    def test_validkeys(self):
        validkeys = {"readingframe",
                     "strings",
                     "categories",
                     "categorycolors",
                     "tokendurations",
                     "tokenintervalduration",
                     "categorycomparisons"}
        for study in availablestudies:
            for key in get_datadict(study).keys():
                self.assertIn(key, validkeys)
