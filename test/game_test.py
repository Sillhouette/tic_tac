import unittest
import src.constants as constants

from unittest.mock import Mock, patch
from src.game import Game
from src.cli import Cli
from src.human_player import HumanPlayer
from src.three_by_three_board import ThreeByThreeBoard
from src.three_by_three_processor import ThreeByThreeProcessor

class GameTest(unittest.TestCase):
    def test_game_loop_plays_full_game(self):
        reader, writer = Mock(), Mock()
        cli = Cli(writer, reader)
        cli.print_board = Mock()
        cli.log = Mock()
        player_1, player_2 = Mock(HumanPlayer), Mock(HumanPlayer)
        player_1.token = "X"
        player_2.token = "O"
        action = constants.MOVE
        player_1.get_move.side_effect = [
            [action, "1"],
            [action, "3"],
            [action, "4"],
            [action, "5"],
            [action, "8"]
        ]
        player_2.get_move.side_effect = [
            [action, "2"],
            [action, "6"],
            [action, "7"],
            [action, "9"]
        ]
        players = [player_1, player_2]
        board = ThreeByThreeBoard()
        processor = ThreeByThreeProcessor(board)
        processor.set_players(players)
        game = Game(cli, players, board, processor)
        expected = True
        expected_print_board_call_count = 10
        expected_p1_get_move_count = 5
        expected_p2_get_move_count = 4

        game.play()

        print_board_call_count = cli.print_board.call_count
        p1_get_move_count = player_1.get_move.call_count
        p2_get_move_count = player_2.get_move.call_count

        self.assertEqual(expected_print_board_call_count, print_board_call_count)
        self.assertEqual(expected_p1_get_move_count, p1_get_move_count)
        self.assertEqual(expected_p2_get_move_count, p2_get_move_count)
        cli.log.assert_called_with("Cats game! You all played phenomenally!")

    def test_player_chose_exit_returns_false_when_given_exit(self):
        cli = Mock()
        player_1, player_2 = Mock(), Mock()
        players = [player_1, player_2]
        board = Mock()
        processor = Mock()
        game = Game(cli, players, board, processor)
        expected = False

        actual = game.player_chose_exit(constants.MOVE)

        self.assertEqual(expected, actual)

    def test_player_chose_exit_returns_true_when_given_exit(self):
        cli = Mock()
        player_1, player_2 = Mock(), Mock()
        players = [player_1, player_2]
        board = Mock()
        processor = Mock()
        game = Game(cli, players, board, processor)
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
        processor = Mock()
        game = Game(cli, players, board, processor)
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
        processor = Mock()
        game = Game(cli, players, board, processor)
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
        processor = Mock()
        game = Game(cli, players, board, processor)
        bad_input = "Gibberish"
        expected = False

        actual = game.game_over(bad_input)

        self.assertEqual(expected, actual)

