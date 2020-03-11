import unittest

import src.constants as constants

from unittest.mock import Mock
from src.three_by_three_hard_strategy import ThreeByThreeHardStrategy
from src.three_by_three_board import ThreeByThreeBoard
from src.three_by_three_processor import ThreeByThreeProcessor
from src.computer_player import ComputerPlayer

class ThreeByThreeHardStrategyTest(unittest.TestCase):
    def test_execute_returns_1_on_first_turn(self):
        processor = Mock()
        processor.board = Mock()
        processor.board.turn_count = Mock()
        processor.board.turn_count.side_effect = [0]
        computer_player = Mock()
        strat = ThreeByThreeHardStrategy(processor, computer_player)
        expected = [constants.MOVE, "1"]

        actual = strat.execute()

        self.assertEqual(expected, actual)

    def test_execute_returns_appropriately_on_second_turn(self):
        SECOND_MOVE = {
            0: "5",
            1: "1",
            2: "5",
            3: "1",
            4: "1",
            5: "3",
            6: "5",
            7: "2",
            8: "5"
        }
        processor = Mock()
        processor.board = Mock()
        processor.board.turn_count = Mock()
        processor.board.turn_count.side_effect = [1] * 9
        side_effects = [[key] for key in SECOND_MOVE.keys()]
        processor.get_taken_positions.side_effect = side_effects 
        computer_player = Mock()
        strat = ThreeByThreeHardStrategy(processor, computer_player)

        for value in SECOND_MOVE.values():
            expected = [constants.MOVE, value]
            
            actual = strat.execute()

            self.assertEqual(expected, actual)

