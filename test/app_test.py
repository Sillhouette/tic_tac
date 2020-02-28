import unittest

from unittest.mock import Mock
from src.app import App
from src.player import Player
from src.three_by_three_board import ThreeByThreeBoard

class AppTest(unittest.TestCase):
    def test_setup_players(self):
        cli = Mock()
        cli.get_player_tokens = Mock()
        cli.get_player_tokens.return_value = ["X", "O"]
        app = App(cli)
        expected_length = 2
        expected_is_players = True

        actual = app.setup_players()
        actual_length = len(actual)
        actual_is_players = any(isinstance(player, Player) for player in actual)

        self.assertEqual(expected_length, actual_length)
        self.assertEqual(expected_is_players, actual_is_players)

    def test_setup_3x3_board(self):
        cli = Mock()
        cli.get_board_type = Mock()
        cli.get_board_type.return_value = "3x3"
        app = App(cli)
        expected = True

        board = app.setup_board()
        actual = isinstance(board, ThreeByThreeBoard)

        self.assertEqual(expected, actual)
