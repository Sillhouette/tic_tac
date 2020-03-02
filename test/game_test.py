import unittest
import src.constants as constants

from unittest.mock import Mock, patch
from src.game import Game

class GameTest(unittest.TestCase):
    def test_player_chose_exit(self):
        cli = Mock()
        player_1, player_2 = Mock(), Mock()
        players = [player_1, player_2]
        board = Mock()
        validator = Mock()
        game = Game(cli, players, board, validator)
        expected_1 = True
        expected_2 = False

        actual_1 = game.player_chose_exit(constants.EXIT)
        actual_2 = game.player_chose_exit(constants.MOVE)

        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)

    def test_game_over(self):
        cli = Mock()
        cli.build_possible_results = Mock()
        cli.build_possible_results.return_value = {
            constants.EXIT: None,
            constants.FINISHED: None
        }
        player_1, player_2 = Mock(), Mock()
        players = [player_1, player_2]
        board = Mock()
        validator = Mock()
        game = Game(cli, players, board, validator)
        bad_input = "Gibberish"
        expected = True

        actual = game.game_over(constants.EXIT)
        actual_2 = game.game_over(constants.FINISHED)
        actual_3 = game.game_over(bad_input)

        self.assertEqual(expected, actual)
        self.assertEqual(expected, actual_2)
        self.assertNotEqual(expected, actual_3)

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

