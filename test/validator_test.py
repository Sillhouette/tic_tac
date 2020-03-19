import unittest
import src.constants as constants

from unittest.mock import Mock
from src.validator import Validator
from src.board import Board
from src.processor import Processor
from src.cli import Cli

class ValidatorTest(unittest.TestCase):
    def test_validate_returns_proper_action_when_move_is_valid(self):
        move = "1"
        board = Board(constants.THREE_BY_THREE)
        processor = Processor(board)
        validator = Validator()
        validator.set_processor(processor)
        expected = ["move", "1"]

        actual = validator.validate(move)

        self.assertEqual(expected, actual)

    def test_validate_returns_error_action_when_move_not_valid(self):
        board = Board(constants.THREE_BY_THREE)
        move = "Gibberish"
        processor = Processor(board)
        validator = Validator()
        validator.set_processor(processor)
        expected = ["error", "gibberish"]

        actual = validator.validate(move)

        self.assertEqual(expected, actual)

    def test_validate_returns_error_action_when_move_out_of_bounds(self):
        board = Board(constants.THREE_BY_THREE)
        move = "87"
        processor = Processor(board)
        validator = Validator()
        validator.set_processor(processor)
        expected = ["error", "87"]

        actual = validator.validate(move)

        self.assertEqual(expected, actual)

    @unittest.skip("Validator no longer has this method")
    def test_validate_input_returns_false_when_not_valid(self):
        board = Board(constants.THREE_BY_THREE)
        move = "gibberish"
        processor = Processor(board)
        validator = Validator()
        validator.set_processor(processor)
        expected = False

        actual = validator.validate_input(move)

        self.assertEqual(expected, actual)

    @unittest.skip("Validator no longer has this method")
    def test_validate_input_returns_true_when_valid(self):
        board = Board(constants.THREE_BY_THREE)
        move = "6"
        processor = Processor(board)
        validator = Validator()
        validator.set_processor(processor)
        expected = True

        actual = validator.validate_input(move)

        self.assertEqual(expected, actual)

    @unittest.skip("Validator no longer has this method")
    def test_get_valid_player_choice_returns_valid_choice(self):
        processor = Mock()
        validator = Validator()
        validator.set_processor(processor)
        cli = Mock(Cli)
        choice = "1"
        cli.get_opponent.return_value = choice
        expected = choice

        actual = validator.get_valid_player_choice(cli)

        self.assertEqual(expected, actual)

    @unittest.skip("Validator no longer has this method")
    def test_get_valid_choice_returns_exit_when_chosen(self):
        processor = Mock()
        validator = Validator()
        validator.set_processor(processor)
        cli = Mock(Cli)
        choice = constants.EXIT
        cli.get_opponent.return_value = choice
        expected = choice

        actual = validator.get_valid_player_choice(cli)

        self.assertEqual(expected, actual)

    @unittest.skip("Validator no longer has this method")
    def test_get_valid_choice_only_returns_valid_choice(self):
        processor = Mock()
        validator = Validator()
        validator.set_processor(processor)
        cli = Mock(Cli)
        choices = ["gibberish", constants.EXIT]
        cli.get_opponent.side_effect = choices
        expected = constants.EXIT

        actual = validator.get_valid_player_choice(cli)

        self.assertEqual(expected, actual)

