import unittest

from unittest.mock import Mock, patch
from src.game import Game

class GameTest(unittest.TestCase):
    def test_current_player(self):
        cli = Mock()
        validator = Mock()
        player_1, player_2 = Mock(), Mock()
        players = [player_1, player_2]
        board = Mock()
        board.turn_count = Mock()
        board.turn_count.return_value = 5
        game = Game(cli, players, board, validator)
        expected = player_2

        actual = game.current_player()

        self.assertEqual(expected, actual)

    def test_current_player_2(self):
        cli = Mock()
        validator = Mock()
        player_1, player_2 = Mock(), Mock()
        players = [player_1, player_2]
        board = Mock()
        board.turn_count = Mock()
        board.turn_count.return_value = 8
        game = Game(cli, players, board, validator)
        expected = player_1

        actual = game.current_player()

        self.assertEqual(expected, actual)

