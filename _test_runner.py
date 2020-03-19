import unittest

from test.cli_test import CliTest
from test.board_test import BoardTest
from test.human_player_test import HumanPlayerTest
from test.computer_player_test import ComputerPlayerTest
from test.game_test import GameTest
from test.validator_test import ValidatorTest
from test.app_test import AppTest
from test.player_builder_test import PlayerBuilderTest
from test.three_by_three_presenter_test import ThreeByThreePresenterTest
from test.processor_test import ProcessorTest
from test.minimax_test import MinimaxTest
from test.strategy_builder_test import StrategyBuilderTest
from test.easy_strategy_test import EasyStrategyTest
from test.three_by_three_hard_strategy_test import ThreeByThreeHardStrategyTest

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(CliTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(HumanPlayerTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(ComputerPlayerTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(GameTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(ValidatorTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(AppTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(PlayerBuilderTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(BoardTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(ThreeByThreePresenterTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(ProcessorTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MinimaxTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(StrategyBuilderTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(EasyStrategyTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(ThreeByThreeHardStrategyTest))

    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

# Note: run the tests from the command line with:
# 'python3 -m unittest _test_runner.py -v'
