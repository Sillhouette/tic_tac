import unittest

import src.constants as constants

from unittest.mock import Mock
from src.strategy_builder import StrategyBuilder
from src.hard_strategy import HardStrategy
from src.easy_strategy import EasyStrategy

class StrategyBuilderTest(unittest.TestCase):
    def test_build_builds_3x3_hard_strat(self):
        processor = Mock()
        computer_player = Mock()
        processor.board = Mock()
        processor.board.type = constants.THREE_BY_THREE
        difficulty = constants.HARD
        strat_builder = StrategyBuilder(processor, computer_player)
        expected = True

        strat = strat_builder.build(difficulty)
        actual = isinstance(strat, HardStrategy)

        self.assertEqual(expected, actual)
    
    def test_build_builds_3x3_easy_strat(self):
        processor = Mock()
        computer_player = Mock()
        processor.board = Mock()
        processor.board.type = constants.THREE_BY_THREE
        difficulty = constants.EASY
        strat_builder = StrategyBuilder(processor, computer_player)
        expected = True

        strat = strat_builder.build(difficulty)
        actual = isinstance(strat, EasyStrategy)

        self.assertEqual(expected, actual)

