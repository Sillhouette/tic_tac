import unittest
import src.constants as constants

from unittest.mock import Mock
from src.three_by_three_validator import ThreeByThreeValidator
from src.three_by_three_board import ThreeByThreeBoard
from src.three_by_three_processor import ThreeByThreeProcessor
from src.cli import Cli

class ThreeByThreeValidatorTest(unittest.TestCase):
    def test_validate_returns_proper_action_when_move_is_valid(self):
        move = "1"
        board = ThreeByThreeBoard()
        processor = ThreeByThreeProcessor(board)
        validator = ThreeByThreeValidator(processor)
        expected = ["move", "1"]

        actual = validator.validate(move)

        self.assertEqual(expected, actual)

    def test_validate_returns_error_action_when_move_not_valid(self):
        board = ThreeByThreeBoard()
        move = "Gibberish"
        processor = ThreeByThreeProcessor(board)
        validator = ThreeByThreeValidator(processor)
        expected = ["error", "gibberish"]

        actual = validator.validate(move)

        self.assertEqual(expected, actual)

    def test_validate_returns_error_action_when_move_out_of_bounds(self):
        board = ThreeByThreeBoard()
        move = "87"
        processor = ThreeByThreeProcessor(board)
        validator = ThreeByThreeValidator(processor)
        expected = ["error", "87"]

        actual = validator.validate(move)

        self.assertEqual(expected, actual)

    def test_validate_input_returns_false_when_not_valid(self):
        board = ThreeByThreeBoard()
        move = "gibberish"
        processor = ThreeByThreeProcessor(board)
        validator = ThreeByThreeValidator(processor)
        expected = False

        actual = validator.validate_input(move)

        self.assertEqual(expected, actual)

    def test_validate_input_returns_true_when_valid(self):
        board = ThreeByThreeBoard()
        move = "6"
        processor = ThreeByThreeProcessor(board)
        validator = ThreeByThreeValidator(processor)
        expected = True

        actual = validator.validate_input(move)

        self.assertEqual(expected, actual)

    def test_get_valid_player_choice_returns_valid_choice(self):
        processor = Mock()
        validator = ThreeByThreeValidator(processor)
        cli = Mock(Cli)
        choice = "1"
        cli.get_opponent.return_value = choice
        expected = choice

        actual = validator.get_valid_player_choice(cli)

        self.assertEqual(expected, actual)

    def test_get_valid_choice_returns_exit_when_chosen(self):
        processor = Mock()
        validator = ThreeByThreeValidator(processor)
        cli = Mock(Cli)
        choice = constants.EXIT
        cli.get_opponent.return_value = choice
        expected = choice

        actual = validator.get_valid_player_choice(cli)

        self.assertEqual(expected, actual)

    def test_get_valid_choice_only_returns_valid_choice(self):
        processor = Mock()
        validator = ThreeByThreeValidator(processor)
        cli = Mock(Cli)
        choices = ["gibberish", constants.EXIT]
        cli.get_opponent.side_effect = choices
        expected = constants.EXIT

        actual = validator.get_valid_player_choice(cli)

        self.assertEqual(expected, actual)

