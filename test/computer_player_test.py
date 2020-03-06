import unittest

from unittest.mock import Mock
from src.computer_player import ComputerPlayer
from src.three_by_three_board import ThreeByThreeBoard

class ComputerPlayerTest(unittest.TestCase):
    def test_setting_computer_player_token(self):
        board = Mock()
        cli = Mock()
        computer = ComputerPlayer(board, cli)
        token = "%"
        expected = token

        computer.set_token(token)
        actual = computer.token

        self.assertEqual(expected, actual)

    def test_get_move_returns_a_valid_move_every_turn(self):
        board = ThreeByThreeBoard()
        cli = Mock()
        computer = ComputerPlayer(board, cli)
        expected = True

        for space in board.spaces:
            move = computer.get_move()[1]
            index = board.move_to_index(move)
            if not board.position_taken(index):
                board.update(move, computer.token)
        actual = board.full()

        self.assertEqual(expected, actual)
