import unittest

from unittest.mock import Mock
from src.three_by_three_easy_strategy import ThreeByThreeEasyStrategy
from src.computer_player import ComputerPlayer
from src.three_by_three_board import ThreeByThreeBoard
from src.three_by_three_processor import ThreeByThreeProcessor

class ThreeByThreeEasyStrategyTest(unittest.TestCase):

    def test_get_random_move_returns_a_valid_move_every_turn(self):
        board = ThreeByThreeBoard()
        processor = ThreeByThreeProcessor(board)
        cli = Mock()
        minimax = Mock()
        computer = ComputerPlayer(processor, cli, minimax)
        strat = ThreeByThreeEasyStrategy(processor, computer)
        expected = True

        for space in board.spaces:
            move = strat.get_random_move()[1]
            index = processor.move_to_index(move)
            if not board.position_taken(index):
                board.update(index, computer.token)
        actual = board.full()

        self.assertEqual(expected, actual)

    def test_execute_calls_get_random_move(self):
        processor = Mock()
        computer_player = Mock()
        strat = ThreeByThreeEasyStrategy(processor, computer_player)
        strat.get_random_move = Mock()

        strat.execute()

        strat.get_random_move.assert_called()
