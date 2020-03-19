import unittest
import src.constants as constants

from unittest.mock import Mock
from src.easy_strategy import EasyStrategy
from src.computer_player import ComputerPlayer
from src.board import Board
from src.processor import Processor

class EasyStrategyTest(unittest.TestCase):

    def test_get_random_move_returns_a_valid_move_every_turn(self):
        board = Board(constants.THREE_BY_THREE)
        processor = Processor(board)
        cli = Mock()
        minimax = Mock()
        computer = ComputerPlayer(processor, cli, minimax)
        strat = EasyStrategy(processor, computer)
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
        strat = EasyStrategy(processor, computer_player)
        strat.get_random_move = Mock()

        strat.execute()

        strat.get_random_move.assert_called()

