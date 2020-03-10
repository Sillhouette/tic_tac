import unittest

from test.cli_test import CliTest
from test.three_by_three_board_test import ThreeByThreeBoardTest
from test.human_player_test import HumanPlayerTest
from test.computer_player_test import ComputerPlayerTest
from test.game_test import GameTest
from test.board_builder_test import BoardBuilderTest
from test.three_by_three_validator_test import ThreeByThreeValidatorTest
from test.app_test import AppTest
from test.player_builder_test import PlayerBuilderTest
from test.validator_builder_test import ValidatorBuilderTest
from test.three_by_three_presenter_test import ThreeByThreePresenterTest
from test.three_by_three_processor_test import ThreeByThreeProcessorTest

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(CliTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(HumanPlayerTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(ComputerPlayerTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(GameTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(BoardBuilderTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(ThreeByThreeValidatorTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(AppTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(PlayerBuilderTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(ThreeByThreeBoardTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(ValidatorBuilderTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(ThreeByThreePresenterTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(ThreeByThreeProcessorTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

# Note: run the tests from the command line with:
# 'python3 -m unittest _test_runner.py -v'
