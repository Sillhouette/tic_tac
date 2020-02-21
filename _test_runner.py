import unittest

from test.cli_test import CliTest
from test.board_test import BoardTest
from test.player_test import PlayerTest
from test.game_test import GameTest

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(CliTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(BoardTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(PlayerTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(GameTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

# Note: run the tests from the command line with:
# 'python3 -m unittest _test_runner.py -v'
