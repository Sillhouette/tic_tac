import unittest
import src.constants as constants

from unittest.mock import Mock, patch
from src.game import Game

class GameTest(unittest.TestCase):
    def test_player_chose_exit_returns_false_when_given_exit(self):
        cli = Mock()
        player_1, player_2 = Mock(), Mock()
        players = [player_1, player_2]
        board = Mock()
        validator = Mock()
        processor = Mock()
        game = Game(cli, players, board, validator, processor)
        expected = False

        actual = game.player_chose_exit(constants.MOVE)

        self.assertEqual(expected, actual)


    def test_player_chose_exit_returns_true_when_given_exit(self):
        cli = Mock()
        player_1, player_2 = Mock(), Mock()
        players = [player_1, player_2]
        board = Mock()
        validator = Mock()
        processor = Mock()
        game = Game(cli, players, board, validator, processor)
        expected = True

        actual = game.player_chose_exit(constants.EXIT)

        self.assertEqual(expected, actual)

    def test_game_over_returns_true_on_exit(self):
        cli = Mock()
        cli.build_possible_results = Mock()
        cli.build_possible_results.return_value = {
            constants.EXIT: None,
            constants.CATS: None
        }
        player_1, player_2 = Mock(), Mock()
        players = [player_1, player_2]
        board = Mock()
        validator = Mock()
        processor = Mock()
        game = Game(cli, players, board, validator, processor)
        expected = True

        actual = game.game_over(constants.EXIT)

        self.assertEqual(expected, actual)

    def test_game_over_returns_true_on_cats_game(self):
        cli = Mock()
        cli.build_possible_results = Mock()
        cli.build_possible_results.return_value = {
            constants.EXIT: None,
            constants.CATS: None
        }
        player_1, player_2 = Mock(), Mock()
        players = [player_1, player_2]
        board = Mock()
        validator = Mock()
        processor = Mock()
        game = Game(cli, players, board, validator, processor)
        expected = True

        actual = game.game_over(constants.CATS)

        self.assertEqual(expected, actual)

    def test_game_over_returns_false_on_other_input(self):
        cli = Mock()
        cli.build_possible_results = Mock()
        cli.build_possible_results.return_value = {
            constants.EXIT: None,
            constants.CATS: None
        }
        player_1, player_2 = Mock(), Mock()
        players = [player_1, player_2]
        board = Mock()
        validator = Mock()
        processor = Mock()
        game = Game(cli, players, board, validator, processor)
        bad_input = "Gibberish"
        expected = False

        actual = game.game_over(bad_input)

        self.assertEqual(expected, actual)

