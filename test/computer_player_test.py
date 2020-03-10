import unittest

from unittest.mock import Mock
from src.computer_player import ComputerPlayer
from src.three_by_three_board import ThreeByThreeBoard
from src.three_by_three_processor import ThreeByThreeProcessor

class ComputerPlayerTest(unittest.TestCase):
    def test_setting_computer_player_token(self):
        processor = Mock()
        cli = Mock()
        minimax = Mock()
        computer = ComputerPlayer(processor, cli, minimax)
        token = "%"
        expected = token

        computer.set_token(token)
        actual = computer.token

        self.assertEqual(expected, actual)

    def test_get_move_returns_a_valid_move_every_turn(self):
        board = ThreeByThreeBoard()
        processor = ThreeByThreeProcessor(board)
        cli = Mock()
        minimax = Mock()
        computer = ComputerPlayer(processor, cli, minimax)
        expected = True

        for space in board.spaces:
            move = computer.get_random_move()[1]
            index = processor.move_to_index(move)
            if not board.position_taken(index):
                board.update(index, computer.token)
        actual = board.full()

        self.assertEqual(expected, actual)

