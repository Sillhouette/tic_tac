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

    def test_current_player_returns_current_player_on_turn_5(self):
        cli = Mock()
        validator = Mock()
        player_1, player_2 = Mock(), Mock()
        players = [player_1, player_2]
        board = Mock()
        processor = Mock()
        board.turn_count = Mock()
        board.turn_count.return_value = 5
        game = Game(cli, players, board, validator, processor)
        expected = player_2

        actual = game.current_player()

        self.assertEqual(expected, actual)

    def test_current_player_returns_current_player_on_turn_8(self):
        cli = Mock()
        validator = Mock()
        player_1, player_2 = Mock(), Mock()
        players = [player_1, player_2]
        board = Mock()
        processor = Mock()
        board.turn_count = Mock()
        board.turn_count.return_value = 8
        game = Game(cli, players, board, validator, processor)
        expected = player_1

        actual = game.current_player()

        self.assertEqual(expected, actual)

