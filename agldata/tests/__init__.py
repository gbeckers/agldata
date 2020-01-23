from unittest import TestLoader, TextTestRunner, TestSuite

from . import test_datafiles
from . import test_stringdata

modules = [test_datafiles, test_stringdata]

def test(verbosity=1):
    suite =TestSuite()
    for module in modules:
        suite.addTests(TestLoader().loadTestsFromModule(module))
    return TextTestRunner(verbosity=verbosity).run(suite)