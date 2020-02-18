import unittest

from test.cli_test import CliTest
from test.board_test import BoardTest

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(CliTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(BoardTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

# Note: run the tests from the command line with:
# 'python3 -m unittest _test_runner.py'
